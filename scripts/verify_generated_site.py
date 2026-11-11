#!/usr/bin/env python3
"""Smoke-test localized taxonomy navigation and published photos after Hugo builds."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"


def page(path: str, contains: list[str], excludes: list[str] | None = None) -> None:
    file = PUBLIC / path / "index.html"
    if not file.is_file():
        raise AssertionError(f"Missing generated page: {file.relative_to(ROOT)}")
    html = file.read_text(encoding="utf-8")
    for value in contains:
        if value not in html:
            raise AssertionError(f"{path}: expected string not present: {value!r}")
    for value in excludes or []:
        if value in html:
            raise AssertionError(f"{path}: unrelated content leaked into taxonomy page: {value!r}")


def main() -> None:
    page("fa/about", ["?year=2026#year-2026", "eventcategories/", "3343844-7"])
    for lang in ("en", "fi", "fa"):
        page(f"{lang}/eventcategories/sports-wellbeing",
             ["sorure-taxonomy-archive", "sports-october-2026", "data-archive-year", "sorure-year-filter-notice"],
             ["pickling-october-2026"])
        page(f"{lang}/eventtags/physical-activity", ["sorure-taxonomy-archive"])
        page(f"{lang}/blogcategories/association-updates",
             ["sorure-taxonomy-archive", "vaasa-environmental-volunteers-2026"],
             ["sports-october-2026"])
        page(f"{lang}/blogtags/volunteering", ["sorure-taxonomy-archive", "vaasa-environmental-volunteers-2026"])
        page(f"{lang}/blog/vaasa-environmental-volunteers-2026",
             ["environment-cleanup-2026-01.jpg", "environment-cleanup-2026-02.jpg",
              "environment-cleanup-2026-03.jpg", "environment-cleanup-2026-04.jpg",
              "environment-cleanup-2026-05.jpg", "sorure-taxonomy-category",
              "sorure-taxonomy-tag", "۲۵۰" if lang == "fa" else "250", "facebook.com/permalink.php"])
        page(f"{lang}/events/finnish-a0-summer-2026",
             ["finnish-a0-summer-2026-01.jpg", "finnish-a0-summer-2026-02.jpg"])
        page(f"{lang}/events/fun-art-june-05-2026",
             ["fun-art-june-05-2026-01.jpg"])
    # Every gallery photo must exist in the generated site, and each translation must reference it.
    for lang in ("en", "fi", "fa"):
        for slug, count in (("summer-picnic-2023", 4), ("nowruz-sizdah-2023", 3)):
            names = [f"{slug}-{n:02d}.jpg" for n in range(1, count + 1)]
            page(f"{lang}/events/{slug}", names)
            for image_name in names:
                asset = PUBLIC / "img" / "events" / image_name
                if not asset.is_file() or asset.stat().st_size < 8000:
                    raise AssertionError(f"Missing or empty photo: {image_name}")
    print("Generated-site smoke checks passed for all three languages.")


if __name__ == "__main__":
    main()
