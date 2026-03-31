<p align="center">
  <img src="images/Image1.png" width="800">
</p>

# 🎮 Mini Game Hub

A modular, command-line driven mini game platform built using **Bash** and **Python (Pygame)**.  
This project demonstrates clean system design, user authentication, and interactive gameplay in a structured and scalable way.

---

## 🚀 Overview

<table align="center">
<tr>
<td align="center">🎯</td>
<td><b>Purpose</b></td>
<td>Lightweight gaming platform with structured architecture</td>
</tr>

<tr>
<td align="center">👥</td>
<td><b>Users</b></td>
<td>Two-player authentication before gameplay</td>
</tr>

<tr>
<td align="center">🧠</td>
<td><b>Concept</b></td>
<td>Separation of concerns for clarity & maintainability</td>
</tr>

<tr>
<td align="center">⚙️</td>
<td><b>System Design</b></td>
<td>Modular + scalable structure</td>
</tr>
</table>

---

<p align="center">
  <img src="images/Private GIF.gif" width="800">
</p>

## ✨ Features

<table align="center">
<tr>
<th>🎮 Feature</th>
<th>💡 Description</th>
<th>🖼️ Visual</th>
</tr>

<tr>
<td>🔐 Authentication</td>
<td>Login / Signup system with secure access</td>
<td><img src="images/auth.png" width="120"></td>
</tr>

<tr>
<td>🔑 SHA-256 Security</td>
<td>Passwords hashed (no plaintext storage)</td>
<td><img src="images/security.png" width="120"></td>
</tr>

<tr>
<td>👥 Two Players</td>
<td>Both users must login before game starts</td>
<td><img src="images/users.png" width="120"></td>
</tr>

<tr>
<td>🧩 Modular Design</td>
<td>Separate files for logic, auth & game</td>
<td><img src="images/modules.png" width="120"></td>
</tr>

<tr>
<td>🎮 Game Engine</td>
<td>Pygame-based interactive UI</td>
<td><img src="images/game.png" width="120"></td>
</tr>

<tr>
<td>🔁 Control Flow</td>
<td>Validation loops + error handling</td>
<td><img src="images/flow.png" width="120"></td>
</tr>

</table>

---

## 🛠️ Tech Stack

<table align="center">
<tr>
<th>⚙️ Technology</th>
<th>💻 Role</th>
<th>🖼️ Visual</th>
</tr>

<tr>
<td>🐚 Bash</td>
<td>User interaction & control flow</td>
<td><img src="images/bash.png" width="100"></td>
</tr>

<tr>
<td>🐍 Python</td>
<td>Core logic & authentication</td>
<td><img src="images/python.png" width="100"></td>
</tr>

<tr>
<td>🎮 Pygame</td>
<td>Game engine & UI rendering</td>
<td><img src="images/pygame.png" width="100"></td>
</tr>

</table>

---

## 📁 Project Structure

<table align="center">
<tr>
<th>📂 File</th>
<th>📌 Purpose</th>
<th>🖼️</th>
</tr>

<tr>
<td><code>main.sh</code></td>
<td>Entry point (handles user flow)</td>
<td>🚀</td>
</tr>

<tr>
<td><code>auth.py</code></td>
<td>Login/signup + hashing</td>
<td>🔐</td>
</tr>

<tr>
<td><code>game.py</code></td>
<td>Pygame engine</td>
<td>🎮</td>
</tr>

<tr>
<td><code>users.tsv</code></td>
<td>User database</td>
<td>📄</td>
</tr>

<tr>
<td><code>README.md</code></td>
<td>Documentation</td>
<td>📘</td>
</tr>

</table>

---

## ▶️ How to Run

<table align="center">
<tr>
<th>⚡ Step</th>
<th>💻 Command</th>
<th>🖼️</th>
</tr>

<tr>
<td>1️⃣ Clone Repo</td>
<td><code>git clone https://github.com/pravarkumar/mini-game-hub.git</code></td>
<td>📥</td>
</tr>

<tr>
<td>2️⃣ Enter Folder</td>
<td><code>cd Mini-Game-Hub</code></td>
<td>📂</td>
</tr>

<tr>
<td>3️⃣ Make Executable</td>
<td><code>chmod +x main.sh</code></td>
<td>⚙️</td>
</tr>

<tr>
<td>4️⃣ Run Project</td>
<td><code>bash main.sh</code></td>
<td>🚀</td>
</tr>

</table>

---

## 🔐 Authentication Flow

<table align="center">
<tr>
<th>🔢 Step</th>
<th>📝 Action</th>
<th>🖼️</th>
</tr>

<tr>
<td>1️⃣</td>
<td>User selects login/signup</td>
<td>👆</td>
</tr>

<tr>
<td>2️⃣</td>
<td>Enter username & password</td>
<td>⌨️</td>
</tr>

<tr>
<td>3️⃣</td>
<td>Password hashed (SHA-256)</td>
<td>🔒</td>
</tr>

<tr>
<td>4️⃣</td>
<td>Checked against <code>users.tsv</code></td>
<td>📄</td>
</tr>

<tr>
<td>5️⃣</td>
<td>Valid → Access granted</td>
<td>✅</td>
</tr>

<tr>
<td>6️⃣</td>
<td>Invalid → Retry loop</td>
<td>🔁</td>
</tr>

</table>

---

## 🎮 Game Flow

<table align="center">
<tr>
<th>🎯 Step</th>
<th>⚡ Action</th>
<th>🖼️</th>
</tr>

<tr>
<td>1️⃣</td>
<td>Player 1 authentication</td>
<td>👤</td>
</tr>

<tr>
<td>2️⃣</td>
<td>Player 2 authentication</td>
<td>👤</td>
</tr>

<tr>
<td>3️⃣</td>
<td>Launch <code>game.py</code></td>
<td>🚀</td>
</tr>

<tr>
<td>4️⃣</td>
<td>Gameplay via Pygame window</td>
<td>🎮</td>
</tr>

</table>

---

## 🔮 Improvements with time

<table align="center">
<tr>
<th>🚀 Feature</th>
<th>💡 Idea</th>
<th>🖼️</th>
</tr>

<tr>
<td>🏆 Leaderboard</td>
<td>Track scores & rankings</td>
<td>🥇</td>
</tr>

<tr>
<td>🎲 More Games</td>
<td>Add TicTacToe, Snake, etc.</td>
<td>🎯</td>
</tr>

<tr>
<td>🎨 UI Upgrade</td>
<td>Better visuals & animations</td>
<td>✨</td>
</tr>

<tr>
<td>🔒 Security+</td>
<td>Salting & encryption</td>
<td>🛡️</td>
</tr>

<tr>
<td>🌐 Multiplayer</td>
<td>Online gameplay support</td>
<td>🌍</td>
</tr>

</table>

---

## 💡 Design Philosophy

<table align="center">
<tr>
<td>🧠</td>
<td>Separation of concerns</td>
</tr>

<tr>
<td>📖</td>
<td>Clean & readable code</td>
</tr>

<tr>
<td>⚙️</td>
<td>Right tool for the right job</td>
</tr>

<tr>
<td>🎮</td>
<td>Fun & smooth gameplay</td>
</tr>

<tr>
<td>🧩</td>
<td>Expandable architecture</td>
</tr>

</table>

---

## 📌 Author

<table align="center">
<tr>
<td>👨‍💻</td>
<td><b>Pravar Kumar</b></td>
</tr>

<tr>
<td>👨‍💻</td>
<td><b>Shantanu Patil</b></td>
</tr>
</table>

---

## ⭐ Final Note

<table align="center">
<tr>
<td>🎯</td>
<td>This project showcases <b>system design + security + modular programming</b></td>
</tr>

<tr>
<td>🎮</td>
<td>A fun escape from everyday boredom</td>
</tr>

<tr>
<td>💙</td>
<td>Built with passion & creativity</td>
</tr>
</table>

<p align="center">
✨ <b>Enjoy the game & happy coding!</b> ✨
</p>
