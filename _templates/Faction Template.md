---
name: "Faction Name"
type: ""
alignment: ""
status: active
headquarters: "[[]]"
leader: "[[]]"
tags:
  - faction
---

# Faction Name

> *What people say about them on the street.*

## At a Glance

| Field | Detail |
|---|---|
| **Type** | |
| **Alignment** | |
| **Status** | active |
| **Headquarters** | |
| **Leader** | |
| **Public Goal** | |
| **Hidden Goal** | |

---

## Description

*How they came to be and why they matter.*

---

## Leader

**[[Leader Name]]** — *Title / Role*

*Brief note on the leader's style and how they run the faction.*

---

## Members

### Player Characters

```dataview
TABLE player, race, class, level
FROM #pc
WHERE faction = this.file.link
SORT level DESC
```

### Key NPCs

```dataview
TABLE race, role, status, location
FROM #npc
WHERE faction = this.file.link
SORT status ASC
```

---

## Key Associations

| Faction | Relationship |
|---|---|
| [[]] | |

---

## Recommended Races

*For player characters joining this faction.*

- 

## Recommended Classes

- 

> [!important] Class Restrictions
> *Note any class restrictions here, or remove this callout if none.*

---

## Obligations

> [!warning] Sworn Duties
> - 

---

## Resources & Assets

- **Military:** 
- **Wealth:** 
- **Magic:** 
- **Information:** 

---

## Agenda & Plans

### Current Objective
- 

### Long-Term Plan
- 

---

## How They View the Party

*Neutral / Friendly / Hostile — and why.*

---

## DM Notes

> [!warning] DM Eyes Only
> *Hidden plans, secret members, things that will change.*
