
a = 3
# from temp.clear_all import clear_all

def clear_all():
    """Clears all the variables from the workspace of the spyder application."""
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]

    print("imported")

# if __name__ == "__main__":
#     clear_all()

clear_all()
