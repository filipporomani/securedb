<h1>securedb</h1>

[![Downloads](https://static.pepy.tech/personalized-badge/securedb?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pypi.org/project/securedb) [![PyPi version](https://badgen.net/pypi/v/securedb/)](https://pypi.org/project/securedb) [![PyPI status](https://img.shields.io/pypi/status/securedb.svg)](https://pypi.python.org/pypi/securedb/)


## securedb is a lightweight Python database framework to handle basic key-value encrypted data.
## `pip install securedb --upgrade`


## Content index

- [Changelog](#changelog)
  - [New in 2.0.2 (Latest)](#new-in-202-latest)
  - [New in 2.0.1](#new-in-201)
  - [New in 2.0.0](#new-in-200)
  - [New in 1.1.0](#new-in-110)
- [Documentation](#documentation)
  - [DB Creation](#db-creation)
    - [Key](#key)
    - [Initialization](#initialization)
  - [Writing keys](#writing-keys)
    - [write()](#write)
    - [write\_many()](#write_many)
  - [Deleting](#deleting)
    - [delete()](#delete)
    - [delete\_many()](#delete_many)
    - [clear()](#clear)
  - [Reading](#reading)
    - [get()](#get)
    - [get\_many()](#get_many)


# Changelog

## New in 2.0.2 (Latest)
-  Bugfix in the get_many() function
-  Pep8 compliant
-  Fixes in the docs
## New in 2.0.1
-  Fixed docs missing initialization instructions

## New in 2.0.0
-  Completely redesigned db schema, now using single files for each database key
-  Maximum database storage size heavily increased
-  Lower memory consumption
-  Mapped every possible error
-  Custom key file path

## New in 1.1.0
-  `force` kwarg added in the initialization; see [initialization](#Initialization)
-  You don't need to manually encode the key during the initialization
-  If there is no error, all the functions now return `True`
-  Useless print() functions were removed
-  Smoother error handling


# Documentation



## DB Creation
### Key
To create a database, an encryption key is needed. To generate it, you can use the built-in `newkey()` function.
```py
import securedb
securedb.newkey(keyfile="path/to/key/storage") # the "keyfile" kwarg is optional and default set to ".key".
```
This will create a new file: it'll be named ".key" if no `keyfile` is specified, else it'll be named as you want.
The key file is the file which contains the encryption key.



### Initialization
```py
import securedb

db = securedb.Db(db_path, path_to_key, force=True)
# path is the database storage location, key is the path to the key file and force is described below.
```
With `force=True` the program will create a new db in the given path if no database is found. `force` is optional and default set to `False`.
Remember that if you lost your key there will be no way to recover the database content.



## Writing keys
### write()
The `write(key, value)` function allows you to insert a single value into the database.
`key` is the value name
`value` is the value data.

`key` is used to access the data, and must be an integer or a string;
`value` can be anything such as boolean, integer, string, array, list, dictionary ecc.

### write_many()
The `write_many(payload)` function allows you to write many values in a single time. 
`payload` is a dictionary with all the values you need to insert:
`{key: value, key1: value1, key2: value2}` etc.
There isn't any limit regarding the size of the payload. For perfomance reasons, we suggest you to use payloads with a maximum size of 5mb, even if there is no software limit.



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
