from src import securedb
with open(".key", "r") as f:
    key = f.read()
db = securedb.Db("db/example.sdb", bytes(key.encode()))

db.write("lol", 2)


db.delete("lol")

print(db.get("lol"))