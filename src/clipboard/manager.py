import pyperclip

class ClipboardManager:
    def __init__(self):
        self.history = []
        self.current_clipboard = ""

    def copy(self, text):
        pyperclip.copy(text)
        self.history.append(text)

    def paste(self):
        return pyperclip.paste()

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

    def check_clipboard(self):
        new_clipboard = pyperclip.paste()
        if new_clipboard != self.current_clipboard:
            self.current_clipboard = new_clipboard
            self.history.append(new_clipboard)