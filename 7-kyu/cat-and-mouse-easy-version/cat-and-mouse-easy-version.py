def cat_mouse(x):
    if len(x[1:-1]) > 3:
        return 'Escaped!'
    else:
        return 'Caught!'