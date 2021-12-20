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
    def __init__(self, path, key):
        self.path = path
        self.key = key
        try:
            if os.path.isfile(path):
                f = open(path, "r")
                if f.read() == "":
                    with open(path, "w") as f:
                        to_write = encrypt(key, ("{}").encode())
                        f.write(str(to_write))
                        f.close()
                        f = open(path, "r")
                        self.payload = eval(f.read())
                else:
                    f = open(path, "r")
                    self.payload = eval(f.read())
            else:
                raise PathError
            
        except PathError:
            print("The specified database does not exist.")

    def write(self, key, value):
        to_dict = decrypt(self.key, bytes(self.payload))
        ev = eval(to_dict.decode())
        data = dict(ev)
        data[key] = value
        with open(self.path, "w") as f:
            to_encrypt = str(data).encode()
            to_write = encrypt(self.key, (to_encrypt))
            f.write(str(to_write))
            f.close()
        return "Key written to the database"

    def write_many(self, payload: dict):
        to_dict = decrypt(self.key, bytes(self.payload))
        ev = eval(to_dict.decode())
        data = dict(ev)
        for key, value in payload.items():
            data[key] = value
        with open(self.path, "w") as f:
            
            to_encrypt = str(data).encode()
            to_write = encrypt(self.key, (to_encrypt))
            f.write(str(to_write))
            f.close()
        return "Keys written to the database"
    
    def clear(self):
        f = open(self.path, 'r+')
        f.truncate(0)
        f.close()
        return "Database ereased"

    def get(self, key):
        f = open(self.path, "r")
        l = eval(f.read())
        to_dict = decrypt(self.key, bytes(l))
        ev = eval(to_dict.decode())
        data = dict(ev)
        try:
            return data[key]
        except KeyError:
            print(f"Key {key} does not exist.")

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
                print(f"Key {x} could not be resolved.")
        return els

    def delete(self, key):
        to_dict = decrypt(self.key, bytes(self.payload))
        ev = eval(to_dict.decode())
        data = dict(ev)
        try:
            data.pop(key)
        except:
            print(f"Key {key} was not deleted because it does not exist.")
        with open(self.path, "w") as f:
            to_encrypt = str(data).encode()
            to_write = encrypt(self.key, (to_encrypt))
            f.write(str(to_write))
            f.close()
        return "Key deleted from the database"

    def delete_many(self, payload: list):
        to_dict = decrypt(self.key, bytes(self.payload))
        ev = eval(to_dict.decode())
        data = dict(ev)
        for x in payload:
            try:
                data.pop(x)
            except:
                print(f"Key {x} was not deleted because it does not exist.")
                continue
        with open(self.path, "w") as f:
            to_encrypt = str(data).encode()
            to_write = encrypt(self.key, (to_encrypt))
            f.write(str(to_write))
            f.close()
        return "Keys deleted from the database"