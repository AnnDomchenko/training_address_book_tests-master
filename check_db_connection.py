from db_api.addressbook_orm import AddressbookORM
from models.group import Group
from models.contacts import Contact


config={
    "host":"localhost",
    "port": 8889,
    "user":"root",
    "password":"root",
    "db":"test"
}

db=AddressbookORM(**config)

try:
    l=db.get_contacts_in_group(Group(id='34'))
    for c in l:
        print(c)
    print(len(l))
finally:
    pass