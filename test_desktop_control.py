#!/usr/bin/env python3
"""
Desktop Control Test Script
Tests basic PyAutoGUI functionality
"""

import pyautogui
import subprocess
import time

print("=" * 50)
print("Desktop Control Test")
print("=" * 50)

# 1. Screen info
print("\n1. Screen Information:")
print(f"   Screen size: {pyautogui.size()}")
print(f"   Current mouse position: {pyautogui.position()}")

# 2. Test Notepad (safe app to open)
print("\n2. Opening Notepad in 3 seconds...")
time.sleep(3)
subprocess.Popen("notepad")
time.sleep(2)

# 3. Type some text
print("3. Typing test message...")
time.sleep(1)
pyautogui.typewrite("Hello from Claw! Desktop control is working.", interval=0.01)

# 4. Take screenshot
print("4. Taking screenshot...")
time.sleep(1)
screenshot = pyautogui.screenshot()
screenshot.save("desktop_test_screenshot.png")
print("   Screenshot saved: desktop_test_screenshot.png")

print("\n" + "=" * 50)
print("Test completed!")
print("=" * 50)
print("\nYou can now:")
print("- Close Notepad manually")
print("- Check the screenshot file")
print("- Try other commands from the skill documentation")
