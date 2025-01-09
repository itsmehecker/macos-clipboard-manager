import rumps
from clipboard.manager import ClipboardManager

class TaskbarApp(rumps.App):
    def __init__(self):
        super(TaskbarApp, self).__init__("Clipboard Manager", icon="clip.png")
        self.clipboard_manager = ClipboardManager()
        self.menu = ["Clear Clipboard History", None]  # None adds a separator
        self.update_clipboard_history()
        self.timer = rumps.Timer(self.check_clipboard, 3)  # Check clipboard every 5 seconds
        self.timer.start()

    @rumps.clicked("Clear Clipboard History")
    def clear_clipboard_history(self, _):
        self.clipboard_manager.clear_history()
        self.update_clipboard_history()
        rumps.alert("Clipboard history cleared.")
    
    def update_clipboard_history(self):
        # Remove old clipboard history items
        self.menu.clear()
        self.menu.add("Clear Clipboard History")
        self.menu.add(None)  # Add separator

        # Add new clipboard history items
        for item in self.clipboard_manager.get_history():
            self.menu.add(rumps.MenuItem(item, callback=self.copy_to_clipboard))

    def copy_to_clipboard(self, sender):
        self.clipboard_manager.copy(sender.title)
        print(f"Copied {sender.title} to clipboard.")

    def check_clipboard(self, _):
        self.clipboard_manager.check_clipboard()
        self.update_clipboard_history()

    def run(self):
        super().run()