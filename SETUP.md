# Setup Guide — Complete Beginner's Walkthrough

This guide assumes you have never used any of these tools before. Every step is explained from scratch.

**Total time:** 60-90 minutes for a first-time setup.
**Cost:** Everything in this guide is free.

---

## What You Are Building

Before touching anything, here is the big picture of what this system does:

```
Your Notes (Private)              Public Website (Players See This)
+----------------------+          +---------------------------+
| Obsidian on your PC  |  Push    | GitHub automatically      |
| - DM notes (hidden)  | -------> | strips DM content and     |
| - Player content     |          | builds a website          |
| - Session notes      |          | your players can visit    |
+----------------------+          +---------------------------+
```

You write everything in one place. A robot (GitHub Actions) automatically separates what players should see from what they should not, and publishes it as a website.

---

## The Tools — What Each One Is

Before installing anything, here is what each tool does and why you need it:

### Obsidian
A free note-taking app that works with plain text files. It runs on your computer (not in a browser). Think of it as a very smart notebook that understands links between pages, shows you a map of how your notes connect, and has a huge library of add-ons. This is where you write all your campaign notes.

### Git
A system that tracks every change you make to your files, like "track changes" in Word but for entire folders. It saves a history of every version of every file. You need it so Obsidian can send your notes to GitHub automatically.

### GitHub
A website where you store your files and their history. Think of it like Google Drive, but built for developers. You will have two locations on GitHub:
- A **private** repository (your full campaign notes, DM content included — only you can see it)
- A **public** repository (the filtered, player-facing wiki website)

### GitHub Actions
An automated robot that lives on GitHub. Every time you save new notes to GitHub, it automatically runs the filter script, builds the website, and publishes it. You set it up once and never think about it again.

### Python
A programming language. The filter script (`filter_public.py`) is written in Python. GitHub's robot runs it automatically in the cloud, so you do not technically need Python on your own computer — but installing it lets you test the filter locally if something goes wrong.

---

## Part 1 — Create a GitHub Account

GitHub is where your campaign notes will be stored and where the website will be published.

1. Open a web browser and go to **github.com**
2. Click the green **Sign up** button in the top right
3. Enter your email address and click **Continue**
4. Create a password and click **Continue**
5. Choose a username — this will appear in your wiki URL, so pick something reasonable (e.g., `dmstephen` or your name). Click **Continue**
6. Complete the verification puzzle
7. Click **Create account**
8. GitHub will send a verification email — open it and click the confirmation link
9. When asked what you want to use GitHub for, you can skip the survey (click the link at the bottom that says "Skip personalization")

You now have a GitHub account. Keep the browser tab open — you will come back to it.

---

## Part 2 — Install Git

Git is the behind-the-scenes tool that lets Obsidian talk to GitHub. You install it once and then mostly forget it exists.

### On Windows

1. Go to **git-scm.com/download/win**
2. The download should start automatically. If not, click **Click here to download**
3. Open the downloaded file (it will be named something like `Git-2.xx.x-64-bit.exe`)
4. A setup wizard opens. Click **Next** on every screen — the default options are all correct
5. On the screen that says "Choosing the default editor used by Git," change the dropdown to **Notepad** (easier for beginners than the default)
6. Keep clicking **Next** until you reach **Install**, then click **Install**
7. When it finishes, click **Finish** (uncheck "View Release Notes" if you like)

### On Mac

1. Go to **git-scm.com/download/mac**
2. The page recommends installing via Homebrew. If you do not have Homebrew, follow the link to **brew.sh** first and install it (paste the command shown into your Terminal app)
3. Once Homebrew is installed, open Terminal (press **Command + Space**, type "Terminal", press Enter)
4. Type this command and press Enter: `brew install git`
5. Wait for it to finish — this takes a few minutes

**How to check Git installed correctly:**
- Windows: Click Start, type "Command Prompt," open it, type `git --version`, press Enter. You should see something like `git version 2.45.0`
- Mac: Open Terminal, type `git --version`, press Enter. Same result.

If you see a version number, Git is installed. If you see an error, try restarting your computer and trying again.

---

## Part 3 — Install Obsidian

Obsidian is the app where you write your campaign notes.

1. Go to **obsidian.md**
2. Click the **Download** button
3. Choose the version for your operating system (Windows or Mac)
4. Open the downloaded file and follow the installer
   - Windows: Run the `.exe` file, click through the prompts
   - Mac: Open the `.dmg` file, drag Obsidian to your Applications folder
5. Launch Obsidian

When Obsidian opens for the first time, it asks how you want to start. Choose **Open folder as vault** — but do not click it yet. You need to get the template files first (Step 5 below). For now, you can click **Create new vault** just to get Obsidian open, then close it after you see the main interface.

---

## Part 4 — Fork This Template to Your GitHub Account

"Forking" means making your own copy of this template on GitHub. This is how you get all the files.

1. Make sure you are signed in to GitHub (from Part 1)
2. Go to this template's page on GitHub (the URL of this repository)
3. Click the **Fork** button near the top right of the page
4. A screen appears asking where to fork it. Your username should already be selected. Under **Repository name**, change it to the name of your campaign — for example, `My-Campaign` or `DragonCampaign2024`
5. Leave everything else as default and click **Create fork**
6. GitHub will take a few seconds to create your copy. When it is done, you will be looking at your own version of the repository

**What just happened:** You now have your own copy of all these files on GitHub, under your account.

---

## Part 5 — Copy Your Campaign Files to Your Computer

Now you need to get those files from GitHub onto your computer so Obsidian can use them.

### On Windows

1. Click the green **Code** button on your GitHub repository page
2. Click **Download ZIP**
3. Open your Downloads folder and find the ZIP file
4. Right-click the ZIP file and choose **Extract All**
5. Choose where to extract it — somewhere easy to find, like your Documents folder. Click **Extract**
6. You will get a folder named something like `My-Campaign-main` — rename it to just `My-Campaign`

### On Mac

Same steps as Windows. Right-click the ZIP and choose "Open With > Archive Utility."

> **Note for later:** Downloading as a ZIP works to get started, but eventually you will want to use the Obsidian Git plugin to keep your files synced. The plugin handles this for you automatically once set up. See Part 9 for that step.

---

## Part 6 — Open the Vault in Obsidian

1. Open Obsidian
2. Click **Open folder as vault**
3. Navigate to the folder you just extracted (e.g., `My-Campaign`) and click **Open** (or **Select Folder** on Mac)
4. Obsidian will open your vault. You will probably see a warning that says "This vault has community plugins that need to be enabled" — click **Trust author and enable plugins** if that option appears, or ignore it for now (you will enable them in the next step)

You should now see your campaign files listed on the left side of Obsidian. If you see `Home.md`, `CLAUDE.md`, folders like `characters/` and `dm/`, you are in the right place.

---

## Part 7 — Install Community Plugins

Obsidian has a library of free add-ons called "community plugins." Think of them like apps for your phone — Obsidian works without them, but these specific ones make the campaign vault system work.

**What a plugin is:** A small piece of software someone built that adds new features to Obsidian. They are free, open source, and reviewed by Obsidian's team before appearing in the library.

### How to get to Community Plugins

1. In Obsidian, click the **gear icon** in the bottom left corner to open Settings
2. In the Settings panel, scroll down the left column and click **Community plugins**
3. If you see a button that says **Turn on community plugins**, click it and confirm

### Installing each required plugin

For each plugin in the list below, do the following:

1. Click **Browse** (the button near the top of the Community plugins page)
2. In the search box, type the plugin name exactly as shown below
3. Click on the plugin when it appears in the results
4. Click **Install**
5. After installation, click **Enable**
6. Click the back arrow to return and search for the next one

**Required plugins:**

| Plugin Name | What It Does |
|---|---|
| **Dataview** | Automatically lists NPCs on faction pages |
| **Templater** | Creates new files from your templates with one click |
| **Obsidian Git** | Sends your notes to GitHub automatically |
| **QuickAdd** | Adds buttons for creating new NPCs, sessions, quests, etc. |
| **Buttons** | Powers the dashboard buttons |
| **Advanced Tables** | Makes editing tables much easier |

### After installing all plugins

One extra step for Templater:

1. In Settings, scroll down the left column until you see **Templater** (under Community plugins)
2. Click on **Templater**
3. Find the field that says **Template folder location**
4. Type `_templates` in that field
5. Close Settings

---

## Part 8 — Create the Public Wiki Repository

You need a second GitHub repository — this one will host the public website your players visit. It is separate from your private campaign notes.

1. Go to **github.com** and make sure you are signed in
2. Click the **+** icon near the top right corner, then click **New repository**
3. Under **Repository name**, type your campaign name followed by `-wiki` — for example, `My-Campaign-wiki`
4. Under visibility, select **Public** (required for free GitHub Pages hosting)
5. Check the box that says **Add a README file**
6. Click **Create repository**

You now have two repositories:
- `My-Campaign` — private, your full notes
- `My-Campaign-wiki` — public, the player-facing website (currently empty)

---

## Part 9 — Connect Obsidian to GitHub (Obsidian Git Setup)

This step connects your vault to GitHub so the Obsidian Git plugin can send your notes to GitHub automatically.

This step requires the command line. Do not panic — you only need to do this once.

### What is the command line?

It is a text-based way of talking to your computer. Instead of clicking buttons, you type instructions. On Windows it is called Command Prompt or PowerShell. On Mac it is called Terminal.

### Setting up Git credentials

Before Obsidian Git can connect to GitHub, you need to tell Git your GitHub username and email. This is a one-time setup.

**On Windows:**
1. Click Start and search for **PowerShell**, then open it
2. Type the following two commands, pressing Enter after each. Replace the example values with your own GitHub username and the email you used to sign up:

```
git config --global user.name "YourGitHubUsername"
git config --global user.email "youremail@example.com"
```

**On Mac:**
1. Open Terminal (Command + Space, type Terminal, press Enter)
2. Type the same two commands above and press Enter after each

### Linking your vault to GitHub

1. On your GitHub repository page for `My-Campaign`, click the green **Code** button
2. Make sure **HTTPS** is selected (not SSH)
3. Copy the URL shown (it will look like `https://github.com/YourUsername/My-Campaign.git`)

Now, in your command line (PowerShell or Terminal):

4. Navigate to your vault folder. Type this command, replacing the path with where your vault actually is, and press Enter:
   - Windows: `cd "C:\Users\YourName\Documents\My-Campaign"`
   - Mac: `cd "/Users/YourName/Documents/My-Campaign"`

5. Type this command and press Enter (replace the URL with your actual URL from step 3):
```
git remote add origin https://github.com/YourUsername/My-Campaign.git
```

6. Type this command and press Enter:
```
git branch -M master
```

7. Type this command and press Enter:
```
git push -u origin master
```

8. GitHub will ask for your username and password. For the password, use a **Personal Access Token**, not your GitHub password — see the next section.

### Creating a Personal Access Token for Git

GitHub no longer accepts your account password for Git commands. You need a token instead.

1. Go to **github.com/settings/tokens**
2. Click **Generate new token** then **Generate new token (classic)**
3. Under **Note**, type `Obsidian Git Access`
4. Under **Expiration**, choose **No expiration** (or set a date you will remember)
5. Check the box next to **repo** (this gives access to your repositories)
6. Scroll to the bottom and click **Generate token**
7. Copy the token immediately — GitHub will only show it once. Paste it somewhere safe (like a note on your computer) before leaving this page

When Git asks for your password, paste this token instead. On Windows, you may be asked to save it — say yes.

---

## Part 10 — Set Up the Automatic Publishing (Deploy Token)

The robot (GitHub Actions) needs permission to move content from your private campaign repo to your public wiki repo. You give it that permission using a deploy token.

### Create the deploy token

1. Go to **github.com/settings/tokens** again
2. Click **Generate new token** then **Generate new token (classic)**
3. Under **Note**, type `Campaign Wiki Deploy`
4. Under **Expiration**, choose **No expiration**
5. Check the box next to **repo** (full repository access)
6. Click **Generate token**
7. Copy the token immediately

### Add the token to your campaign repository

1. Go to your **campaign repository** on GitHub (the private `My-Campaign` one)
2. Click the **Settings** tab at the top of the repository page
3. In the left column, click **Secrets and variables**, then click **Actions**
4. Click the green **New repository secret** button
5. In the **Name** field, type exactly: `WIKI_DEPLOY_TOKEN`
6. In the **Secret** field, paste the token you just copied
7. Click **Add secret**

---

## Part 11 — Update the Workflow File with Your Details

The workflow file is the instructions GitHub's robot follows. It needs to know your specific repository name.

1. In Obsidian, look at the left panel (your file list) and open the folder `.github` then `workflows`
2. Click on `publish-wiki.yml` to open it
3. Find this line near the bottom of the file:
   ```
   external_repository: YOUR-USERNAME/your-campaign-wiki
   ```
4. Replace `YOUR-USERNAME` with your actual GitHub username and `your-campaign-wiki` with the name of your public wiki repository. For example:
   ```
   external_repository: dmstephen/My-Campaign-wiki
   ```
5. A few lines above that, find:
   ```
   pageTitle: "My Campaign Wiki"
   ```
6. Replace `My Campaign Wiki` with the actual name of your campaign

Save the file (Ctrl+S on Windows, Command+S on Mac).

---

## Part 12 — Push Your Changes and Watch the Robot Work

Now you trigger the pipeline for the first time.

### Using Obsidian Git to push

1. In Obsidian, press **Ctrl+P** (Windows) or **Command+P** (Mac) to open the command palette
2. Type `git` and you will see a list of Git commands
3. Click **Obsidian Git: Commit all changes**
4. When it asks for a commit message, type something like `Initial setup` and press Enter
5. Press **Ctrl+P** again, type `git`, and this time click **Obsidian Git: Push**

### Watch it work

1. Go to your campaign repository on GitHub
2. Click the **Actions** tab at the top
3. You should see a workflow running — there will be a yellow spinning circle next to it
4. Click on the workflow to see it running in detail
5. It takes about 2-3 minutes to complete
6. When the circle turns green, the workflow succeeded

If the circle turns red, click on it to see the error message. Common errors are listed at the bottom of this guide.

---

## Part 13 — Enable GitHub Pages on the Wiki Repository

After the first successful workflow run, you need to turn on the website hosting.

1. Go to your **wiki repository** on GitHub (`My-Campaign-wiki`)
2. Click the **Settings** tab
3. In the left column, click **Pages**
4. Under **Source**, click the dropdown and select **Deploy from a branch**
5. Under **Branch**, click the dropdown and select **gh-pages**
6. Leave the folder set to **/ (root)**
7. Click **Save**

After a minute or two, GitHub Pages will publish your site. You will see a green box at the top of the Pages settings page with a URL like:

```
https://YourUsername.github.io/My-Campaign-wiki/
```

Click that link. Your campaign wiki is live.

---

## Part 14 — Customize for Your Campaign

Now you replace the example content with your real campaign.

### The order to do this

1. **Edit `dm/Campaign Foundation.md`** — write your plot, antagonist, and act structure here first. This is your private master reference.

2. **Edit `CLAUDE.md`** — update the campaign name, setting, faction list, and NPC roster. This file helps Claude Code understand your campaign if you use AI assistance.

3. **Replace the example files with your real content:**
   - `world/factions/Example Faction.md` → copy this file and rename it to your actual faction
   - `characters/npcs/John Doe.md` → copy the NPC template and rename to your first NPC
   - `world/locations/Location A.md` → copy and rename for your first location

4. **Update player-facing pages:**
   - `Player Resources/Character Creation.md` — your system and rules
   - `Player Resources/Player Factions.md` — your actual factions
   - `rules/House Rules.md` — your table rules

5. **Set up your player notes form** — see `Player Resources/Session Notes Form.md` for instructions on creating a Google Form and adding the link.

6. **Delete the placeholder files** once you have real content to replace them:
   - `characters/npcs/John Doe.md`
   - `characters/pcs/Jane Smith.md`
   - `world/locations/Location A.md`
   - `world/factions/Example Faction.md`
   - `quests/Example Quest.md`

### The publish flag

Every file has a line in its header (frontmatter) that looks like this:

```
publish: true
```
or
```
publish: false
```

- `publish: true` means players can see this on the wiki
- `publish: false` means it stays private

By default, everything is `publish: false`. When you are ready for players to see something — a faction page, a character, a location — change that line to `publish: true` and push. The website updates automatically.

---

## Your Ongoing Workflow

Once setup is done, your session-to-session workflow is:

1. **Write notes** in Obsidian as normal
2. **Push to GitHub** with Obsidian Git (Ctrl+P → Commit → Ctrl+P → Push)
3. **Website updates automatically** within 2-3 minutes

That is it. You only had to do all the setup steps once.

---

## Troubleshooting

### The GitHub Action failed (red circle)

Click on the red circle to see the error. The most common causes:

**"Permission denied to wiki repo"**
- Your deploy token is wrong or was not saved correctly
- Go to your campaign repo → Settings → Secrets and variables → Actions
- Check that `WIKI_DEPLOY_TOKEN` is listed there
- If in doubt, delete it and create a new token, then re-add it

**"Quartz build error"**
- Usually a formatting error in one of your files
- Look for the specific file name mentioned in the error
- The most common cause is broken YAML frontmatter (the section between `---` marks at the top of a file) — check for missing quotes, incorrect indentation, or special characters

**"File not found" errors**
- A wiki link `[[File Name]]` points to a file that does not exist yet
- Either create the file or remove the link

### Obsidian Git says "Authentication failed"

- Your Personal Access Token may have expired or been entered incorrectly
- Go to github.com/settings/tokens and create a new one
- When Git asks for a password next time, use the new token

### The website updated but I cannot see the change

- Browser caching: try opening the page in a private/incognito window, or press Ctrl+Shift+R (Windows) / Command+Shift+R (Mac) to force a refresh
- The change may still be deploying: wait 2-3 minutes after the Action completes

### Obsidian is showing code blocks on faction pages instead of NPC lists

- This is the Dataview plugin showing raw code because Dataview is not running in the browser
- On the actual wiki website, the filter script pre-renders these into tables — it will look correct on the public site
- To see the live tables inside Obsidian, make sure the Dataview plugin is enabled

### I do not see my vault files in Obsidian

- Close Obsidian, then reopen it
- Click **Open folder as vault** and navigate back to your campaign folder
- If the left panel is empty, try clicking the folder icon at the top left

---

## Glossary

**Branch** — A version of your files. `master` is your main version. You will not need to create other branches.

**Commit** — Saving a snapshot of your files with a short description of what changed. Like hitting "Save" but with a note attached.

**Deploy** — Putting files somewhere for others to access. "Deploying to GitHub Pages" means publishing your wiki to the web.

**Fork** — Making your own copy of someone else's GitHub repository, while keeping a connection to the original.

**Frontmatter** — The block of information at the very top of each Markdown file, between the two `---` lines. This is where the `publish: true/false` flag lives.

**GitHub Actions** — GitHub's automated robot system. It runs scripts automatically when you push changes.

**GitHub Pages** — GitHub's free website hosting service. Your public wiki runs on this.

**Markdown** — A simple way of formatting text using symbols. `**bold**` becomes **bold**, `# Heading` becomes a large heading. Obsidian uses Markdown for all files.

**Plugin** — An optional add-on that extends what an app can do. Obsidian's community plugins are free and created by volunteers.

**Push** — Sending your local commits from your computer up to GitHub.

**Repository (Repo)** — A project folder stored on GitHub, including all of its files and their complete history.

**Token** — A long string of random characters that acts as a password for automated tools. More secure than a regular password because you can set exactly what it has access to.

**Vault** — What Obsidian calls a folder of notes. When you open a folder as a vault, Obsidian treats everything inside it as your notes.
