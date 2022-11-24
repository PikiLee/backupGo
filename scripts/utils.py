import sys
import pathlib
import os
from cryptography.fernet import Fernet

pathFilenames = {"en": "enpath", "de": "depath"}


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


def readEncryptionPaths(type="en"):
    path = pathlib.Path(pathFilenames[type]).resolve()
    if not path.exists():
        return None
    else:
        with open(path) as f:
            input_path = f.readline().replace("\n", "")
            output_path = f.readline().replace("\n", "")

        return (input_path, output_path)


def saveEncryptionPaths(input_path, output_path, type="en"):
    path = pathlib.Path(pathFilenames[type]).resolve()
    if path.exists():
        os.remove(path)
    with open(path, "w") as f:
        f.write(input_path + "\n")
        f.write(output_path + "\n")
