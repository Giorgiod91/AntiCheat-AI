# AntiCheat AI - Demo-based Anti-Cheat Detection System

## Overview

**AntiCheat AI** is a machine learning-powered anti-cheat detection system that analyzes in-game demo files to detect suspicious player behaviors. By comparing player actions to professional-level gameplay, the system flags anomalies that could indicate cheating, such as aimbots, wallhacks, and other unfair advantages.

This project aims to provide a new, behavior-driven layer of anti-cheat protection to complement traditional methods, leveraging **demo file analysis** and **machine learning** to identify cheaters in online multiplayer games.

## Features

- **Machine Learning-Based Detection**: Analyzes player behavior, particularly reaction time, by comparing it to the reaction times of the top professional players.
- **Detects Unusual Reaction Time**: Flags players whose reaction times are significantly faster or slower than the average of top-tier professional players, as this can indicate cheating (e.g., aimbots or other assistance tools).
- **Demo File Analysis**: Extracts detailed player actions and game events from demo files to evaluate reaction times and detect potential cheaters.
- **Pro Player Benchmarking**: Uses the best professional players' benchmarks to define what is "normal" for reaction times in specific game scenarios.


## More Features coming

- **Detects Suspicious Corner-Checking**: Uses machine learning to analyze corner-checking behavior, comparing it to how professional players approach corners and angles. Players who display abnormal pre-aiming or predictive behavior at corners may be flagged for potential wallhack usage.

## Technologies Used

- **Python**: Primary language for data parsing and machine learning model training.
- **Pandas**: Used for data manipulation and analysis of demo events.
- **Scikit-learn**: Machine learning library for training detection models.
- **NumPy**: Used for numerical computations on game data.
- **Matplotlib/Seaborn**: Visualization tools for data analysis.
- **DemoParser**: A custom Python module for parsing demo files and extracting relevant player data.

## How It Works

1. **Data Extraction**: The system reads demo files from games (e.g., Counter-Strike 2) and extracts player actions, team names, weapon choices, and more.
   
2. **Behavioral Analysis**: The system compares these actions against a dataset of professional player demos. This dataset acts as a benchmark for normal behavior in the game.
   
3. **Anomaly Detection**: Using machine learning algorithms, the system identifies patterns of play that differ significantly from the norm (e.g., extreme accuracy, improbable kills, strange movement).
   
4. **Flagging Cheating**: If a player's behavior is too far outside normal patterns, they are flagged for potential cheating.
