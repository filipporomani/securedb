import securedb
with open(".key", "r") as f:
    key = f.read()
db = securedb.Db("db/example.sdb", bytes(key.encode()))