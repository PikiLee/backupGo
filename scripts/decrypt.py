from cryptography.fernet import Fernet
from .utils import exitIfPathNotExists, getFnet
import pathlib
import sys

def decrypt(input_p, output_d):
    print("Decrytion starts.")
    if not input_p or not output_d:
        raise Exception("地址不能为空")

    input_file = pathlib.Path(input_p).resolve()
    exitIfPathNotExists(input_file, "file")
    output_dir = pathlib.Path(output_d).resolve()
    exitIfPathNotExists(output_dir)
    filename = input_file.name.replace(".nmsl", "")

    # encrypt
    key_path = pathlib.Path("key").resolve()
    exitIfPathNotExists(key_path, "file")
    output_path = output_dir.joinpath(filename)

    fnet = getFnet()

    with open(input_file, "rb") as f:
        file = fnet.decrypt(f.read())

    with open(output_path, "wb") as f:
        f.write(file)

    print("Decryption succeeded.")
