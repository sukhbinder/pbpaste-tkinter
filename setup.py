import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pbpaste-win",
    version="0.1.0",
    author="Sukhbinder Singh",
    author_email="sukh2010@yahoo.com",
    description="A tiny uility to mimic pbpaste in windows.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sukhbinder/pbpaste-win",
    packages=setuptools.find_packages(),
    extras_require={
        "test": [
            "pytest",]
    },
    entry_points={"console_scripts": ["pbpaste = pbpastesrc.clipcon:get_clipboard_content_tkinter"]}
)


