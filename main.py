import keyboard
SCAN_CODE_P = 34

def replace_p(event):
    if event.event_type == "down":
        keyboard.send("backspace")
        keyboard.write("П")
        return False 

keyboard.hook(lambda e: replace_p(e) if e.scan_code == SCAN_CODE_P else None)

keyboard.wait()
