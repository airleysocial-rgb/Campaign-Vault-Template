#!/usr/bin/env python3
"""
filter_public.py -- Filters vault content for public wiki publication.

PUBLISHING RULES
----------------
A file is published if and only if its YAML frontmatter contains:

    publish: true

Files without this field, or with publish: false, are silently skipped.
No folder-level assumptions are made -- the flag is the single source of truth.

PROCESSING
----------
NPC files (tagged `- npc`):
    Published as player-facing stubs. Strips: Motivations, Secrets,
    Connections, Background, Plot Hooks, Encounter Notes, Session Log,
    DM Notes, DM Eyes Only callouts.

All other files:
    Published with DM-only content stripped: ## DM Notes sections,
    > [!warning] DM Eyes Only callouts, hidden_goal frontmatter field.

Faction files (tagged `- faction`):
    Dataview code blocks are replaced with static markdown tables built
    from vault frontmatter. Quartz does not execute Dataview -- pre-rendering
    here ensures NPC and PC lists display correctly on the wiki.

NEVER PUBLISHED (regardless of publish flag)
--------------------------------------------
    dm/          -- DM-only documents
    _templates/  -- Obsidian templates
    .obsidian/   -- Obsidian config
    .github/     -- CI/CD config
    scripts/     -- build scripts
    sessions/    -- Session notes (DM only)
    quests/      -- Quest files (DM only)
"""

import re
import shutil
from pathlib import Path

VAULT = Path(".")
OUT = Path("public-content")

# These directories are always skipped, even if a file inside has publish: true
ALWAYS_SKIP_DIRS = {
    "dm",
    "_templates",
    ".obsidian",
    ".github",
    "scripts",
    "sessions",
    "quests",
}

STRIP_SECTIONS_ALL = ["DM Notes"]

NPC_STRIP_SECTIONS = [
    "Motivations & Goals",
    "Secrets",
    "Connections",
    "Background",
    "Plot Hooks",
    "Encounter Notes",
    "Session Log",
    "D&D Mechanics Notes",
    "Personality",
]

STRIP_FRONTMATTER_FIELDS_ALL = ["hidden_goal"]
NPC_STRIP_FRONTMATTER = ["alignment"]


# -- Frontmatter helpers -------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (fields dict, body_after_closing_dashes). Fields are raw strings."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    block = text[3:end]
    body = text[end + 3:]
    fields = {}
    for line in block.splitlines():
        m = re.match(r"^(\w+):\s*(.*)", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields, body


def should_publish(text: str) -> bool:
    """Return True only if frontmatter contains 'publish: true'."""
    fields, _ = parse_frontmatter(text)
    return fields.get("publish", "false").lower() == "true"


def is_npc(text: str) -> bool:
    """Return True if the file has '- npc' in its tags block."""
    return bool(re.search(r"^\s*-\s*npc\s*$", text, re.MULTILINE))


def is_pc(text: str) -> bool:
    """Return True if the file has '- pc' in its tags block."""
    return bool(re.search(r"^\s*-\s*pc\s*$", text, re.MULTILINE))


def is_faction(text: str) -> bool:
    """Return True if the file has '- faction' in its tags block."""
    return bool(re.search(r"^\s*-\s*faction\s*$", text, re.MULTILINE))


def strip_wiki_link(value: str) -> str:
    """Convert [[Link]] or [[Link|Alias]] to plain text."""
    m = re.match(r"^\[\[([^\]|]+)(?:\|[^\]]+)?\]\]$", value.strip('"').strip("'"))
    return m.group(1) if m else value.strip('"').strip("'")


# -- Vault data collection -----------------------------------------------------

def collect_characters(vault: Path) -> tuple[dict, dict]:
    """
    Scan vault for NPC and PC files. Return two dicts keyed by faction name:
        npc_by_faction: { "Faction Name": [ {name, race, role, status, location}, ... ] }
        pc_by_faction:  { "Faction Name": [ {name, player, race, class, level}, ... ] }
    """
    npc_by_faction: dict[str, list] = {}
    pc_by_faction: dict[str, list] = {}

    for md_file in sorted(vault.rglob("*.md")):
        parts = set(md_file.parts)
        if parts & ALWAYS_SKIP_DIRS:
            continue
        try:
            md_file.relative_to(OUT)
            continue
        except ValueError:
            pass

        content = md_file.read_text(encoding="utf-8-sig")
        fields, _ = parse_frontmatter(content)

        if not (is_npc(content) or is_pc(content)):
            continue

        raw_faction = fields.get("faction", "")
        faction_name = strip_wiki_link(raw_faction)
        if not faction_name:
            continue

        name = md_file.stem

        if is_npc(content):
            entry = {
                "name": name,
                "race": fields.get("race", ""),
                "role": fields.get("role", ""),
                "status": fields.get("status", ""),
                "location": strip_wiki_link(fields.get("location", "")),
            }
            npc_by_faction.setdefault(faction_name, []).append(entry)

        elif is_pc(content):
            entry = {
                "name": name,
                "player": fields.get("player", ""),
                "race": fields.get("race", ""),
                "class": fields.get("class", ""),
                "level": fields.get("level", ""),
            }
            pc_by_faction.setdefault(faction_name, []).append(entry)

    return npc_by_faction, pc_by_faction


def build_npc_table(npcs: list) -> str:
    """Render a list of NPC dicts as a markdown table."""
    if not npcs:
        return "*No key NPCs on record.*"
    rows = ["| Name | Race | Role | Status | Location |",
            "|---|---|---|---|---|"]
    for npc in sorted(npcs, key=lambda x: x["name"]):
        name_link = f"[[{npc['name']}]]"
        rows.append(
            f"| {name_link} | {npc['race']} | {npc['role']} | {npc['status']} | {npc['location']} |"
        )
    return "\n".join(rows)


def build_pc_table(pcs: list) -> str:
    """Render a list of PC dicts as a markdown table."""
    if not pcs:
        return "*No player characters assigned to this faction.*"
    rows = ["| Name | Player | Race | Class | Level |",
            "|---|---|---|---|---|"]
    for pc in sorted(pcs, key=lambda x: x.get("level", "0"), reverse=True):
        name_link = f"[[{pc['name']}]]"
        rows.append(
            f"| {name_link} | {pc['player']} | {pc['race']} | {pc['class']} | {pc['level']} |"
        )
    return "\n".join(rows)


def resolve_dataview(text: str, faction_name: str,
                     npc_by_faction: dict, pc_by_faction: dict) -> str:
    """
    Replace ```dataview ... ``` blocks in faction files with static markdown tables.
    Detects whether the block queries #npc or #pc and renders accordingly.
    """
    def replacer(match: re.Match) -> str:
        block = match.group(1)
        if "#pc" in block or "FROM #pc" in block:
            pcs = pc_by_faction.get(faction_name, [])
            return build_pc_table(pcs)
        elif "#npc" in block or "FROM #npc" in block:
            npcs = npc_by_faction.get(faction_name, [])
            return build_npc_table(npcs)
        return f"```\n{block}```"

    return re.sub(r"```dataview\n(.*?)```", replacer, text, flags=re.DOTALL)


# -- Content stripping ---------------------------------------------------------

def strip_dm_callouts(text: str) -> str:
    """Remove > [!warning] DM Eyes Only callout blocks."""
    lines = text.split("\n")
    result = []
    in_callout = False
    for line in lines:
        if re.match(r"^> \[!warning\] DM Eyes Only", line):
            in_callout = True
            continue
        if in_callout:
            if re.match(r"^>", line) or line.strip() == ">":
                continue
            else:
                in_callout = False
        result.append(line)
    return "\n".join(result)


def strip_section(text: str, section_name: str) -> str:
    """Remove a markdown section and everything under it until the next same-level heading."""
    lines = text.split("\n")
    result = []
    skip = False
    skip_level = 0
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.+)", line)
        if m:
            level = len(m.group(1))
            name = m.group(2).strip()
            if name == section_name:
                skip = True
                skip_level = level
                continue
            if skip and level <= skip_level:
                skip = False
        if not skip:
            result.append(line)
    return "\n".join(result)


def strip_frontmatter_fields(text: str, fields: list) -> str:
    """Remove specific keys from YAML frontmatter."""
    if not text.startswith("---"):
        return text
    end = text.find("---", 3)
    if end == -1:
        return text
    frontmatter_block = text[3:end]
    body = text[end + 3:]
    lines = frontmatter_block.split("\n")
    filtered = []
    skip_field = False
    for line in lines:
        field_match = re.match(r"^(\w+):", line)
        if field_match:
            skip_field = field_match.group(1) in fields
        if not skip_field:
            filtered.append(line)
    return "---" + "\n".join(filtered) + "---" + body


def clean_whitespace(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# -- Per-file processing -------------------------------------------------------

def process_general(text: str) -> str:
    """Strip DM content from a world/rules/player-resources file."""
    text = strip_dm_callouts(text)
    for section in STRIP_SECTIONS_ALL:
        text = strip_section(text, section)
    text = strip_frontmatter_fields(text, STRIP_FRONTMATTER_FIELDS_ALL)
    return clean_whitespace(text)


def process_faction(text: str, faction_name: str,
                    npc_by_faction: dict, pc_by_faction: dict) -> str:
    """Strip DM content from a faction file and pre-render Dataview queries."""
    text = strip_dm_callouts(text)
    for section in STRIP_SECTIONS_ALL:
        text = strip_section(text, section)
    text = strip_frontmatter_fields(text, STRIP_FRONTMATTER_FIELDS_ALL)
    text = resolve_dataview(text, faction_name, npc_by_faction, pc_by_faction)
    return clean_whitespace(text)


def process_npc_stub(text: str) -> str:
    """Generate a player-facing NPC stub -- appearance and personality only."""
    text = strip_dm_callouts(text)
    for section in NPC_STRIP_SECTIONS + STRIP_SECTIONS_ALL:
        text = strip_section(text, section)
    text = strip_frontmatter_fields(text, NPC_STRIP_FRONTMATTER + STRIP_FRONTMATTER_FIELDS_ALL)
    text = re.sub(
        r"(# .+\n)",
        r"\1\n> *What is publicly known about this individual.*\n\n",
        text,
        count=1,
    )
    return clean_whitespace(text)


# -- Folder index pages --------------------------------------------------------

def build_folder_index(title: str, description: str, links: list[str]) -> str:
    """Generate a simple index page for a published folder."""
    link_lines = "\n".join(f"- [[{name}]]" for name in sorted(links))
    return f"""---
title: "{title}"
tags:
  - index
---

# {title}

{description}

---

{link_lines}
""".strip()


# -- Main ----------------------------------------------------------------------

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    # Collect character data from the full vault before processing any files
    npc_by_faction, pc_by_faction = collect_characters(VAULT)

    published = 0
    skipped = 0

    published_npcs: list[str] = []
    published_factions: list[str] = []

    for md_file in sorted(VAULT.rglob("*.md")):
        parts = set(md_file.parts)
        if parts & ALWAYS_SKIP_DIRS:
            continue

        try:
            md_file.relative_to(OUT)
            continue
        except ValueError:
            pass

        content = md_file.read_text(encoding="utf-8-sig")

        if not should_publish(content):
            skipped += 1
            continue

        rel = md_file.relative_to(VAULT)
        out_file = OUT / rel
        out_file.parent.mkdir(parents=True, exist_ok=True)

        if is_npc(content):
            processed = process_npc_stub(content)
            published_npcs.append(md_file.stem)
        elif is_faction(content):
            faction_name = md_file.stem
            published_factions.append(faction_name)
            processed = process_faction(content, faction_name,
                                        npc_by_faction, pc_by_faction)
        else:
            processed = process_general(content)

        out_file.write_text(processed, encoding="utf-8")
        published += 1

    # Generate folder index pages for Quartz Explorer navigation
    if published_npcs:
        npc_index_path = OUT / "characters" / "npcs" / "index.md"
        npc_index_path.parent.mkdir(parents=True, exist_ok=True)
        npc_index_path.write_text(
            build_folder_index(
                "Characters",
                "Known individuals in the campaign world.",
                published_npcs,
            ),
            encoding="utf-8",
        )

    if published_factions:
        faction_index_path = OUT / "world" / "factions" / "index.md"
        faction_index_path.parent.mkdir(parents=True, exist_ok=True)
        faction_index_path.write_text(
            build_folder_index(
                "Factions",
                "The factions whose interests shape this campaign.",
                published_factions,
            ),
            encoding="utf-8",
        )

    print(f"Published {published} files | Skipped {skipped} files -> {OUT}/")


if __name__ == "__main__":
    main()
