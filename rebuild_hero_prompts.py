"""Rebuild hero image prompts from hero_image_queue_v3.json.

Extracts only OVERALL FEEL, DOMINANT ANCHOR, and VISIBLE TEXT IN THE IMAGE
from each old prompt and reassembles them into a clean, fixed-structure
prompt suitable for premium 4096x2048 personal-finance hero banners.

Usage:
    python rebuild_hero_prompts.py --mode test   # first 5 entries -> hero_image_queue_test5.json
    python rebuild_hero_prompts.py --mode final  # all entries     -> hero_image_queue_final.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SRC = Path(__file__).parent / "hero_image_queue_v3.json"
TEST_OUT = Path(__file__).parent / "hero_image_queue_test5.json"
FINAL_OUT = Path(__file__).parent / "hero_image_queue_final.json"


def extract_section(prompt: str, name: str) -> str:
    """Return the text under a `NAME:` heading until the next blank line or next ALL-CAPS heading."""
    pattern = rf"{re.escape(name)}:\s*\n(.*?)(?=\n\n|\n[A-Z][A-Z ]+:)"
    m = re.search(pattern, prompt, re.DOTALL)
    return m.group(1).strip() if m else ""


def clean_short_sentence(text: str, max_words: int) -> str:
    """Collapse to one short sentence, replace semicolons with commas, enforce word cap."""
    s = " ".join(text.split())
    s = s.replace("; ", ", ").replace(";", ",")
    words = s.split()
    if len(words) > max_words:
        s = " ".join(words[:max_words]).rstrip(",.;:")
    if not s.endswith("."):
        s = s.rstrip(",.;:") + "."
    return s


def extract_visible_text_lines(prompt: str) -> list[str]:
    """Pull only Eyebrow, Headline line 1, Headline line 2, and Headline line 3 (if present)."""
    block = re.search(
        r"VISIBLE TEXT IN THE IMAGE:\s*\n(.*?)(?=\n\n|\nTYPOGRAPHY:)",
        prompt,
        re.DOTALL,
    )
    if not block:
        return []

    wanted = {
        "Eyebrow": None,
        "Headline line 1": None,
        "Headline line 2": None,
        "Headline line 3": None,
    }

    for raw in block.group(1).splitlines():
        line = raw.strip()
        if not line.startswith("-"):
            continue
        if ":" not in line:
            continue
        label, value = line[1:].split(":", 1)
        label = label.strip()
        # Normalise "Headline line 3 (amber)" -> "Headline line 3"
        norm = re.sub(r"\s*\(.*?\)\s*$", "", label).strip()
        if norm not in wanted:
            continue
        # Preserve the value exactly as-is (including its surrounding quotes).
        wanted[norm] = value.strip()

    ordered = []
    for key in ("Eyebrow", "Headline line 1", "Headline line 2", "Headline line 3"):
        v = wanted[key]
        if v is None:
            if key == "Headline line 3":
                continue  # missing line 3 is allowed; do not invent
            continue
        ordered.append(f"- {v}")
    return ordered


NEW_TEMPLATE = """Wide landscape hero banner, 4096x2048 pixels, 2:1 ratio.
Premium flat editorial design for a personal finance blog.

Use a spacious layout with one dominant visual anchor,
clear breathing room, and strong hierarchy. The image should look like a
finished website hero, not an infographic or classroom chart.

STYLE:
{style}

DOMINANT VISUAL:
{dominant}

VISIBLE TEXT:
Render only this text, copied exactly:
{visible_text_lines}

No other words, labels, captions, UI text, annotations, placeholder text, or extra numbers.

COLOR:
Near-white or deep navy canvas. Amber accents. Blue labels. Green success details.
No palette swatches, color chips, visible hex codes, watermarks, website addresses,
brand burn-ins, decorative icons, shadows, 3D effects, bevels, or stock-finance props.

QUALITY:
Crisp high-resolution editorial banner suitable for final 4096x2048 export.
Clean edges, readable text, balanced spacing, and calm premium composition.
"""


def rebuild_prompt(old_prompt: str) -> str:
    overall = extract_section(old_prompt, "OVERALL FEEL")
    anchor = extract_section(old_prompt, "DOMINANT ANCHOR")
    style_line = clean_short_sentence(overall, 15)
    dominant_line = clean_short_sentence(anchor, 12)
    visible_lines = extract_visible_text_lines(old_prompt)
    return NEW_TEMPLATE.format(
        style=style_line,
        dominant=dominant_line,
        visible_text_lines="\n".join(visible_lines),
    )


def rebuild(data: dict, limit: int | None) -> dict:
    new_data = {"meta": data["meta"], "queue": []}
    queue = data["queue"]
    if limit is not None:
        queue = queue[:limit]
    for entry in queue:
        new_entry = dict(entry)  # preserve all non-prompt fields unchanged
        new_entry["prompt"] = rebuild_prompt(entry["prompt"])
        new_data["queue"].append(new_entry)
    return new_data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("test", "final"), required=True)
    args = parser.parse_args()

    with SRC.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if args.mode == "test":
        out = rebuild(data, limit=5)
        out_path = TEST_OUT
    else:
        out = rebuild(data, limit=None)
        out_path = FINAL_OUT

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Total entries rebuilt: {len(out['queue'])}")
    print(f"Output: {out_path.name}")


if __name__ == "__main__":
    main()
