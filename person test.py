from person import Person

bob = Person('Bob Smith')  # Show bob`s __str__
print(bob)

print(bob.__class__)  # Show bob`s class and its name
print(bob.__class__.__name__)

list(bob.__dictc__.keys())  # Attributes are really dict keys. Use list to force lists in 3.0

for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])  # Index manually

for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))  # obj.attr, but attr is a var
