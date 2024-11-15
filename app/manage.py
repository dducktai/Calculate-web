#!/usr/bin/env python
import os
import sys
import time

if __name__ == "__main__":
    start_time = time.time()  # Ghi lại thời gian khởi động server
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Calculator.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    finally:
        uptime = time.time() - start_time
        print(f"Server uptime: {uptime:.2f} seconds")
    execute_from_command_line(sys.argv)
    

    

        
