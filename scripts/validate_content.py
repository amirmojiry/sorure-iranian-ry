#!/usr/bin/env python3
"""Validate public Hugo content taxonomy metadata without third-party packages."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = (ROOT / "data/content_taxonomy.yaml").read_text(encoding="utf-8")
LANGUAGES = {"en", "fi", "fa"}


def taxonomy_ids(group: str, field: str) -> set[str]:
    scope = re.search(rf"(?ms)^{re.escape(group)}:\n(.*?)(?=^[a-z]+:\n|\Z)", DATA)
    if not scope:
        raise ValueError(f"Missing taxonomy group: {group}")
    section = re.search(
        rf"(?ms)^  {re.escape(field)}:\n(.*?)(?=^  [a-z_]+:\n|\Z)",
        scope.group(1),
    )
    if not section:
        raise ValueError(f"Missing taxonomy section: {group}.{field}")
    return set(re.findall(r"^    ([a-z0-9-]+):\s*$", section.group(1), re.M))


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    out = {}
    for line in match.group(1).splitlines():
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip()
    return out


def classify(folder: str, name: str) -> tuple[int, dict[str, int]]:
    allowed_categories = taxonomy_ids(name, "categories")
    allowed_tags = taxonomy_ids(name, "tags")
    translations = {}
    by_year = Counter()
    for path in sorted((ROOT / "content" / folder).glob("*.md")):
        if path.name.startswith("_index."):
            continue
        parts = path.name.rsplit(".", 2)
        if len(parts) != 3 or parts[1] not in LANGUAGES:
            raise ValueError(f"{path}: expected a <slug>.<language>.md filename")
        slug, lang, _ = parts
        f = frontmatter(path)
        try:
            categories = json.loads(f[f"{name}categories"])
            tags = json.loads(f[f"{name}tags"])
        except (KeyError, ValueError, TypeError) as ex:
            raise ValueError(f"{path}: invalid {name} taxonomy field(s): {ex}") from ex
        if not isinstance(categories, list) or len(categories) != 1:
            raise ValueError(f"{path}: exactly one primary category is required")
        if categories[0] not in allowed_categories:
            raise ValueError(f"{path}: unknown category '{categories[0]}'")
        if not isinstance(tags, list) or len(tags) < 1 or len(set(tags)) != len(tags):
            raise ValueError(f"{path}: tags must be a nonempty list without duplicates")
        unknown = set(tags) - allowed_tags
        if unknown:
            raise ValueError(f"{path}: unknown tags {sorted(unknown)}")
        if name == "event":
            year = f.get("event_year", "").strip('"')
            if not re.fullmatch(r"20\d{2}", year):
                raise ValueError(f"{path}: invalid event_year '{year}'")
            by_year.setdefault(year, 0)
        else:
            year = ""
        record = (tuple(categories), tuple(tags), year)
        translations.setdefault(slug, {})[lang] = record
    for slug, variants in translations.items():
        if set(variants) != LANGUAGES:
            raise ValueError(f"{folder}/{slug}: missing translation(s) {sorted(LANGUAGES - set(variants))}")
        if len(set(variants.values())) != 1:
            raise ValueError(f"{folder}/{slug}: taxonomy or year differs across translations")
        if name == "event":
            by_year[next(iter(variants.values()))[2]] += 1
    return len(translations), dict(sorted(by_year.items()))


def main() -> None:
    try:
        events, years = classify("events", "event")
        blogs, _ = classify("blog", "blog")
    except ValueError as error:
        print(f"Content validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Content taxonomy OK: {events} events and {blogs} blog posts, each in en/fi/fa.")
    print("Documented event entries per year:", years)


if __name__ == "__main__":
    main()
