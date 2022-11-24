from cryptography.fernet import Fernet
from utils import exitIfPathNotExists, getFnet
import pathlib
import sys

print("Decrytion starts.")

input_file = pathlib.Path(sys.argv[1]).resolve()
exitIfPathNotExists(input_file, "file")
output_dir = pathlib.Path(sys.argv[2]).resolve()
exitIfPathNotExists(output_dir)

# encrypt
key_path = pathlib.Path("key").resolve()
exitIfPathNotExists(key_path, "file")
output_path = output_dir.joinpath(input_file.name + ".zip")

fnet = getFnet()

with open(input_file, "rb") as f:
    file = fnet.decrypt(f.read())

with open(output_path, "wb") as f:
    f.write(file)

print("Decryption succeeded.")
