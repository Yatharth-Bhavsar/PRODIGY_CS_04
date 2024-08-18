
# Simple Keylogger

This is a simple keylogger implemented in Python using the `pynput` library. It listens for keyboard events and logs the keystrokes to a file named `keylog.txt`.

## Features

- Logs all alphanumeric keys and special keys (space, enter, shift, etc.)
- Runs in a separate thread for continuous monitoring
- Stops logging when the `Esc` key is pressed

## Prerequisites

- Python 3.x
- `pynput` library (can be installed via pip)

## Installation

1. Clone the repository or download the `simple_keylogger.py` file.
2. Install the `pynput` library if you haven't already:

    ```bash
    pip install pynput
    ```

## Usage

1. Run the keylogger script:

    ```bash
    python simple_keylogger.py
    ```

2. The keylogger will start, and keystrokes will be logged to `keylog.txt`.

3. Press the `Esc` key to stop the keylogger.

## Key Mapping

Special keys are logged as follows:

- Space: ` `
- Enter: `\n`
- Shift: `[Shift]`
- Ctrl: `[Ctrl]`
- Backspace: `[Backspace]`
- Esc: `[Esc]`

Other special keys will be logged with their names in square brackets (e.g., `[Tab]`).

