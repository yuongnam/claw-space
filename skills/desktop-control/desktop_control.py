#!/usr/bin/env python3
"""
Desktop Control Helper Script
Basic automation for opening apps and GUI interactions
"""

import sys
import time
import subprocess

def show_usage():
    print("""
Desktop Control Helper

Usage:
  python desktop_control.py open <app_name>     - Open application
  python desktop_control.py click <x> <y>         - Click at coordinates
  python desktop_control.py type <text>          - Type text
  python desktop_control.py screenshot [file]    - Take screenshot
  python desktop_control.py position             - Show mouse position
  python desktop_control.py run <command>        - Run shell command

Examples:
  python desktop_control.py open wechat
  python desktop_control.py open chrome
  python desktop_control.py click 500 300
  python desktop_control.py type "Hello World"
  python desktop_control.py screenshot myscreen.png
""")

def open_app(app_name):
    """Open application"""
    app_map = {
        'wechat': 'wechat',
        'chrome': 'chrome',
        'edge': 'msedge',
        'notepad': 'notepad',
        'calc': 'calc',
        'explorer': 'explorer',
    }
    
    app = app_map.get(app_name.lower(), app_name)
    
    try:
        if sys.platform == 'win32':
            subprocess.Popen(app, shell=True)
        else:
            subprocess.Popen([app])
        print(f"✓ Opened: {app}")
        time.sleep(2)  # Give app time to launch
    except Exception as e:
        print(f"✗ Failed to open {app}: {e}")

def main():
    if len(sys.argv) < 2:
        show_usage()
        return
    
    command = sys.argv[1]
    
    if command == 'open' and len(sys.argv) >= 3:
        open_app(sys.argv[2])
    
    elif command == 'position':
        print("Move mouse to desired position...")
        time.sleep(3)
        print(f"Now implement pyautogui to capture position")
    
    elif command == 'run' and len(sys.argv) >= 3:
        cmd = ' '.join(sys.argv[2:])
        subprocess.run(cmd, shell=True)
    
    else:
        show_usage()

if __name__ == '__main__':
    main()
