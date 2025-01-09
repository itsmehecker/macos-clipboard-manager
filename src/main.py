import sys
import os

# Run the startup script
startup_script = os.path.join(os.path.dirname(__file__), '../startup.py')
exec(open(startup_script).read())

from ui.taskbar import TaskbarApp

def main():
    app = TaskbarApp()
    app.run()

if __name__ == "__main__":
    main()