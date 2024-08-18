
# 🖥️ Simple Keylogger

## 📖 Overview

This project is a simple Python keylogger that logs keyboard inputs to a file named `keylog.txt`. The program captures both alphanumeric and special keys, running continuously in the background until the `Esc` key is pressed.

## 💡 Problem Statement

Create a Python program that logs all keyboard inputs, including special keys, to a text file. The keylogger should run in a separate thread and allow users to stop it by pressing the `Esc` key.

## ✨ Features

- **📝 Logs Alphanumeric Keys**: Captures and logs all alphanumeric keys (letters and numbers).
- **🔑 Special Key Mapping**: Recognizes and logs special keys such as space, enter, shift, ctrl, backspace, and escape.
- **🔄 Continuous Monitoring**: The keylogger runs in a separate thread, continuously monitoring keystrokes.
- **❌ Stop with 'Esc' Key**: Pressing the `Esc` key stops the keylogger.

## 💻 Requirements

- 🐍 Python 3.x
- `pynput` library

## ▶️ How to Run

1. **📥 Clone this repository or download the `simple_keylogger.py` file**.

2. **📦 Install the `pynput` library**:
    ```bash
    pip install pynput
    ```

3. **🏃 Run the Python script**:
    ```bash
    python simple_keylogger.py
    ```

4. **🔍 Monitor the `keylog.txt` file**: Keystrokes will be logged here as they are captured.

5. **❌ Stop the keylogger**: Press the `Esc` key to stop the program.

## 🗺️ Key Mapping

- Space: ` `
- Enter: `\\n`
- Shift: `[Shift]`
- Ctrl: `[Ctrl]`
- Backspace: `[Backspace]`
- Esc: `[Esc]`

Other special keys will be logged with their names in square brackets (e.g., `[Tab]`).

## 👤 Author

- Yatharth Bhavsar


