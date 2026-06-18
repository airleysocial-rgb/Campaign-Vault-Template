# Setup Guide

Complete walkthrough for getting this vault running with a public wiki.

**Time required:** 30-60 minutes
**Cost:** Free (GitHub Pages, Obsidian, and Quartz are all free)

---

## Prerequisites

Install these before starting:

- [Obsidian](https://obsidian.md) -- the note-taking app that runs this vault
- [Git](https://git-scm.com/downloads) -- version control; required for Obsidian Git plugin
- [Python 3.x](https://www.python.org/downloads/) -- required to run the publishing filter locally (optional but recommended for testing)
- A [GitHub account](https://github.com) -- free tier is sufficient

---

## Step 1 -- Fork and Clone the Template

1. On GitHub, click **Fork** on this repository
2. Name your fork something like `My-Campaign` (this will be your **private** campaign notes repo)
3. Clone it to your computer:

```
git clone https://github.com/YOUR-USERNAME/My-Campaign.git
```

---

## Step 2 -- Open the Vault in Obsidian

1. Open Obsidian
2. Click **Open folder as vault**
3. Select the cloned folder (`My-Campaign/`)
4. Obsidian will open the vault -- you may see a warning about community plugins; click **Trust author and enable plugins** if prompted (or enable them manually in the next step)

---

## Step 3 -- Install Community Plugins

In Obsidian: **Settings → Community plugins → Turn on community plugins → Browse**

Install and enable each of these:

| Plugin | Search for |
|---|---|
| **Dataview** | `Dataview` |
| **Templater** | `Templater` |
| **Obsidian Git** | `Obsidian Git` |
| **QuickAdd** | `QuickAdd` |
| **Buttons** | `Buttons` |
| **Advanced Tables** | `Advanced Tables` |

After installing, go to **Settings → Templater** and set the template folder to `_templates`.

---

## Step 4 -- Configure Obsidian Git

1. In Obsidian: **Settings → Obsidian Git**
2. Set **Auto pull interval** to your preference (10-15 minutes is reasonable)
3. Set **Auto push** to on if you want automatic syncing
4. The plugin uses your system Git credentials -- if you have not authenticated GitHub on your machine, follow [GitHub's credential setup guide](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)

---

## Step 5 -- Create the Public Wiki Repository

This is a second, separate GitHub repository that will host your public wiki.

1. Go to [github.com/new](https://github.com/new)
2. Name it `My-Campaign-wiki` (must match what you'll put in Step 7)
3. Set visibility to **Public** (GitHub Pages requires public for free accounts)
4. Check **Add a README file**
5. Click **Create repository**

---

## Step 6 -- Create a Deploy Token

The GitHub Action needs permission to push files from your private campaign repo to your public wiki repo.

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Name it `Campaign Wiki Deploy`
4. Select scope: **repo** (full repo access)
5. Click **Generate token**
6. Copy the token -- you will not see it again

Now add it to your campaign repo:

1. Go to your **campaign repo** on GitHub (not the wiki repo)
2. **Settings → Secrets and variables → Actions → New repository secret**
3. Name: `WIKI_DEPLOY_TOKEN`
4. Value: paste the token
5. Click **Add secret**

---

## Step 7 -- Configure the Publishing Script

Open `scripts/filter_public.py` in a text editor and update the two values at the top of the file:

```python
GITHUB_USERNAME = "your-github-username"
WIKI_REPO_NAME = "My-Campaign-wiki"
```

Save the file and commit the change.

---

## Step 8 -- Enable GitHub Pages on the Wiki Repo

After your first successful Action run (which happens on your first push), enable GitHub Pages:

1. Go to your **wiki repo** on GitHub
2. **Settings → Pages**
3. Source: **Deploy from a branch**
4. Branch: `gh-pages` / `/ (root)`
5. Click **Save**

Your wiki will be live at `https://YOUR-USERNAME.github.io/My-Campaign-wiki/`

---

## Step 9 -- Test the Pipeline

1. Make any small change in Obsidian (edit `Home.md`, for example)
2. Push via Obsidian Git (**Ctrl+P → Obsidian Git: Commit all changes and push**)
3. Go to your campaign repo on GitHub → **Actions** tab
4. Watch the workflow run -- it should complete in about 2 minutes
5. Check `https://YOUR-USERNAME.github.io/My-Campaign-wiki/` -- it should be live

If the Action fails, check the error in the Actions tab. Common issues are listed at the bottom of this guide.

---

## Step 10 -- Customize Your Campaign

Now that the pipeline is working, replace the example content with your own:

1. **Edit `dm/Campaign Foundation.md`** -- add your plot, antagonist, factions, and act structure
2. **Edit `CLAUDE.md`** -- update with your campaign name, setting, factions, and NPC roster (this file guides Claude Code if you use it)
3. **Edit `Player Resources/Character Creation.md`** -- your system, rules, and options
4. **Edit `Player Resources/Player Factions.md`** -- your playable factions
5. **Edit `rules/House Rules.md`** -- your table rules
6. **Delete the example files:**
   - `characters/npcs/John Doe.md`
   - `characters/pcs/Jane Smith.md`
   - `world/locations/Location A.md`
   - `world/factions/Example Faction.md`
   - `quests/Example Quest.md`

---

## What Gets Published vs. What Stays Private

Every file has a `publish` field in its frontmatter:

```yaml
publish: true    # appears on the public wiki (DM content stripped)
publish: false   # DM only -- never published
```

**The filter automatically strips these sections from published files:**
- Any section containing `DM Eyes Only` callout blocks
- Sections titled: Motivations & Goals, Secrets, Connections, Background, Plot Hooks, Encounter Notes, Session Log, DM Notes, D&D Mechanics Notes

**Default:** set `publish: false` on all new NPCs and most world content. Only flip to `true` when you are ready for players to see it.

---

## Using with Claude Code (Optional)

[Claude Code](https://claude.ai/code) can act as a DM assistant -- creating NPC files, building quest structures, writing session notes, and maintaining consistency across documents.

1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Run `claude` from inside your campaign folder
3. Claude reads `CLAUDE.md` for context about your campaign -- keep it updated

---

## Troubleshooting

**Action fails with "Permission denied" on wiki push**
- Check that `WIKI_DEPLOY_TOKEN` is set correctly in your campaign repo secrets
- Make sure the token has `repo` scope and has not expired

**Quartz build fails**
- Check the Actions log for the specific error
- Usually a malformed frontmatter in one of your files -- YAML is indent-sensitive

**Obsidian Git not pushing**
- Run `git push` manually in a terminal from your vault folder to see the raw error
- Usually a credential issue -- re-authenticate GitHub

**filter_public.py encoding error**
- The script uses `encoding="utf-8-sig"` to handle files edited in Obsidian or PowerShell
- Do not change this to `"utf-8"` -- it will break files with a BOM

**Dataview blocks showing as code on the wiki**
- This is expected and handled automatically -- the filter pre-renders Dataview queries into static markdown tables before Quartz builds the site

---

## File Encoding Note

If you edit files with PowerShell, they may be saved with a UTF-8 BOM. The publishing script handles this automatically. Do not change `encoding="utf-8-sig"` to `"utf-8"` in `filter_public.py`.
