import pytest

def test_delete_contact(app, init_login, init_group, index):
    app.contact.open_contact_page()
    old_contact_list = app.contact.count_c()
    app.contact.delete_contact_by_number(index)
    assert "Record successful deleted." in app.find_message()
    app.contact.open_contact_page()
    # Verifying Deletion group in list
    new_contact_list = app.contact.count_c()
    assert len(old_contact_list)-1 == len(new_contact_list)
    old_contact_list.pop(index)
    assert old_contact_list == new_contact_list
