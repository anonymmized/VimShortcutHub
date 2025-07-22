from rich.console import Console
from cursor_movement import cursor_movement_list
from cut_paste import cut_paste_list
from editing import editing_list
from exiting import exiting_list
from insert_mode import insert_mode_list
from marking_text import marking_text_list
from search_replace import search_replace_list
from visual_commands import visual_commands_list
from working_with_multiple_files import multiple_work_list

console = Console()
MAIN_COLOR="#FFD700"

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
    console.print("{1} -- Cursor movement", style=f"bold italic {MAIN_COLOR}")
    console.print("{2} -- Insert Mode - Inserting/Appending text", style=f"bold italic {MAIN_COLOR}")
    console.print("{3} -- Editing", style=f"bold italic {MAIN_COLOR}")
    console.print("{4} -- Marking text", style=f"bold italic {MAIN_COLOR}")
    console.print("{5} -- Visual commands", style=f"bold italic {MAIN_COLOR}")
    console.print("{6} -- Cut and Paste", style=f"bold italic {MAIN_COLOR}")
    console.print("{7} -- Exiting", style=f"bold italic {MAIN_COLOR}")
    console.print("{8} -- Search/Replace", style=f"bold italic {MAIN_COLOR}")
    console.print("{9} -- Working with multiple files", style=f"bold italic {MAIN_COLOR}")
    console.print("Choose the desired topic: ", style=f"italic {MAIN_COLOR}")
    target = input()
    if 0 < int(target) < 10:
        for key, value in choice_dict.items():
            if target == key:
                print(value)

    