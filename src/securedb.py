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


def newkey(**kwargs):
    # New in 2.0.0: keyfile now supports custom path
    keyfile = open(kwargs.get("keyfile", ".key"), "w+")
    editable = Fernet.generate_key()
    key1 = str(editable).replace("b'", "")
    key = str(key1).replace("'", "")
    keyfile.write(str(key))


class Db:
    def __init__(self, path: str, key: str, **kwargs):
        self.path = path
        try:
            with open(key, "r") as f:
                keyf = f.read()
        except FileNotFoundError:
            raise PathError(f"Error: key file {key} does not exist.")
        self.key = bytes(keyf.encode())
        self.force = kwargs.get("force", False)

        try:
            if os.path.isdir(path):
                return None
            else:
                if self.force:  # New in 1.1.0: force=True -> Create a new database if it does not exist
                    os.mkdir(path + "/")
                else:
                    raise PathError

        except:
            raise PathError(
                "The specified database does not exist. Enable force to create a new database without raising an error.")

    def write(self, key, value):
        f = open(self.path + '/' + str(key) + ".sdbk", "w+").read()
        if f == "":
            f = str(encrypt(self.key, str({}).encode()))
        to_dict = decrypt(self.key, bytes(eval(f)))
        data = dict(eval(to_dict.decode()))
        data[key] = value
        with open(self.path + '/' + str(key) + ".sdbk", "w") as f:
            to_encrypt = str(data).encode()
            to_write = encrypt(self.key, (to_encrypt))
            f.write(str(to_write))
            f.close()
        return True

    def write_many(self, payload: dict):
        try:
            for x in payload.keys():
                f = open(self.path + '/' + str(x) + ".sdbk", "w+").read()
                if f == "":
                    f = str(encrypt(self.key, str({}).encode()))

                to_dict = decrypt(self.key, bytes(eval(f)))
                data = dict(eval(to_dict.decode()))
                data[x] = payload[x]
                with open(self.path + '/' + str(x) + ".sdbk", "w") as f:
                    to_encrypt = str(data).encode()
                    to_write = encrypt(self.key, (to_encrypt))
                    f.write(str(to_write))
                    f.close()
            return True
        except:
            return False

    def clear(self):
        for x in os.listdir(self.path):
            os.remove(self.path + "/" + x)

    def get(self, key):
        try:
            f = open(self.path + '/' + str(key) + ".sdbk", "r")
        except FileNotFoundError:
            raise KeyError(f"Key {key} does not exist.")
        l = eval(f.read())
        to_dict = decrypt(self.key, bytes(l))
        data = dict(eval(to_dict.decode()))
        try:
            return data[key]
        except KeyError:
            # New in 2.0.0: KeyErrors now raise a KeyError instead of printing a message. This is to make it easier to catch errors.
            raise KeyError(f"Error getting {key}: key {key} does not exist.")

    def get_many(self, keys: list):
        try:
            els = {}
            for key in keys:
                try:
                    f = open(self.path + '/' + str(key) + ".sdbk", "r").read()
                except FileNotFoundError:
                    raise KeyError(f"Key {key} does not exist.")

                to_dict = decrypt(self.key, bytes(eval(f)))
                data = dict(eval(to_dict.decode()))
                try:
                    els[key] = data[key]
                except KeyError:
                    raise KeyError(
                        f"Error getting many keys: key {key} could not be resolved.")
            return els
        except:
            return False

    def delete(self, key):
        try:
            os.remove(self.path + '/' + str(key) + ".sdbk")
            return True
        except FileNotFoundError:
            raise KeyError(f"Error deleting {key}: key {key} does not exist.")
            return False

    def delete_many(self, payload: list):
        for key in payload:
            try:
                os.remove(self.path + '/' + str(key) + ".sdbk")
            except FileNotFoundError:
                raise KeyError(
                    f"Error deleting {key}: key {key} does not exist.")

        return True
