import pymysql
from models.group import Group
from models.contacts import Contact

class AddressBookDB:
    def __init__(self, host, port, user, password, db):
        self.connection=pymysql.connect(host=host, port=port, user=user,password=password, db=db, charset='utf8')

    def get_group_list(self):
        with self.connection.cursor() as cursor:
            sql="SELECT group_id, group_name, group_header, group_footer FROM group_list;"
            cursor.execute(sql)
            group_list = []
            for row in cursor:
                group_list.append(Group(id=row[0], name=row[1], header=row[2], footer=row[3]))
        self.connection.commit()
        return group_list

    def get_contact_list(self):
        with self.connection.cursor() as cursor:
            sql="SELECT firstname, middlename, lastname FROM addressbook;"
            cursor.execute(sql)
            contact_list = []
            for row in cursor:
                contact_list.append(Contact(firstname=row[0], secondname=row[1], lastname=row[2]))
        self.connection.commit()
        return contact_list


    def destroy(self):
        self.connection.close()

