# pbpaste-tkinter: A Simple Tkinter Script to Get Clipboard Content
====================================================================

This is a simple Python script that uses the tkinter library to get the clipboard content. It can be used as a command-line tool or integrated into other projects.
It mimics pbpaste.

**How it works**

1. The script creates a hidden tkinter window.
2. It retrieves the current clipboard contents using `root.clipboard_get()`.
3. The retrieved text is then printed to the console.

**Installation and Usage**

You can install this package using pip:
```
pip install pbpaste-tkinter
```

Once installed, you can use it as a command-line tool by running:
```
pbpaste
```

This will print the current clipboard contents to the console.
