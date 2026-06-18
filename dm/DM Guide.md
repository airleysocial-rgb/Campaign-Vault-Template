---
title: "DM Guide"
publish: false
---

# DM Guide

Workflow and maintenance reference for running this vault.

---

## Daily Workflow

**Before a session:**
1. Open `dm/DM Session Notes.md` and write the Session N Prep section
2. Review active quest files for threads likely to come up
3. Check NPC files for any characters likely to appear -- refresh yourself on their secrets and motivations

**During a session:**
- Take rough notes in `sessions/Session 0N.md` (fill in properly after)

**After a session:**
1. Fill in the session file completely
2. Update any NPC files touched during play
3. Update quest files -- check off completed objectives, add progress log entries
4. Update `Player Resources/Player Notes - Session Recaps.md` with curated player-facing notes
5. Push to GitHub: `git add [files] && git commit -m "Session N complete" && git push`

---

## Adding New Content

**New NPC:**
- Copy `_templates/NPC Template.md` into `characters/npcs/`
- Name the file `Firstname Lastname.md`
- Set `faction: "[[Exact Faction Filename]]"` -- must match the faction file name exactly
- Set `publish: false` until ready for players to see

**New Location:**
- Copy `_templates/Location Template.md` into `world/locations/`
- Set `publish: false` by default

**New Session:**
- Copy `_templates/Session Template.md` into `sessions/`
- Name it `Session 02.md`, `Session 03.md` etc. (zero-padded)

**New Quest:**
- Copy `_templates/Quest Template.md` into `quests/`

---

## Publishing to the Wiki

### What gets published
Only files with `publish: true` in their frontmatter. The filter script strips:
- All `> [!warning] DM Eyes Only` callout blocks
- Sections titled: Motivations & Goals, Secrets, Connections, Background, Plot Hooks, Encounter Notes, Session Log, DM Notes, D&D Mechanics Notes

### How to publish
Push to the `master` branch. GitHub Actions handles the rest automatically.

```
git add [specific files]
git commit -m "description"
git push
```

### To flip a file to public
Change `publish: false` to `publish: true` in the file's frontmatter, then push.

---

## Obsidian Plugins Reference

| Plugin | What It Does | Settings Location |
|---|---|---|
| Dataview | Auto-populates NPC/PC lists on faction pages | Community Plugins > Dataview |
| Templater | Creates files from templates | Community Plugins > Templater > Template folder = `_templates` |
| Obsidian Git | Commits and pushes from within Obsidian | Community Plugins > Obsidian Git |
| QuickAdd | One-click file creation from templates | Community Plugins > QuickAdd |
| Buttons | Dashboard buttons | Used in Dashboard.md |
| Advanced Tables | Better markdown table editing | Auto-activates in table rows |

---

## Frontmatter Reference

### Required fields by file type

**NPC:**
```yaml
name: "Full Name"
race: ""
gender: ""
age: ""
role: ""
status: alive
location: "[[Location Name]]"
faction: "[[Faction Name]]"
tags:
  - npc
publish: false
```

**Faction:**
```yaml
name: "Faction Name"
type: ""
alignment: ""
status: active
leader: "[[NPC Name]]"
tags:
  - faction
publish: true
```

**Session:**
```yaml
session: 1
date_played: YYYY-MM-DD
pcs_present: []
tags:
  - session
```

---

## Troubleshooting

**Dataview not showing NPCs on faction pages:**
- Check that the NPC's `faction` field is a wiki link: `"[[Exact Faction Name]]"`
- The faction name must match the faction file name exactly (case-sensitive)
- On the public wiki, Dataview is pre-rendered by the filter script -- this is expected behavior

**Wiki not updating after push:**
- Check the Actions tab in your GitHub repo for errors
- Most common cause: malformed YAML frontmatter in a file

**Obsidian Git not pushing:**
- Run `git push` in a terminal from the vault folder to see the raw error
- Usually a GitHub authentication issue
