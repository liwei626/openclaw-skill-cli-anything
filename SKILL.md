---
name: cli-anything
description: Use when the user wants OpenClaw to build, refine, test, or validate a CLI-Anything harness for a GUI application or source repository. Adapts the CLI-Anything methodology to OpenClaw without changing the generated Python harness format.
version: 1.0.0
author: liwei626
tags: [cli, automation, gui, harness, openclaw]
---

## CLI-Anything Skill

This skill helps you build, refine, test, or validate a CLI-Anything harness for any GUI application or source repository.

### What is CLI-Anything?

CLI-Anything is a methodology for creating command-line interfaces for applications that don't have one. It generates a Python harness that can:
- Launch GUI applications
- Send keystrokes and mouse actions
- Read screen output via OCR
- Automate complex workflows

### When to Use This Skill

Use this skill when:
- The user wants to automate a GUI application
- The user needs to create a CLI for a source repository
- The user wants to test or validate an existing harness
- The user needs to refine a CLI-Anything implementation

### Workflow

1. **Analyze Requirements**
   - Understand the target application or repository
   - Identify the operations to automate
   - Determine input/output requirements

2. **Generate Harness**
   - Create Python harness using CLI-Anything methodology
   - Define CLI argument structure
   - Implement screen reading and interaction logic

3. **Test and Validate**
   - Test the harness against the target application
   - Validate OCR accuracy
   - Ensure reliable automation

4. **Refine and Optimize**
   - Improve error handling
   - Add logging and debugging
   - Optimize for performance

### Output Format

The skill generates:
- `harness.py` - Main CLI harness
- `README.md` - Usage documentation
- `requirements.txt` - Python dependencies

### Example

```python
#!/usr/bin/env python3
"""CLI-Anything harness for MyApp"""

import argparse
import subprocess
import time
from typing import Optional

def main():
    parser = argparse.ArgumentParser(description='CLI for MyApp')
    parser.add_argument('--input', required=True, help='Input file')
    parser.add_argument('--output', required=True, help='Output file')
    args = parser.parse_args()
    
    # Launch application
    proc = subprocess.Popen(['myapp'])
    time.sleep(2)
    
    # Send keystrokes
    # ...
    
    proc.terminate()

if __name__ == '__main__':
    main()
```

### Dependencies

- Python 3.8+
- pynput (for keyboard/mouse control)
- pyautogui (for screen capture)
- pytesseract (for OCR)

### License

MIT License - See LICENSE file for details.
