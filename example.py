import securedb
db = securedb.Db("db/example.sdb", b'jbOmCnLhN3S2UQJAYaqoV6GXBIC4M8x_ZZvOtvNxzdI=')


db.write_many({'lol': 1, "lol1": 2})

a = db.get('lol')

print(a)