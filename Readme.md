# pbpaste-tkinter: python code to mimic pbpaste in windows

Simple command-line tool that mimics pbpaste in windows.

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


**How it works**

1. The script creates a hidden tkinter window.
2. It retrieves the current clipboard contents using `root.clipboard_get()`.
3. The retrieved text is then printed to the console.


