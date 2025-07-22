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