#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarea1.settings')
>>>>>>> 82a4018cf60c6f85920295766337339584e54363
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
