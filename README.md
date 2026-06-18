# D&D Campaign Vault Template

An Obsidian vault template for running a tabletop RPG campaign with a public player-facing wiki, automated publishing via GitHub Actions, and optional Claude Code AI assistance.

## What This Is

A complete, working starter kit that gives you:

- **Obsidian vault** with a structured folder layout, templates for every content type, and a DM dashboard with one-click file creation
- **Public wiki** built with Quartz v4 and hosted on GitHub Pages -- players get a clean, searchable website; DM-only content is automatically stripped before publishing
- **Automated publishing pipeline** -- every push to your private campaign repo triggers a GitHub Action that filters your notes, builds the site, and deploys it
- **Separation of DM and player content** -- a single `publish: true/false` flag in each file's frontmatter controls what players see

## Quick Start

1. **Fork or clone** this repository to your GitHub account
2. **Open the vault** in Obsidian (File → Open Folder as Vault → select the repo folder)
3. **Install the required plugins** (see [SETUP.md](SETUP.md))
4. **Create a second GitHub repository** for the public wiki (name it `your-campaign-wiki`)
5. **Add a deploy token** to your campaign repo's Actions secrets
6. **Update `scripts/filter_public.py`** with your wiki repo name
7. **Push** -- the wiki builds automatically

Full walkthrough: [SETUP.md](SETUP.md)

## Folder Structure

```
Campaign-Vault-Template/
  Home.md                      <- Campaign home page
  Dashboard.md                 <- DM action dashboard
  _templates/                  <- Templates for all content types
  characters/
    npcs/                      <- One file per NPC
    pcs/                       <- One file per player character
  world/
    factions/                  <- One file per faction
    locations/                 <- One file per location
    history/
    cosmology/
  sessions/                    <- One file per session
  quests/                      <- One file per quest
  tables/                      <- Random tables, encounter tables
  rules/                       <- House rules
  Player Resources/            <- Player-facing pages (publish: true)
  dm/                          <- DM-only documents (never published)
  scripts/
    filter_public.py           <- Wiki publishing filter
  .github/
    workflows/
      publish-wiki.yml         <- GitHub Actions workflow
```

## Required Obsidian Plugins

Install these from Obsidian's Community Plugins settings:

| Plugin | Purpose |
|---|---|
| Dataview | Auto-populates NPC/PC lists on faction pages |
| Templater | Dynamic template insertion |
| Obsidian Git | Commit and push from within Obsidian |
| QuickAdd | One-click file creation from templates |
| Buttons | Dashboard action buttons |
| Advanced Tables | Easier markdown table editing |

## How Publishing Works

1. You write notes in Obsidian and set `publish: true` on files players should see
2. You push to GitHub (Obsidian Git plugin makes this one click)
3. GitHub Actions runs `filter_public.py` -- copies only `publish: true` files, strips all DM-only sections (callouts marked `DM Eyes Only`, secrets, plot hooks, etc.)
4. Quartz v4 builds a static site from the filtered files
5. The site deploys to your public wiki repository on GitHub Pages

Players never see DM notes. You maintain one set of files.

## Customizing for Your Campaign

1. Edit `dm/Campaign Foundation.md` with your plot, antagonist, and act structure
2. Edit `CLAUDE.md` with your campaign name, setting, factions, and NPC roster
3. Replace the example files with your real content
4. Update `Player Resources/Character Creation.md` and `Player Resources/Player Factions.md`
5. Delete `characters/npcs/John Doe.md`, `characters/pcs/Jane Smith.md`, `world/locations/Location A.md`, and `world/factions/Example Faction.md` when you have real content

## Using with Claude Code

This vault is designed to work with [Claude Code](https://claude.ai/code). The `CLAUDE.md` file at the root gives Claude context about your campaign structure, conventions, and content. Update it as your campaign grows.

---

*Template by [your name]. Built on Quartz v4, Obsidian, and GitHub Actions.*
