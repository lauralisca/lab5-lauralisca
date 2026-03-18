global_int = None
global_Str = None

def set_globals(some_int, some_str):
    global global_int
    global global_Str

    global_int = some_int
    global_Str = some_str

def get_globals ():
    return (global_int, global_Str)