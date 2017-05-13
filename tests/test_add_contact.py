from models.contacts import Contact

def test_add_contact(app, init_login, test_contact):
    test_contact = Contact(address="contact_address")
    old_contacts = app.contact.count_c()
    app.contact.create_contact(test_contact)
    assert "Information entered into into address book." in app.find_message()
    app.contact.open_contact_page()
    new_contacts=app.contact.count_c()
    assert len(old_contacts)== len(new_contacts)-1
    old_contacts.append(test_contact)
    assert sorted(old_contacts)==sorted(new_contacts)






