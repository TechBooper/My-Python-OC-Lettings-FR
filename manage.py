import os
import sys


def main():
    """
    The main entry point for the Django application.

    This function sets the default Django settings module for the project,
    checks if Django is properly installed, and executes commands from
    the command line.

    Steps:
    1. Sets the environment variable `DJANGO_SETTINGS_MODULE` to the settings module for the project.
    2. Attempts to import `execute_from_command_line` from Django's core management.
       - If Django is not installed or cannot be imported, raises an informative ImportError.
    3. Executes the command-line arguments using Django's management utility.

    Raises:
        ImportError: If Django is not installed or unavailable on the PYTHONPATH.

    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    """
    Ensures that the script runs only when executed directly,
    and not when imported as a module.
    """
    main()
