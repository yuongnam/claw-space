---
name: desktop-control
description: "Control Windows desktop via automation. Open applications, click UI elements, type text, take screenshots, and perform GUI interactions using Python PyAutoGUI. Use when: opening apps like WeChat/Chrome/VSCode, clicking buttons, typing into forms, taking screenshots, automating repetitive UI tasks, or any task requiring desktop GUI interaction."
---

# Desktop Control Skill

Control Windows desktop through GUI automation using PyAutoGUI.

## Capabilities

- **Open applications** — Launch programs by name or path
- **Click UI elements** — Buttons, menus, coordinates
- **Type text** — Input fields, search boxes, chat messages
- **Take screenshots** — Capture screen or specific regions
- **Keyboard shortcuts** — Send key combinations
- **Wait for elements** — Pause for UI to load

## Requirements

```bash
pip install pyautogui pywin32 pillow
```

## Safety Rules

⚠️ **Critical safety requirements:**

1. **Always confirm** before any destructive action (deleting files, closing apps)
2. **Never automate** password entry or sensitive credentials
3. **Pause for user confirmation** when switching contexts
4. **Screenshot before** and **after** major changes
5. **Respect active window** — check what's currently focused

## Core Functions

### 1. Open Application

```python
import subprocess
import time

def open_app(app_name_or_path):
    """Open application by name or full path"""
    try:
        subprocess.Popen(app_name_or_path)
        time.sleep(2)  # Wait for app to launch
        return f"Opened: {app_name_or_path}"
    except Exception as e:
        return f"Failed to open {app_name_or_path}: {e}"

# Examples
open_app("wechat")           # Open WeChat
open_app("chrome")           # Open Chrome
open_app("notepad")          # Open Notepad
open_app(r"C:\Path\App.exe")  # Open by full path
```

### 2. Click at Coordinates

```python
import pyautogui
import time

def click_at(x, y, clicks=1, button='left'):
    """Click at screen coordinates"""
    pyautogui.click(x, y, clicks=clicks, button=button)

def click_on(image_path, confidence=0.9):
    """Click on image match (requires screenshot)"""
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
            return f"Clicked on {image_path}"
        return f"Image {image_path} not found"
    except Exception as e:
        return f"Error: {e}"

# Get current mouse position
x, y = pyautogui.position()
print(f"Mouse at: ({x}, {y})")
```

### 3. Type Text

```python
def type_text(text, interval=0.05):
    """Type text with optional delay between characters"""
    pyautogui.typewrite(text, interval=interval)

def type_and_submit(text):
    """Type text and press Enter"""
    pyautogui.typewrite(text)
    pyautogui.keyDown('return')
    pyautogui.keyUp('return')

# Examples
type_text("Hello World")
type_and_submit("Search query")
```

### 4. Keyboard Shortcuts

```python
def send_hotkey(*keys):
    """Send keyboard shortcuts"""
    pyautogui.keyDown(*keys)
    pyautogui.keyUp(*keys)

# Common shortcuts
send_hotkey('alt', 'tab')        # Switch window
send_hotkey('win')               # Open Start menu
send_hotkey('win', 'r')          # Open Run dialog
send_hotkey('ctrl', 'c')         # Copy
send_hotkey('ctrl', 'v')         # Paste
send_hotkey('alt', 'f4')         # Close window
send_hotkey('win', 'd')          # Show desktop
```

### 5. Take Screenshot

```python
def screenshot(filename="screenshot.png", region=None):
    """
    Take screenshot
    region = (left, top, width, height) for partial capture
    """
    if region:
        img = pyautogui.screenshot(region=region)
    else:
        img = pyautogui.screenshot()
    img.save(filename)
    return f"Screenshot saved: {filename}"

# Full screen
screenshot()

# Specific region
screenshot("wechat_chat.png", region=(100, 100, 400, 600))
```

### 6. Find and Click Image

```python
def find_and_click(image_path, confidence=0.8, timeout=10):
    """Find image on screen and click it"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                return f"Found and clicked {image_path}"
        except:
            pass
        time.sleep(0.5)
    return f"Could not find {image_path}"
```

## Common Tasks

### Open WeChat and Send Message

```python
import pyautogui
import subprocess
import time

# 1. Open WeChat
subprocess.Popen("wechat")
time.sleep(3)  # Wait for launch

# 2. Click search box (adjust coordinates for your screen)
pyautogui.click(200, 100)
time.sleep(0.5)

# 3. Type contact name
pyautogui.typewrite("Contact Name")
time.sleep(1)

# 4. Press Enter to open chat
pyautogui.keyDown('return')
pyautogui.keyUp('return')
time.sleep(1)

# 5. Type message
pyautogui.typewrite("Hello! This is automated.")
time.sleep(0.5)

# 6. Send (Ctrl+Enter)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('return')
pyautogui.keyUp('return')
pyautogui.keyUp('ctrl')
```

### Open Chrome and Search

```python
import subprocess
import pyautogui
import time

# Open Chrome
subprocess.Popen("chrome")
time.sleep(3)

# Click address bar (usually at top)
pyautogui.click(500, 50)
time.sleep(0.5)

# Type URL or search
pyautogui.typewrite("github.com")
time.sleep(0.5)

# Press Enter
pyautogui.keyDown('return')
pyautogui.keyUp('return')
```

### Take Screenshot of Specific Window

```python
import pyautogui
import time

def capture_window(window_title_contains):
    """Screenshot window by title (requires pygetwindow)"""
    import pygetwindow as gw
    
    windows = gw.getWindowsWithTitle(window_title_contains)
    if windows:
        win = windows[0]
        win.activate()
        time.sleep(0.5)
        screenshot = pyautogui.screenshot(region=(win.left, win.top, win.width, win.height))
        screenshot.save(f"{window_title_contains}_screenshot.png")
        return f"Captured {window_title_contains}"
    return f"Window not found: {window_title_contains}"
```

## Screen Coordinates Helper

```python
def get_mouse_position():
    """Get current mouse position - use this to find coordinates"""
    print("Move mouse to target position...")
    time.sleep(3)
    x, y = pyautogui.position()
    print(f"Position: ({x}, {y})")
    return x, y

# Run this to find where to click
get_mouse_position()
```

## Best Practices

### 1. Always Add Delays

GUI actions need time:
```python
time.sleep(2)  # After opening app
time.sleep(0.5)  # Between clicks
time.sleep(1)  # After typing
```

### 2. Handle Resolution Differences

Different screens have different coordinates. Use relative positions or image matching.

### 3. Check if Element Exists

```python
if pyautogui.locateOnScreen("button.png"):
    pyautogui.click("button.png")
else:
    print("Button not found")
```

### 4. Fail Gracefully

```python
try:
    pyautogui.click(100, 100)
except Exception as e:
    print(f"Click failed: {e}")
```

## Windows-Specific Tips

### Launch Programs

```python
# Via Start menu search
pyautogui.keyDown('win')
pyautogui.keyUp('win')
time.sleep(0.5)
pyautogui.typewrite("wechat")
time.sleep(0.5)
pyautogui.keyDown('return')
pyautogui.keyUp('return')
```

### Focus Window

```python
import pygetwindow as gw

# Bring window to front
window = gw.getWindowsWithTitle("WeChat")[0]
window.activate()
```

### Check if Running

```python
import psutil

def is_running(process_name):
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

is_running("wechat")  # Check if WeChat is running
```

## Limitations

- **Cannot see UI** — Only works with coordinates or image matching
- **Screen dependent** — Coordinates vary by resolution
- **Window focus** — Actions go to active window
- **Security prompts** — Cannot bypass UAC or system dialogs
- **Speed** — Too fast = missed clicks; too slow = user frustration

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Clicks not working | Add delays between actions |
| Wrong position | Use `pyautogui.position()` to find correct coords |
| Image not found | Lower confidence threshold, check screenshot |
| Permission denied | Run as administrator |
| Window not activating | Use `pygetwindow` to properly focus |
