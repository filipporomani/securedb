from src import securedb
with open(".key", "r") as f:
    key = f.read()
db = securedb.Db("db/example.sdb", key, force=True)


db.write("lol", 2)


print(db.get("lol"))

db.delete("lol")


print(db.get("lol"))