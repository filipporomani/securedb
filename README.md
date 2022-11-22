# securedb
[![Downloads](https://static.pepy.tech/personalized-badge/securedb?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pypi.org/project/securedb) [![PyPi version](https://badgen.net/pypi/v/securedb/)](https://pypi.org/project/securedb) [![PyPI status](https://img.shields.io/pypi/status/securedb.svg)](https://pypi.python.org/pypi/securedb/)
## securedb is a Python framework that lets you work with encrypted JSON databases.
## `pip install securedb --upgrade`
## Content index
- [securedb](#securedb)
  - [securedb is a Python framework that lets you work with encrypted JSON databases.](#securedb-is-a-python-framework-that-lets-you-work-with-encrypted-json-databases)
  - [`pip install securedb --upgrade`](#pip-install-securedb---upgrade)
  - [Content index](#content-index)
- [Documentation](#documentation)
  - [New in 1.1.0](#new-in-110)
  - [Creation](#creation)
    - [Key](#key)
    - [Initialization](#initialization)
  - [Writing](#writing)
    - [write()](#write)
    - [write\_many()](#write_many)
  - [Deleting](#deleting)
    - [delete()](#delete)
    - [delete\_many()](#delete_many)
    - [clear()](#clear)
  - [Reading](#reading)
    - [get()](#get)
    - [get\_many()](#get_many)



# Documentation

## New in 1.1.0
-  `force` kwarg added in the initialization; see [initialization](#Initialization)
-  You don't need to manually encode the key during the initialization
-  If there is no error, all the functions now return `True`
-  Useless print() functions were removed
-  Smoother error handling


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
db = securedb.Db(path, key, force=True)
```
With `force=True` the program will create a new db in the given path if no database is found. `force` is default set to `False`.
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
There isn't any limit regarding the size of the input dictionary.

## Deleting
### delete()
The `delete(key)` function allows you to delete a single value from the database.
`key` is the value's key inside the database (see [write](#writing)) and must be a string or an integer. 

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
`key` is the key of the value you want to read (see [write](#writing)).

### get_many()
To read any value from the database, you need to use the `get_many(keys)` function.
`keys` is a list of the keys you want to read (see [write](#writing)).
