def test_group_list(app, init_login, db):
    app.group.open_group_page()
    ui_group_list = app.group.get_list()
    db_group_list = db.get_group_list()
    assert sorted(ui_group_list) == sorted(db_group_list)