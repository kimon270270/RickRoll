# 🐱 Rickroll Payload Delivery Simulation (Python, Steganography, Tkinter)

This is a fun and educational cybersecurity project I built to explore how attackers might deliver hidden scripts using **steganography** and **basic social engineering** techniques — all in a safe, controlled, and harmless way.

The goal? To prank users with a classic Rickroll — but with a twist: the prank script is hidden inside an image file.

> ⚠️ **Disclaimer**: This project is for educational purposes only. It does not cause harm, delete files, or collect data. Please do not use it maliciously or without consent.

---

## 📦 What the Project Does

- A Python GUI app built with `Tkinter` opens a simple window with a “Continue” button.
- On click, the app downloads two images from my GitHub — one of them contains a hidden Python script.
- The hidden script is extracted using the `stepic` library (steganography) and saved as `script.py`.
- That script opens the Rick Astley video in the default browser **every 3 seconds, up to 10 times**.
- If either `script.py` or the stego image is deleted, the script stops early.

---

## 🎯 Purpose

This project was inspired by a YouTube short about using images as passwords, which led me to study steganography. I wanted to:
- Simulate how payloads are delivered and triggered in real-world scenarios.
- Practice safe offensive techniques in a red-team-like setup.
- Learn more about how GUIs can be used to influence user behavior.

---

## 🛠️ Tech Stack / Tools Used

- Python 3
- `Tkinter` – for the GUI interface
- `stepic` – to hide and extract the script from the image
- `webbrowser` – to trigger the Rickroll
- `requests` – to download image files from GitHub

---

## 🧠 What I Learned

- How steganography can be used to conceal scripts
- Basics of GUI-based social engineering
- How loops and file existence checks can be used for controlled execution
- The importance of responsible design and ethical use in cybersecurity projects

---

## 🔍 How to Run It

1. Clone this repo:
    ```bash
    git clone https://github.com/kimon270270/RickRoll.git
    cd RickRoll
    ```

2. Install dependencies:
    ```bash
    pip install stepic pillow
    ```

3. Run the GUI app:
    ```bash
    python tinker.py
    ```

4. After clicking "Continue", the app will download the image with the hidden script and run it.

---

## 💡 Notes

- This project is **not malware**. It does not damage or modify any system files.
- The Rickroll loop runs a maximum of 10 times.
- All components were tested in a local environment.

---

## 🙌 Feedback & Sharing

If you’ve built something similar or have ideas for improvement, I’d love to hear from you!  
Feel free to fork this project, try it out, and share your own spin on it.


---

## 🔗 GitHub Repo

[https://github.com/kimon270270/RickRoll](https://github.com/kimon270270/RickRoll)

