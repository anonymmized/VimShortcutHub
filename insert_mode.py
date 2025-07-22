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