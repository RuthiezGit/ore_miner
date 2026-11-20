# Ore Miner ⛏️

A Minecraft-inspired arcade game developed entirely in Python using Pygame.

## 1. Game Overview

**Ore Breaker** is a 2D arcade game inspired by the classic Brick Breaker concept and Minecraft's mining mechanics.

The player takes the role of a miner trapped inside a cave. The miner throws a pickaxe upwards to break different types of ores. Each destroyed ore awards points depending on its type.

The miner moves horizontally across the cave to keep the pickaxe bouncing towards the ores. The objective is to destroy all the ores, accumulate the highest possible score and progress through multiple levels. The miner has three lives in each game.

## 2. Game Features

### Mandatory Features

| Feature | Description | Assigned Member |
|---|---|---|
| Brick Layout | Beginner level consisting of a 5 × 8 ore arrangement. | Dimash |
| Multiple Levels | Introduces different ore arrangements and increasing difficulty. | Dimash |
| Paddle Control | Controls the miner's horizontal movement. | Ruth |
| Ball Motion | Handles the pickaxe's movement and trajectory. | Ruth |
| Paddle Collision | Detects collisions between the pickaxe and miner. | Ruth |
| Brick Destruction and Score | Removes destroyed ores and awards points according to ore type. | Yerkhan |
| Lives | Tracks the miner's three lives. | Eren |
| HUD | Displays relevant game information, including score, lives and level. | Eren |
| Time Handling | Manages game timing and movement updates. | Eren |
| Win/Lose Screens | Displays the appropriate screen when the player wins or loses. | Shan |
| Playable and Stable Game | Tests, debugs and ensures the game runs reliably. | Shan |

### Extra Features

| Feature | Description | Assigned Member |
|---|---|---|
| Power-ups | Special items dropped by destroyed ores. | Yerkhan |
| Angle Control | Changes the pickaxe's bouncing direction depending on where it hits the miner. | Yerkhan |
| Multi-hit Bricks | Introduces ores that require multiple hits before destruction. | Dimash |
| Sound Effects and Music | Adds audio feedback and background music. | Shan |
| Progressive Ball Speed | Increases pickaxe speed after a certain number of hits (e.g. every 10 hits). | Ayesha |
| Pause and Resume | Allows players to pause and continue the game. | Ayesha |
| How to Play | Provides instructions explaining the game's controls and objectives. | Ayesha |

## 3. Technologies and Libraries

### Mandatory Installation

**Python**

The programming language used to develop the game.

**Pygame**

The main Python library used for game development. It handles:
- Game window and graphics rendering.
- Keyboard and mouse input.
- Object movement and animation.
- Collision detection.
- Sound effects and music.

Install Pygame:

```bash
pip install pygame
```

### Additional Python Modules

The following modules are part of Python's standard library and do not require separate installation.

| Module | Purpose |
|---|---|
| `math` | Mathematical calculations, including movement and bouncing angles. |
| `random` | Generating random elements and levels. |
| `json` | Storing and exchanging data, including reading external files. |

## 4. Development Tools

**GitHub**

Used for version control, code sharing and collaboration between team members.

**Visual Studio Code (VS Code)**

Recommended code editor for developing the game.

### Recommended VS Code Extensions

| Extension | Purpose |
|---|---|
| Python + Pylance (Microsoft) | Syntax checking, autocomplete, go-to-definition and type hints. |
| GitLens | Tracks code changes, contributors and commits. |
| Live Share (Microsoft) | Allows team members to collaboratively edit and debug code in real time. |

## 5. Installation and Setup

### Prerequisites

- Python installed on your computer.
- Visual Studio Code or another Python-compatible code editor.
- Git installed if you intend to use GitHub for collaboration.

### Getting Started

1. Clone or download the project repository from GitHub.
2. Open the project folder in VS Code.
3. Open the integrated terminal.
4. Install the required Python library:

```bash
pip install pygame
```

5. Run the main Python file:

```bash
python main.py
```

## 6. Project Structure

The project will be organised into separate Python files to keep the code modular and make collaboration easier.

```text
OreBreaker/
│
├── main.py
├── logic.py
├── gui.py
├── levels.py
├── theme.py
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
├── requirements.txt
└── README.md
```

*The final folder structure may change as development progresses.*

## 7. Team Collaboration

Each team member is responsible for their assigned component. All components will eventually be integrated into the main game.

Members are expected to:
- Contribute to the development process.
- Understand the code they implement.
- Test their individual components.
- Communicate with other members to ensure compatibility.
- Participate in debugging and integration.

## 8. Project Requirements

- The game must be developed entirely in Python.
- Pygame must be used as the primary game development library.
- The game must include all mandatory features.
- The game must have multiple playable levels.
- The game must remain stable during gameplay.
- All team members must contribute and understand their implementations.
- The final project must be packaged as a ZIP file named `<team-name>.zip`.
- File paths must be relative and portable so that assets continue to work after the project is moved or extracted from its ZIP archive.

---

**Project:** Ore Miner  
**Language:** Python  
**Game Engine/Library:** Pygame  
**Development Environment:** Visual Studio Code