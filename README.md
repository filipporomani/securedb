# securedb

## securedb is a Python framework that lets you work with encrypted JSON databases.
Features: 
- newkey() to generate an encryption key
- write(key, value) to write a determinated value into the database
- clear() to nuke the database
- get(key) to get a determinated key from the database
- write_many(dict) to write an undefined amount of keys to the database.
- delete_many(list) to delete an undefined amount of keys from the database

## WARNING!! IF YOU LOST YOUR ENCRYPTION KEY, THE WHOLE DATABASE DATA WILL BE LOST! THERE'S NO WAY TO RECOVER A LOST KEY!
