import os
import time
from rich.console import Console


console = Console()
MAIN_COLOR="#FFD700"

def show_ascii():
    art = """
     ██      ██ ██              ████████ ██                        ██                     ██   ██      ██         ██     
    ░██     ░██░░              ██░░░░░░ ░██                       ░██                    ░██  ░██     ░██        ░██     
    ░██     ░██ ██ ██████████ ░██       ░██       ██████  ██████ ██████  █████  ██   ██ ██████░██     ░██ ██   ██░██     
    ░░██    ██ ░██░░██░░██░░██░█████████░██████  ██░░░░██░░██░░█░░░██░  ██░░░██░██  ░██░░░██░ ░██████████░██  ░██░██████ 
     ░░██  ██  ░██ ░██ ░██ ░██░░░░░░░░██░██░░░██░██   ░██ ░██ ░   ░██  ░██  ░░ ░██  ░██  ░██  ░██░░░░░░██░██  ░██░██░░░██
      ░░████   ░██ ░██ ░██ ░██       ░██░██  ░██░██   ░██ ░██     ░██  ░██   ██░██  ░██  ░██  ░██     ░██░██  ░██░██  ░██
       ░░██    ░██ ███ ░██ ░██ ████████ ░██  ░██░░██████ ░███     ░░██ ░░█████ ░░██████  ░░██ ░██     ░██░░██████░██████ 
        ░░     ░░ ░░░  ░░  ░░ ░░░░░░░░  ░░   ░░  ░░░░░░  ░░░       ░░   ░░░░░   ░░░░░░    ░░  ░░      ░░  ░░░░░░ ░░░░░   
    """
    console.print(art, style=f"bold italic {MAIN_COLOR}")

def cursor_movement_list():
    commands = [
        ('h', 'move left'),
        ('j', 'move down'),
        ('k', 'move up'),
        ('l', 'move right'),
        ('w', 'jump by start of words (punctuation considered words)'),
        ('W', 'jump by words (spaces separate words)'),
        ('e', 'jump to end of words (punctuation considered words)'),
        ('E', 'jump to end of words (no punctuation)'),
        ('b', 'jump backward by words (punctuation considered words)'),
        ('B', 'jump backward by words (no punctuation)'),
        ('0', '(zero) start of line'),
        ('^', 'first non-blank character of line'),
        ('$', 'end of line'),
        ('G', 'Go To command (prefix with number - 5G goes to line 5)'),
        ('Note', 'Prefix a cursor movement command with a number to repeat it. For example, 4j moves down 4 lines.')

    ]
    return '\n'.join(f"{cmd} - {desc}" for cmd, desc in commands)

def cut_paste_list():
    ct_pst_list = """
yy - yank (copy) a line
2yy - yank 2 lines
yw - yank word
y$ - yank to end of line
p - put (paste) the clipboard after cursor
P - put (paste) before cursor
dd - delete (cut) a line
dw - delete (cut) the current word
x - delete (cut) current character
    """
    return ct_pst_list 
    
def editing_list():
    main_list = """
r - replace a single character (does not use insert mode)
J - join line below to the current one
cc - change (replace) an entire line
cw - change (replace) to the end of word
c$ - change (replace) to the end of line
s - delete character at cursor and subsitute text
S - delete line at cursor and substitute text (same as cc)
xp - transpose two letters (delete and paste, technically)
u - undo
. - repeat last command
    """
    return main_list 

def exiting_list():
    ext_list = """ 
:w - write (save) the file, but don't exit
:wq - write (save) and quit
:q - quit (fails if anything has changed)
:q! - quit and throw away changes
    """
    return ext_list 

def insert_mode_list():
    insert_list = """
i - start insert mode at cursor
I - insert at the beginning of the line
a - append after the cursor
A - append at the end of the line
o - open (append) blank line below current line (no need to press return)
O - open blank line above current line
ea - append at end of word
Esc - exit insert mode

The register is important
    """

    return insert_list 

def marking_text_list():
    marking_list = """
v - start visual mode, mark lines, then do command (such as y-yank)
V - start Linewise visual mode
o - move to other end of marked area
Ctrl+v - start visual block mode
O - move to Other corner of block
aw - mark a word
ab - a () block (with braces)
aB - a {} block (with brackets)
ib - inner () block
iB - inner {} block
Esc - exit visual mode
    """
    return marking_list 

def search_replace_list():
    srch_rplc_list = r"""
/pattern - search for pattern
?pattern - search backward for pattern
n - repeat search in same direction
N - repeat search in opposite direction
:%s/old/new/g - replace all old with new throughout file
:%s/old/new/gc - replace all old with new throughout file with confirmations
    """
    return srch_rplc_list 

def visual_commands_list():
    visual_commnds_list = """
> - shift right
< - shift left
y - yank (copy) marked text
d - delete marked text
~ - switch case
    """
    return visual_commnds_list 

def multiple_work_list():
    mltpl_wrk_list = """
:e filename - Edit a file in a new buffer
:bnext (or :bn) - go to next buffer
:bprev (of :bp) - go to previous buffer
:bd - delete a buffer (close a file)
:sp filename - Open a file in a new buffer and split window
ctrl+ws - Split windows
ctrl+ww - switch between windows
ctrl+wq - Quit a window
ctrl+wv - Split windows vertically
    """ 
    return mltpl_wrk_list

def show_menu():
    menu_options = [
        ('1', 'Cursor movement'),
        ('2', 'Insert Mode - Inserting/Appending text'),
        ('3', 'Editing'),
        ('4', 'Marking text'),
        ('5', 'Visual commands'),
        ('6', 'Cut and Paste'),
        ('7', 'Exiting'),
        ('8', 'Search/Replace'),
        ('9', 'Working with multiple files')
    ]

    for key, desc in menu_options:
        console.print(f"[[ {key} ]] -- {desc}", style=f"bold italic {MAIN_COLOR}")

def main():
    cursor = cursor_movement_list()
    cut_paste = cut_paste_list()
    editing = editing_list()
    exiting = exiting_list()
    insert = insert_mode_list()
    marking = marking_text_list()
    search_replace = search_replace_list()
    visual = visual_commands_list()
    multiple = multiple_work_list()
    choice_dict = {'1': cursor, 
    '2': insert, 
    '3': editing,
    '4': marking, 
    '5': visual,
    '6': cut_paste,
    '7': exiting,
    '8': search_replace,
    '9': multiple}
    
    while True:
        show_menu()
        console.print("Choose the desired topic or 'q' to quit: ", style=f"italic {MAIN_COLOR}")
        target = input().strip()
        if target.lower() == 'q':
            console.print("Exit from the program...", style="bold italic red")
            break
        if int(target) not in range(1, 10):
            console.print("There is no such option", style="bold italic red")
            continue
        for key, value in choice_dict.items():
                if target == key:
                    os.system('clear')
                    console.print(value, style=f"bold italic {MAIN_COLOR}")
                    time.sleep(3)

if __name__ == "__main__":
    show_ascii()
    main()
    