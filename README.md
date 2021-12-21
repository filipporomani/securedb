# securedb
[![Downloads](https://pepy.tech/badge/securedb)](https://pepy.tech/project/securedb) [![PyPi version](https://badgen.net/pypi/v/securedb/)](https://pypi.com/project/securedb)
## securedb is a Python framework that lets you work with encrypted JSON databases.
## `pip install securedb --upgrade`
## Content index
- [Creating a DB](#creation)
  - [Encryption key generation](#key)
  - [Database initialization](#initialization)
- [Writing values](#writing)
  - [write()](#write)
  - [write_many()](#write_many)
- [Deleting values](#deleting)
  - [delete()](#delete)
  - [delete_many()](#delete_many)
  - [clear()](#clear)
- [Reading values](#reading)
  - [get()](#get)
  - [get_many()](#get_many)



# Documentation
## Creation
### Key
To create a database, an encryption key is needed. To generate it, you can use the built-in `newkey()` function.
```py
import securedb
securedb.newkey()
```
This will create a new file named ".key" which contains a randomly generated encryption key.

### Initialization
Now, create a blank file (there aren't file extensions restrictions), copy the path and the init the Db() class:
```py
import securedb
with open(".key", "r") as f:
    key = f.read()
db = securedb.Db(path, bytes(key.encode()))
```
Remember that if you lost your key there will be no way to recover the database content, so keep it safe!

## Writing
### write()
The `write(key, value)` function allows you to insert a single value into the database.
`key` is the value name
`value` is the value data.

`key` is used to access the data, and must be an integral or a string;
`value` can be anything such as boolean, integer, string, array, list, dictionary ecc.

### write_many()
The `write_many(payload)` function allows you to write many values in a single time. 
`payload is a dictionary with all the values you need to insert:
`{key: value, key1: value1, key2: value2}` etc.
There isn't any limit regarding the size of the dictionary; theoretically you can write an infinite amount of values at the same time.

## Deleting
### delete()
The `delete(key)` function allows you to delete a single value from the database.
`key` is the value's key inside the database (see [write](##writing)) and must be a string or an integer. 

### delete_many()
The `delete_many(payload)` function allows you to delete many values at the same time.
`payload` is a list of the keys you want to delete:
`[key, key1, key2]` etc. 

### clear()
The `clear()` functions is a dangerous function that allows you to erease the whole database. 
Be careful using it, because this action cannot be undone and the function doesn't ask confirmation before ereasing the database.

## Reading
### get()
To read any value from the database, you need to use the `get(key)` function.
`key` is the key of the value you want to read (see [write](##writing)).

### get_many()
To read any value from the database, you need to use the `get_many(keys)` function.
`keys` is a list of the keys you want to read (see [write](##writing)).
