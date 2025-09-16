# VimShortcutHub
A simple command-line Vim cheatsheet built with Python and Rich.
This program provides quick access to the most commonly used Vim commands, organized into categories for easy navigation.
## ✨ Features
- Beautiful ASCII art welcome screen
- Menu-driven interface with colored output
- Categories of Vim commands:
  - Cursor movement
  - Insert mode
  - Editing
  - Marking text
  - Visual commands
  - Cut & Paste
  - Exiting
  - Search & Replace
  - Working with multiple files
- Easy navigation and quitting option
## 📦 Requirements
- Python 3.7+
- rich library
Install dependencies with:
```bash
pip install rich
```
## ▶️ Usage
Run the program with:
```bash
python vim_cheatsheet.py
```
You’ll see the ASCII art and a numbered menu like this:
```
[[ 1 ]] -- Cursor movement
[[ 2 ]] -- Insert Mode - Inserting/Appending text
[[ 3 ]] -- Editing
...
[[ 9 ]] -- Working with multiple files
```
- Enter the number of the desired topic to see Vim commands.
- Type q to quit the program.
## 🖥️ Example
```
Choose the desired topic or 'q' to quit: 1
h - move left
j - move down
k - move up
l - move right
...
```
