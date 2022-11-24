import sys
import pathlib
import os
from cryptography.fernet import Fernet
from .generate_keys import genKey

pathFilenames = {"en": "enpath", "de": "depath"}


def exitIfPathNotExists(path, type="dir"):
    exit = False
    if type == "dir" and not path.is_dir():
        message = f"{path} 不是文件"
        exit = True
    if type != "dir" and not path.is_file():
        message = f"{path} 不是目录"
        exit = True
    if not path.exists():
        message = f"{path} 不存在"
        exit = True

    if exit:
        raise Exception(message)

def getFnet():
    print("Reading Key...")
    key_path = pathlib.Path("key").resolve()

    if not key_path.exists():
        key = genKey()
    else:
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
