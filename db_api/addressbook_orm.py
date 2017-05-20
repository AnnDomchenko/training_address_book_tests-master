from pony.orm import *
from datetime import datetime
from pymysql.converters import conversions
from models.group import Group
from models.contacts import Contact

class AddressbookORM:

    db=Database()

    class GroupORM(db.Entity):
        _table_="group_list"
        id=PrimaryKey(int,column="group_id")
        name=Optional(str, column="group_name")
        header=Optional(str, column="group_header")
        footer=Optional(str, column="group_footer")
        contacts=Set('ContactORM', table="address_in_groups", column='id', reverse='groups', lazy=True)

        def get_model(self):
            return Group(id=self.id, name=self.name, header=self.header, footer=self.footer)


    class ContactORM(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int)
        firstname = Optional(str)
        lastname = Optional(str)
        middlename = Optional(str)
        deprecated = Optional(datetime)
        groups=Set('GroupORM', table="address_in_groups", column='group_id', reverse='contacts', lazy=True)

        def get_model(self):
            return Contact(id=self.id, firstname=self.firstname, lastname=self.lastname, middlename=self.middlename)

    def __init__(self, host, port, user, password, db):
        self.db.bind('mysql', host=host, port=port, user=user, password=password, db=db, charset='utf8', conv=conversions)
        self.db.generate_mapping()
        # sql_debug(True)

    @db_session
    def get_contact_list(self):
        query = select(c for c in self.ContactORM if c.deprecated is None)
        return [c.get_model() for c in query]

    @db_session
    def get_group_list(self):
        query = select(n for n in self.GroupORM)
        return [n.get_model() for n in query]

    @db_session
    def get_contacts_in_group(self, group):
        dbgroup=select(g for g in self.GroupORM if g.id==group.id).first()
        return [c.get_model() for c in dbgroup.contacts]


    # @db_session
    # def get_contact_list(self):
    #     select(g for g in self.ContactORM if g.deprecated)

