import platform
import os
import sys
import struct

def check_environment():
    print("=== System Information ===")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {sys.version}")
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    
    # Check if running on ARM
    is_arm = "arm" in platform.machine().lower() or "aarch" in platform.machine().lower()
    if is_arm:
        print("Detected: ARM Architecture")
    else:
        print("Detected: Non-ARM Architecture")
    
    # Check OS type
    if os.name == "nt":
        print("Operating System: Windows")
    elif os.name == "posix":
        print("Operating System: Unix/Linux-based")
    else:
        print("Operating System: Unknown")

if __name__ == "__main__":
    check_environment()
