---
name: desktop-control
description: "Control Windows desktop via GUI automation using Python PyAutoGUI. Open applications, click UI elements, type text, take screenshots, and automate repetitive desktop tasks. Use when: (1) Opening apps like WeChat, Chrome, VSCode, (2) Clicking buttons or UI elements, (3) Typing into forms or search boxes, (4) Taking screenshots, (5) Sending keyboard shortcuts, (6) Any task requiring desktop GUI interaction."
---

# Desktop Control

Automate Windows desktop GUI using PyAutoGUI.

## Requirements

```bash
pip install pyautogui pywin32 pillow pygetwindow psutil
```

## Safety First

⚠️ **Always confirm with user before:**
- Deleting files or closing applications
- Typing sensitive information
- Making system-wide changes

## Quick Start

### Open Application

```python
import subprocess
subprocess.Popen("wechat")  # or chrome, notepad, etc.
```

### Click at Position

```python
import pyautogui
pyautogui.click(500, 300)  # x, y coordinates
```

### Type Text

```python
pyautogui.typewrite("Hello World", interval=0.05)
```

### Keyboard Shortcut

```python
pyautogui.keyDown('alt')
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')
```

### Screenshot

```python
pyautogui.screenshot("capture.png")
```

## Common Patterns

See `README.md` for complete API documentation.

## Helper Script

Use the bundled script for simple operations:

```bash
python desktop_control.py open wechat
python desktop_control.py click 500 300
python desktop_control.py type "Hello"
python desktop_control.py screenshot
```

## Notes

- Add delays (`time.sleep()`) between actions
- Use `pyautogui.position()` to find coordinates
- Coordinates are screen-resolution dependent
- Requires focus (actions affect active window)
