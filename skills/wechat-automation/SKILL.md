---
name: wechat-automation
description: "Automate WeChat (微信) desktop application on Windows. Open WeChat, search contacts, open chats, send messages, and perform common WeChat actions using PyAutoGUI. Use when: (1) Opening WeChat, (2) Searching for contacts, (3) Opening chat conversations, (4) Sending text messages, (5) Sending WeChat messages to specific contacts."
---

# WeChat Automation

Automate WeChat desktop application on Windows.

## Requirements

```bash
pip install pyautogui pywin32 pygetwindow
```

## Screen Resolution

**Important:** Coordinates are based on 1366x768 resolution. Adjust for your screen.

## Common Coordinates (1366x768)

| Element | Approximate Position |
|---------|---------------------|
| Search box | (200, 80) |
| First chat | (150, 150) |
| Message input | (800, 700) |
| Send button | (1050, 700) |
| Emoji button | (750, 700) |

## Quick Start

### Open WeChat

```python
import subprocess
import time

subprocess.Popen("wechat")
time.sleep(5)  # Wait for WeChat to fully load
```

### Search and Open Contact

```python
import pyautogui
import time

# Click search box
pyautogui.click(200, 80)
time.sleep(0.5)

# Type contact name
pyautogui.typewrite("Contact Name", interval=0.05)
time.sleep(1)

# Press Enter to open chat
pyautogui.keyDown('return')
pyautogui.keyUp('return')
time.sleep(1)
```

### Send Message

```python
# Click message input area
pyautogui.click(800, 700)
time.sleep(0.5)

# Type message
pyautogui.typewrite("Hello! This is a test message.", interval=0.01)
time.sleep(0.5)

# Send (Ctrl+Enter or just Enter depending on settings)
pyautogui.keyDown('return')
pyautogui.keyUp('return')
```

## Full Workflow Example

```python
import subprocess
import pyautogui
import time

def send_wechat_message(contact_name, message):
    """Send a message to a WeChat contact"""
    
    # 1. Open WeChat
    subprocess.Popen("wechat")
    time.sleep(5)
    
    # 2. Click search
    pyautogui.click(200, 80)
    time.sleep(0.5)
    
    # 3. Type contact name
    pyautogui.typewrite(contact_name, interval=0.05)
    time.sleep(1)
    
    # 4. Open chat
    pyautogui.keyDown('return')
    pyautogui.keyUp('return')
    time.sleep(1)
    
    # 5. Click input area
    pyautogui.click(800, 700)
    time.sleep(0.5)
    
    # 6. Type message
    pyautogui.typewrite(message, interval=0.01)
    time.sleep(0.5)
    
    # 7. Send
    pyautogui.keyDown('return')
    pyautogui.keyUp('return')
    
    return f"Message sent to {contact_name}"

# Usage
send_wechat_message("Friend Name", "Hello!")
```

## Finding Coordinates

Run this to find your screen coordinates:

```python
import pyautogui
import time

print("Move mouse to target position...")
time.sleep(3)
x, y = pyautogui.position()
print(f"Position: ({x}, {y})")
```

## Safety Notes

- Always add delays between actions
- WeChat must be logged in
- Window should not be minimized
- Coordinates vary by screen resolution
