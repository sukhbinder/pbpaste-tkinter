import tkinter as tk


def get_clipboard_content_tkinter():
    root = tk.Tk()
    root.withdraw()
    clipboard_content = root.clipboard_get()
    root.destroy()
    print(clipboard_content)


if __name__ == "__main__":
    get_clipboard_content_tkinter()
