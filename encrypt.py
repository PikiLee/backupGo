import shutil
import random
import os, sys, datetime, pathlib
from cryptography.fernet import Fernet
from utils import exitIfPathNotExists, getFnet


def encrypt(input_dir, output_dir):
    print("Encryption starts.")
    input_dir = pathlib.Path(input_dir).resolve()
    exitIfPathNotExists(input_dir)
    output_dir = pathlib.Path(output_dir).resolve()
    exitIfPathNotExists(output_dir)

    # turn folder into a zip file
    temp_dir = pathlib.Path("temp").resolve()
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    random_name = str(random.random())
    file_path = temp_dir.joinpath(random_name)
    shutil.make_archive(file_path, "zip", input_dir)
    file_path = pathlib.Path(str(file_path) + ".zip")

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
