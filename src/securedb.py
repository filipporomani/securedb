import os
from cryptography.fernet import Fernet

class Error(Exception):
    pass
class PathError(Error):
    pass

def encrypt(key, data):
    fernet = Fernet(key)
    return fernet.encrypt(data)
def decrypt(key, data):
    fernet = Fernet(key)
    return fernet.decrypt(data)

def newkey():
        keyfile = open(".key", "w+")
        editable = Fernet.generate_key()
        key1 = str(editable).replace("b'", "")
        key = str(key1).replace("'", "")
        keyfile.write(str(key))

class Db():
    def __init__(self, path: str, key: str, **kwargs):
        self.path = path
        self.key = bytes(key.encode())
        self.force = kwargs.get("force", False)

        try:
            if os.path.isfile(path): 
                f = open(path, "r")
                if f.read() == "": # If the file is empty
                    with open(path, "w") as f:
                        to_write = encrypt(key, ("{}").encode()) # Write an empty dict and setup a new database
                        f.write(str(to_write))
                        f.close()
            else:
                if self.force: # New in 1.1.0: force=True -> Create a new database if it does not exist
                    with open(path, "w+") as f:
                        to_write = encrypt(key, ("{}").encode())
                        f.write(str(to_write))
                        f.close()
                else:
                    raise PathError
            
        except PathError:
            print("The specified database does not exist. Enable force to create a new database without raising an error.")



    def write(self, key, value):
        try:
            f = open(self.path, "r").read()
            to_dict = decrypt(self.key, bytes(eval(f)))
            data = dict(eval(to_dict.decode()))
            data[key] = value
            with open(self.path, "w") as f:
                to_encrypt = str(data).encode()
                to_write = encrypt(self.key, (to_encrypt))
                f.write(str(to_write))
                f.close()
            return True
        except:
            return False

    def write_many(self, payload: dict):
        try:
            f = open(self.path, "r").read()
            to_dict = decrypt(self.key, bytes(eval(f)))
            data = dict(eval(to_dict.decode()))
            for key, value in payload.items():
                data[key] = value
            with open(self.path, "w") as f:
                
                to_encrypt = str(data).encode()
                to_write = encrypt(self.key, (to_encrypt))
                f.write(str(to_write))
                f.close()
            return True
        except:
            return False
    
    def clear(self):
        try:
            f = open(self.path, 'r+')
            f.truncate(0)
            f.close()
            return True
        except:
            return False

    def get(self, key):
        f = open(self.path, "r")
        l = eval(f.read())
        to_dict = decrypt(self.key, bytes(l))
        data = dict(eval(to_dict.decode()))
        try:
            return data[key]
        except KeyError:
            print(f"Error getting {key}: key {key} does not exist.")
            return False

    def get_many(self, keys : list):
        f = open(self.path, "r")
        l = eval(f.read())
        to_dict = decrypt(self.key, bytes(l))
        ev = eval(to_dict.decode())
        data = dict(ev)
        els = {}
        for x in keys:
            try:
                els[x] = data[x]
            except KeyError:
                print(f"Error getting many keys: key {x} could not be resolved.")
        return els

    def delete(self, key):
        f = open(self.path, "r").read()
        to_dict = decrypt(self.key, bytes(eval(f)))
        data = dict(eval(to_dict.decode()))
        try:
            data.pop(key)
        except:
            print(f"Error deleting {key}: key {key} was not deleted because it does not exist.")
            return False
        with open(self.path, "w") as f:
            to_encrypt = str(data).encode()
            to_write = encrypt(self.key, (to_encrypt))
            f.write(str(to_write))
            f.close()
        return True

    def delete_many(self, payload: list):
        f = open(self.path, "r").read()
        to_dict = decrypt(self.key, bytes(eval(f)))
        ev = eval(to_dict.decode())
        data = dict(ev)
        for x in payload:
            try:
                data.pop(x)
            except:
                print(f"Error deleting many keys: key {x} was not deleted because it does not exist.")
                continue
        with open(self.path, "w") as f:
            to_encrypt = str(data).encode()
            to_write = encrypt(self.key, (to_encrypt))
            f.write(str(to_write))
            f.close()
        return True