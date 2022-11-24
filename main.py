from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from components.file_selector import FileSelector
from components.base_component import BaseComponent
from encrypt import encrypt
from decrypt import decrypt
from utils import readEncryptionPaths, saveEncryptionPaths


class App(BaseComponent):
    def __init__(self, root):
        root.title("backupGo")
        root.geometry("600x200")
        root.iconbitmap("icon.ico")

        main_frame = Frame(root)
        self.get_full_width(main_frame, root, 10)

        main_notebook = Notebook(main_frame)
        self.get_full_width(main_notebook, main_frame)

        encrypt_frame = Frame(main_notebook)
        self.get_full_width(encrypt_frame, main_notebook, 25)
        encrypt_frame.columnconfigure(56, weight=1)

        decrypt_frame = Frame(main_notebook)
        self.get_full_width(decrypt_frame, main_notebook, 25)
        decrypt_frame.columnconfigure(56, weight=1)

        main_notebook.add(encrypt_frame, text="备份")
        main_notebook.add(decrypt_frame, text="解密")
        
        # Encryption Page
        res = readEncryptionPaths()
        if res:
            self.input_path = StringVar(value=res[0])
            self.output_path = StringVar(value=res[1])
        else:
            self.input_path = StringVar()
            self.output_path = StringVar()

        FileSelector(encrypt_frame, self.input_path, "输入", column=55, row=55)
        FileSelector(encrypt_frame, self.output_path, "输出目录",
                     column=55, row=60, allow_types=["dir"])

        self.error = StringVar()
        errorLabel = Label(encrypt_frame, text=self.error.get(), textvariable=self.error)
        errorLabel.grid(column=55, row=63, columnspan=4, rowspan=3)

        confirmButton = Button(
            encrypt_frame, text="开始加密备份",  command=self.backup)
        confirmButton.grid(column=56, row=70, columnspan=2)

        infoLabel = Label(encrypt_frame, text="首次加密后，在软件安装目录里的key文件内查看密钥，请妥善保存。")
        infoLabel.grid(column=55, row=75, columnspan=4)

        # Decryption Page

        res = readEncryptionPaths(type="de")
        if res:
            self.input_de_path = StringVar(value=res[0])
            self.output_de_path = StringVar(value=res[1])
        else:
            self.input_de_path = StringVar()
            self.output_de_path = StringVar()

        FileSelector(decrypt_frame, self.input_de_path, "输入", column=55, row=55, allow_types=["file"])
        FileSelector(decrypt_frame, self.output_de_path, "输出目录",
                     column=55, row=60, allow_types=["dir"])

        self.de_error = StringVar()
        de_errorLabel = Label(decrypt_frame, text=self.de_error.get(), textvariable=self.de_error)
        de_errorLabel.grid(column=55, row=63, columnspan=4, rowspan=3)

        confirm_de_button = Button(
            decrypt_frame, text="开始解密备份",  command=self.unbackup)
        confirm_de_button.grid(column=55, row=70, columnspan=3)

    def backup(self):
        try:
            self.error.set("")
            self.error.set("开始加密备份")
            saveEncryptionPaths(self.input_path.get(), self.output_path.get())
            encrypt(self.input_path.get(), self.output_path.get())
            self.error.set("备份成功")
        except Exception as error: 
            self.error.set(error)
        
    def unbackup(self):
        try:
            self.de_error.set("")
            self.de_error.set("开始解密")
            saveEncryptionPaths(self.input_de_path.get(), self.output_de_path.get(), type="de")
            decrypt(self.input_de_path.get(), self.output_de_path.get())
            self.de_error.set("解密成功")
        except Exception as de_error: 
            self.de_error.set(de_error)



root = Tk()
App(root)
root.mainloop()
