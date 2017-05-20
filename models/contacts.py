class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None):
        self.id=id
        self.firstname = firstname
        self.middlename=middlename
        self.lastname=lastname

    def __repr__(self):
        return "id: {}, {}, {}, {}".format(self.id, self.firstname, self.middlename, self.lastname)