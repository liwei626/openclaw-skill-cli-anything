#!/usr/bin/env python3
"""
CLI-Anything Harness Example
Demonstrates basic automation patterns for GUI applications
"""

import argparse
import subprocess
import time
import sys
from pathlib import Path

# Optional dependencies - install if needed
# pip install pynput pyautogui

def launch_app(app_name: str, wait_time: float = 3.0) -> subprocess.Popen:
    """Launch a GUI application and return the process handle."""
    print(f"Launching {app_name}...")
    proc = subprocess.Popen([app_name])
    time.sleep(wait_time)
    return proc

def send_keys(keys: str, interval: float = 0.01):
    """Send keyboard input using pynput."""
    try:
        from pynput.keyboard import Controller
        keyboard = Controller()
        keyboard.type(keys, interval=interval)
    except ImportError:
        print("Warning: pynput not installed. Skipping key input.")
        print(f"Would type: {keys}")

def press_hotkey(*keys):
    """Press a hotkey combination."""
    try:
        import pyautogui
        pyautogui.hotkey(*keys)
    except ImportError:
        print(f"Warning: pyautogui not installed. Would press: {keys}")

def capture_screen(region: tuple = None) -> str:
    """Capture screen and return image path."""
    try:
        import pyautogui
        screenshot = pyautogui.screenshot(region=region)
        path = "/tmp/screenshot.png"
        screenshot.save(path)
        return path
    except ImportError:
        print("Warning: pyautogui not installed.")
        return None

def main():
    parser = argparse.ArgumentParser(
        description='Example CLI-Anything Harness',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --app notepad --type "Hello World"
  %(prog)s --app calc --wait 5
        """
    )
    
    parser.add_argument('--app', required=True, help='Application to launch')
    parser.add_argument('--type', help='Text to type')
    parser.add_argument('--wait', type=float, default=5.0, help='Wait time after launch')
    parser.add_argument('--hotkey', nargs='+', help='Hotkey to press (e.g., ctrl s)')
    
    args = parser.parse_args()
    
    # Launch application
    proc = None
    try:
        proc = launch_app(args.app, wait_time=args.wait)
        
        # Type text if provided
        if args.type:
            print(f"Typing: {args.type}")
            send_keys(args.type)
            time.sleep(0.5)
        
        # Press hotkey if provided
        if args.hotkey:
            print(f"Pressing hotkey: {'+'.join(args.hotkey)}")
            press_hotkey(*args.hotkey)
        
        # Keep running until user interrupts
        print("\nApplication running. Press Ctrl+C to exit.")
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        if proc:
            print("Terminating application...")
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
        print("Done.")

if __name__ == '__main__':
    main()
