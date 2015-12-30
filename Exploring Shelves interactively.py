import shelve

db = shelve.open('persondb')  # Reopen the shelve

len(db)  # Three 'records' stored

list(db.keys())  # keys is th index

bob = db['Bob Smith']  # Fetch bob by key

print(bob)  # Runs __str__from AttrDisplay

bob.lastName()  # Runs lastName from Person

for key in db:  # Iterate, fetch, print
    print(key, '=>', db[key])

for key in sorted(db):
    print(key, '=>', db[key])

"""
Notice that we don`t have to import our Person or Manager classes
here in order to load or use our stored objects
"""