# pbpaste-win: Small uility to mimic pbpaste in windows
[![PyPI](https://img.shields.io/pypi/v/llm-embed-ollama.svg)](https://pypi.org/project/pbpaste-win/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/pbpaste-win?include_prereleases&label=changelog)](https://github.com/sukhbinder/pbpaste-win/releases)
[![Tests](https://github.com/sukhbinder/pbpaste-win/workflows/Test/badge.svg)](https://github.com/sukhbinder/pbpaste-win/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/pbpaste-win/blob/main/LICENSE)

Simple command-line tool that mimics pbpaste in windows.

**Installation and Usage**

You can install this package using pip:
```
pip install pbpaste-win
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


