# AntiCheat AI - Demo-based Anti-Cheat Detection System

## 🌱 Overview

**AntiCheat AI** is a personal project where I'm experimenting with **machine learning** to detect suspicious behavior in online multiplayer games. By analyzing **in-game demo files**, the system compares player actions to professional-level gameplay and flags anomalies that could indicate cheating. This includes detecting behaviors like **aimbots**, **wallhacks**, and more.

This project is a stepping stone in my journey to explore AI and **computer science**, as I plan to study Artificial Intelligence further. The goal is to build a better understanding of AI techniques, and apply them to something fun and practical like online game security.

---

## 🧠 Features

### ⏱️ **Unusual Reaction Time Detection**  
By analyzing player reaction times, I compare them to the reaction times of professional players. If a player's reaction is too fast (or unusually slow), it may indicate the use of cheats like **aimbots**. This allows the system to flag potential cheaters based on an outlier performance.

### 🎮 **Demo File Analysis**  
The system extracts **player actions**, **team info**, and **game events** from demo files to assess players' behaviors, especially focusing on timing, accuracy, and movements.

### 🏆 **Pro Player Benchmarking**  
Professional player data is used as a benchmark to understand what "normal" reaction times and behaviors look like in various scenarios. This helps establish what's considered fair play, and detects players who fall far outside these norms.

---

## 🚧 More Features Coming Soon

### 👀 **Suspicious Corner-Checking Behavior**  
One of the future plans for this project is to implement **corner-checking** detection. This uses machine learning to compare how players approach corners and angles in the game. Professional players have a specific way of checking corners, and players who display predictive aiming or suspicious movements might be flagged for using **wallhacks**.

---

## 🔧 Technologies Used

- **Python**: The primary language for this project, as I learn how to use Python for data analysis and machine learning.
- **Pandas**: Helps me manipulate the demo data and extract useful player stats.
- **Scikit-learn**: The library I’m using to experiment with machine learning techniques to detect patterns.
- **NumPy**: For efficient handling of numerical data.
- **Matplotlib/Seaborn**: Used for visualizing the data and analyzing trends.
- **DemoParser**: Awpy to analyse data
---



## Machine Learning Techniques Applied
- In building this project, I applied concepts from Andrew Ng’s Machine Learning course, particularly on data transformation and feature engineering. For example, I transformed pitch and yaw data into 3D vectors, which are then used as features for training machine learning models to detect cheating


#trying out to use heatmaps
![image](https://github.com/user-attachments/assets/0fce2978-5bb0-43d9-9b77-f2d8accecff9)




## 🚀 How It Works

1. **Data Extraction**  
   First, the system reads **demo files** from the game (such as **Counter-Strike 2**) and extracts important details like **player actions**, **team names**, **kills**, **weapon choices**, and **game events**.

2. **Behavioral Analysis**  
   It then compares the extracted player actions to those of **professional players**, using their gameplay as a benchmark to understand what's normal and what's not.

3. **Anomaly Detection**  
   Using basic machine learning techniques, the system tries to find outliers in player behavior — for example, players who are **too accurate**, have **extreme reaction times**, or show **strange movement patterns**.

4. **Flagging Potential Cheating**  
   If a player's actions don’t match up with what is expected from top players, they are flagged for possible cheating.

---

## 💡 How You Can Contribute

Since this is a personal project, I’m still figuring things out. But if you want to get involved or offer advice, I’d love to hear from you! You can help by:

1. Forking the repo
2. Submitting pull requests if you have ideas or improvements
3. Reporting any bugs or suggesting features to improve the system

Feel free to dive into the code and suggest changes. This is all part of my learning journey, and any help is greatly appreciated!

---
