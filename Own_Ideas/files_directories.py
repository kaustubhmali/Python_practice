import glob, os


def select_dir(path):
    try:
        if not path:
            print("Empty Directory")
        else:
            print(f"Path Loaded: {path}")
            return os.chdir(path)
    except ValueError:
        print("Invalid Path: ")


def file_ext(extension):
    files = []
    for file in glob.glob(extension):
        # if str(file[::-4]) = ".exe":
        last_chars = file[-3:]
        files.append(file)
    return last_chars, files


def select_ext(number):
    if number == 1:
        return file_ext("*.msi")
    elif number == 2:
        return file_ext("*.exe")
    else:
        return "Invalid Selection"


def decor(func):
    def wrap(args):
        symbol = "*"
        print(symbol.join(symbol * len(args)))
        func(args)
        print(symbol.join(symbol * len(args)))

    return wrap


selected_path = str(input("Enter your Directory Path: "))

print(f"Enter path for the directory: {decor(select_dir(selected_path))}")

print("""\nSelect the extensions in the Directory: 
\n\t 1. exe
\n\t 2. msi 
        """)
selected_extension = int(input("Enter your selection: "))
print(f"Your selected: {select_ext(selected_extension)}")
