# Desktop Control Skill

**Source:** Custom skill created for OpenClaw  
**Purpose:** GUI automation for Windows desktop

## What It Does

Allows OpenClaw to:
- ✅ Open applications (微信, Chrome, Notepad, etc.)
- ✅ Click on screen coordinates
- ✅ Type text into input fields
- ✅ Take screenshots
- ✅ Send keyboard shortcuts
- ✅ Automate repetitive UI tasks

## How It Works

Uses **Python PyAutoGUI** library:
- `pyautogui.click(x, y)` — Click at coordinates
- `pyautogui.typewrite(text)` — Type text
- `pyautogui.screenshot()` — Capture screen
- `pyautogui.keyDown/Up()` — Send hotkeys
- `subprocess.Popen()` — Launch applications

## Installation

```bash
# Required packages
pip install pyautogui pywin32 pillow pygetwindow psutil

# Windows only - disable failsafe (optional)
# Add to script: pyautogui.FAILSAFE = False
```

## Usage Examples

### Open WeChat
```python
import subprocess
subprocess.Popen("wechat")
```

### Click at Position
```python
import pyautogui
pyautogui.click(500, 300)  # x, y coordinates
```

### Type Text
```python
pyautogui.typewrite("Hello", interval=0.05)
```

### Take Screenshot
```python
pyautogui.screenshot("screen.png")
```

## Safety Considerations

⚠️ **Important:**
- Always ask user confirmation before actions
- Never automate password entry
- Screenshot before/after major changes
- Respect user's active window

## Limitations

- Cannot "see" UI elements (blind coordinates)
- Screen resolution dependent
- Requires focus (actions go to active window)
- Cannot bypass system security dialogs

## Full Documentation

See `README.md` for complete API reference and examples.
