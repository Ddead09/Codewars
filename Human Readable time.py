def make_readable(seconds):
    hours=int(seconds/3600)
    minutes=int(seconds/60%60)
    s=int(seconds%60)
    return f'{hours:02}:{minutes:02}:{s:02}'
