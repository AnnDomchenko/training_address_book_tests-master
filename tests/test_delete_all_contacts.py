import pytest

def test_delete_all_contacts(app):
    app.contact.open_contact_page()
    total_contacts = app.contact.count_c()
    app.contact.delete_all_contacts()
    assert total_contacts is None


