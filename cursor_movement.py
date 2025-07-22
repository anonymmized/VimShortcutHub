def cursor_movement_list():
    movement_list = """
    h - move left
    j - move down
    k - move up
    l - move right
    w - jump by start of words (punctuation considered words)
    W - jump by words (spaces separate words)
    e - jump to end of words (punctuation considered words)
    E - jump to end of words (no punctuation)
    b - jump backward by words (punctuation considered words)
    B - jump backward by words (no punctuation)
    0 - (zero) start of line
    ^ - first non-blank character of line
    $ - end of line
    G - Go To command (prefix with number - 5G goes to line 5)

    Prefix a cursor movement command with a number to repeat it. For example, 4j moves down 4 lines.
    """
    return movement_list