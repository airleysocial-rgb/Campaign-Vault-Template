# Claude Code -- Campaign Vault Context

## What This Is

An Obsidian vault for a tabletop RPG campaign managed via Claude Code. All campaign documents are written in Markdown with YAML frontmatter, structured for Obsidian, and published as a public player-facing wiki via GitHub Pages.

**Vault location:** `[UPDATE: path to your vault]`

---

## Campaign Overview

**Name:** [Your Campaign Name]
**Setting:** [Setting description]
**Start Level:** [Level]
**System:** D&D 5e / 5.5e (2024) [or your system]
**Premise:** [One paragraph describing the campaign premise]

---

## Vault Folder Structure

```
Campaign-Vault/
  Home.md
  Dashboard.md
  _templates/
    NPC Template.md
    PC Template.md
    Location Template.md
    Session Template.md
    Faction Template.md
    Quest Template.md
  characters/
    npcs/
    pcs/
  world/
    factions/
    locations/
    history/
    cosmology/
  sessions/
  quests/
  tables/
  rules/
  Player Resources/
  dm/
  scripts/
    filter_public.py
```

---

## Conventions -- Follow These Exactly

### Frontmatter Tags

Every file must have the correct tag for Dataview queries to work:

| File Type | Required Tag | Key Frontmatter Fields |
|---|---|---|
| NPC | `- npc` | `faction: "[[Faction Name]]"`, `role`, `race`, `status`, `location` |
| PC | `- pc` | `faction: "[[Faction Name]]"`, `player`, `race`, `class`, `level` |
| Faction | `- faction` | `name`, `type`, `alignment`, `status`, `leader` |
| Location | `- location` | `name`, `type`, `region`, `status` |
| Session | `- session` | `session`, `date_played`, `pcs_present` |
| Quest | `- quest` | `name`, `type`, `status`, `giver` |

### Faction Links

The `faction` field in NPC and PC frontmatter **must** be a wiki link to the exact faction filename:

```yaml
faction: "[[The Faction Name]]"
```

### Publish Flag -- Wiki Visibility

Every file outside `dm/`, `sessions/`, `quests/`, `tables/`, `scripts/`, or `_templates/` must have a `publish` field:

```yaml
publish: true    # file appears on public wiki (filtered)
publish: false   # DM only -- never published
```

**Default to `publish: false` for all new NPCs and most world content.**

### NPC Secrets

Always use the DM-only callout for secrets:

```markdown
> [!warning] DM Eyes Only
> - Secret content here
```

### File Naming

- NPCs and PCs: `Firstname Lastname.md`
- Factions: `The Faction Name.md`
- Sessions: `Session 01.md`, `Session 02.md` (zero-padded)
- Locations: descriptive name, e.g., `City Name -- The Venue.md`

### Gender and Pronouns

[Your convention here]

---

## Writing and Output Conventions

- **No em-dashes (--)** anywhere in prose output -- use `--` instead
- **No read-aloud text or dialogue suggestions** in session files
- **Session structure:** brief bullet-point beats and DM reference notes; not prose scenes

---

## Combat Design Standards

- **Party level:** [Level]
- **Party size:** [Expected size]
- **Always include a harder difficulty variant** for every combat encounter

---

## Factions

| File | Type | Notes |
|---|---|---|
| `Example Faction.md` | [Type] | Replace with your factions |

---

## NPCs

| File | Faction | Role |
|---|---|---|
| `John Doe.md` | Example Faction | Example NPC -- replace with real content |

---

## Dataview Dependency

Faction pages use Dataview plugin queries to auto-populate NPC and PC lists. **Dataview must be installed** in Obsidian (Community Plugins > Dataview).

---

## GitHub Repository

**URL:** [Your repo URL]
**Visibility:** Private
**Remote:** `origin` -- HTTPS
**Default branch:** `master`

### Commit workflow

```
git add [specific files]
git commit -m "description of changes"
git push
```

Always use specific file paths rather than `git add .`.

## Publishing Pipeline

| Step | Status |
|---|---|
| Git + GitHub private repo | [Done / Pending] |
| GitHub Actions workflow | [Done / Pending] |
| Python filter script | [Done / Pending] |
| Quartz v4 static site | [Done / Pending] |
| Public wiki repo + GitHub Pages | [Done / Pending] |

**Public wiki URL:** [Your wiki URL once live]

**filter_public.py encoding note:** The script reads files with `encoding="utf-8-sig"` to handle UTF-8 BOM from files edited in Obsidian or PowerShell. Do not change this to `"utf-8"` or publishing will break.
