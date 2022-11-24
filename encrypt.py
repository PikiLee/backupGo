import shutil
import random
import os
import sys
import datetime
import pathlib
from cryptography.fernet import Fernet
from utils import exitIfPathNotExists, getFnet


def encrypt(input_path, output_dir):
    print("Encryption starts.")
    input_path = pathlib.Path(input_path).resolve()
    temp_dir = pathlib.Path("temp").resolve()
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    if input_path.is_file():
        exitIfPathNotExists(input_path, "file")
        file_path = input_path
    elif input_path.is_dir():
        exitIfPathNotExists(input_path)
        # turn folder into a zip file

        random_name = str(random.random())
        file_path = temp_dir.joinpath(random_name)
        shutil.make_archive(file_path, "zip", input_path)
        file_path = pathlib.Path(str(file_path) + ".zip")

    output_dir = pathlib.Path(output_dir).resolve()
    exitIfPathNotExists(output_dir)

    # encrypt
    fnet = getFnet()
    with open(file_path, "rb") as f:
        cipher = fnet.encrypt(f.read())

    with open(
        output_dir.joinpath(
            "backup__" + datetime.datetime.now().strftime(f"%Y-%m-%d-%H-%M-%S")
        ),
        "wb",
    ) as f:
        f.write(cipher)

    shutil.rmtree(temp_dir)

    print("Encryption succeeded.")
