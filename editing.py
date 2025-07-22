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