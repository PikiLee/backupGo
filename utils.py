import sys, pathlib
from cryptography.fernet import Fernet


def exitIfPathNotExists(path, type="dir"):
    exit = False
    if type == "dir" and not path.is_dir():
        print(f"The path {path} is not a directory.")
        exit = True
    if type != "dir" and not path.is_file():
        print(f"The path {path} is not a file.")
        exit = True
    if not path.exists():
        print(f"The path {path} does not exist.")
        exit = True

    if exit:
        sys.exit(1)


def getFnet():
    print("Reading Key...")
    key_path = pathlib.Path("key").resolve()
    exitIfPathNotExists(key_path, "file")
    with open(key_path) as f:
        key = f.read()

    fnet = Fernet(key)
    print("Key readed.")
    return fnet
