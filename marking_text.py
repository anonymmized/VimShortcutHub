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