# AntiCheat AI - Demo-based Anti-Cheat Detection System

## 🌱 Overview

**AntiCheat AI** is a personal project that leverages **machine learning** to detect suspicious behaviors in online multiplayer games. By analyzing **in-game demo files**, the system compares player actions to professional-level gameplay and flags anomalies that could indicate cheating, such as the use of **aimbots**, **wallhacks**, and more.

This project serves as a stepping stone in my journey into **AI** and **software development**. As I plan to dive deeper into Artificial Intelligence, this project is a practical application of what I've learned so far, and my goal is to continue building on it and eventually apply it to more complex use cases in the future.

---

## 🧠 Features

### ⏱️ **Unusual Reaction Time Detection**  
The system analyzes player reaction times, comparing them with professional-level benchmarks. Fast or unusually slow reactions could indicate the use of cheats like **aimbots**, flagging players as potential cheaters based on outlier performances.

### 🎮 **Demo File Analysis**  
The system extracts critical data from **game demo files**, such as **player actions**, **team information**, **kills**, **weapon choices**, and other **game events**. This data is then used to assess the player’s behavior.

### 🏆 **Pro Player Benchmarking**  
The behavior of professional players serves as a benchmark, allowing the system to understand what "normal" behavior looks like. This helps identify players who deviate significantly from these norms and may be cheating.

---

## 🚧 More Features Coming Soon

### 👀 **Suspicious Corner-Checking Behavior**  
One of the future features will focus on detecting **corner-checking behavior**. By analyzing how players approach corners and angles in the game, we can identify unusual movements that may be indicative of cheats like **wallhacks**.

---

## 🔧 Technologies Used

- **Python**: The primary language for implementing this project, as it’s widely used in data analysis and machine learning.
- **Pandas**: For data manipulation and extracting valuable player stats from demo files.
- **Scikit-learn**: Used for machine learning models to detect cheating patterns.
- **NumPy**: For efficient numerical data handling.
- **Matplotlib/Seaborn**: For data visualization and trend analysis.
- **DemoParser**: For parsing demo files and extracting data for analysis.

---

## 🚀 How It Works

1. **Data Extraction**  
   First, the system processes **demo files** from games like **Counter-Strike 2**, extracting important player information like **kills**, **weapon choices**, and **team information**.

2. **Behavioral Analysis**  
   Once the data is extracted, it’s compared to **professional player benchmarks** to determine what normal player behavior looks like. The system looks for anomalies in **reaction times**, **aiming accuracy**, and **movement patterns**.

3. **Anomaly Detection**  
   Using machine learning algorithms, the system searches for unusual patterns in player behavior, such as excessive accuracy or abnormal movement that doesn’t match the professional benchmark.

4. **Flagging Potential Cheating**  
   If the system detects behavior that significantly deviates from professional standards, the player is flagged as a potential cheater.

---

## 💡 Thought Process and Decision-Making

In building this project, I applied machine learning concepts from Andrew Ng’s **Machine Learning** course, specifically around **binary classification**, data transformation, and feature engineering. Here are some key decisions I made during the project:

- **Why Binary Classification?**  
  The problem of detecting cheating is inherently binary: a player is either cheating or they are not. This makes **binary classification** the ideal approach for this project. I trained the model to classify players as either “cheating” or “not cheating,” based on the analysis of their in-game behavior.

- **Why Neural Networks?**  
  After experimenting with simpler machine learning models, I decided to use a **neural network** to identify complex patterns in player behavior. Neural networks excel at recognizing these intricate patterns, especially when the data is high-dimensional, like in-game behavior data.

- **Data Preprocessing**  
  Extracting and preprocessing data from game demo files was one of the more challenging aspects. Using a parser, I extracted relevant features like aiming behavior and player movement data. A significant step was transforming aiming data (pitch and yaw angles) into **3D vectors** to capture the spatial relationship between the player’s viewpoint and the environment. This was a technique I learned in Andrew Ng's course, and it greatly improved the quality of my model's predictions.

---

## 🔬 Machine Learning Techniques Applied

- **Feature Engineering**: I transformed **raw gameplay data** into usable features for training, such as reaction time, accuracy, and movement patterns.
- **Neural Networks**: I chose a neural network for this binary classification task, as it allows the model to recognize complex, non-linear patterns in the data.
- **Data Analysis**: The process of analyzing the data and creating meaningful features has been one of the most valuable learning experiences for me. It has taught me how to clean and prepare raw data for machine learning applications.
- **Supervised Learning**: This project utilizes **supervised learning**, where labeled data is used to train the model to predict whether a player is cheating or not based on their behavior.

---

## 💬 How You Can Contribute

As this is a personal project, I’m still refining and learning along the way. However, if you’d like to get involved, here’s how you can contribute:

1. **Fork the Repo**  
   Feel free to fork the repo and experiment with the code. You can try improving the model or adding new features.

2. **Submit Pull Requests**  
   If you have any ideas for improving the project or fixing bugs, submit a pull request. I’m always open to suggestions.

3. **Report Issues**  
   If you find any bugs or glitches, don’t hesitate to open an issue. Your feedback is always appreciated.

I’m excited to continue improving this project and would love to hear from others interested in AI, machine learning, and game development!

---
