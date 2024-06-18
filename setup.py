import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pbpaste-tkinter",
    version="0.1.0",
    author="Sukhbinder Singh",
    author_email="sukh2010@yahoo.com",
    description="A simple Tkinter script to get clipboard content.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sukhbinder/pbpaste-tkinter",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["pbpaste = pbpastesrc.clipcon:get_clipboard_content_tkinter"]}
)


