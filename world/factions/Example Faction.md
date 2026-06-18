---
name: "Example Faction"
type: "[Faction type -- e.g. Mortal, Fae, Religious, Criminal]"
alignment: "Lawful Neutral"
status: active
leader: "[[John Doe]]"
hq: "[[Location A]]"
tags:
  - faction
publish: true
---

# Example Faction

> *"Example faction motto or quote."*

## Overview

*Two to three sentences describing what this faction is, what it wants, and why it matters in the campaign.*

---

## At a Glance

| Field | Detail |
|---|---|
| **Type** | [Faction type] |
| **Alignment** | Lawful Neutral |
| **Status** | Active |
| **Leader** | [[John Doe]] |
| **Headquarters** | [[Location A]] |

---

## What They Want

*What is this faction's stated goal? What is their actual goal -- are those the same thing?*

---

## How They Operate

*How does this faction pursue its goals? What are their methods, resources, and constraints?*

---

## Relationship to Other Factions

| Faction | Relationship |
|---|---|
| *Other Faction* | *Describe the relationship* |

---

## Key NPCs

```dataview
TABLE race as Race, role as Role, status as Status, location as Location
FROM #npc
WHERE faction = [[Example Faction]]
SORT file.name ASC
```

---

## Player Characters

```dataview
TABLE player as Player, race as Race, class as Class, level as Level
FROM #pc
WHERE faction = [[Example Faction]]
SORT level DESC
```

---

## DM Notes

> [!warning] DM Eyes Only
> - *What does this faction know that the party doesn't?*
> - *What is the faction's hidden agenda, if any?*
> - *What would it take to turn this faction against the party?*
