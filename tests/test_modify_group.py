from models.group import Group
import pytest
test_groups=[
    Group(name="ggg", header="hhh", footer="gggr"),
    Group(name="45", header="th", footer="gh")
]

@pytest.mark.parametrize("index", [0,-1], ids=["first", "last"])
@pytest.mark.parametrize("data_to_modify", test_groups, ids=["groups_with_letters", "groups_with_digits"])

def test_modify_by_number(app, init_group, init_login, data_to_modify, index):
    data_to_modify=Group(name="arr")
    app.group.open_group_page()
    old_groups = app.group.get_list()
    app.group.modify_by_number(0, data_to_modify)
    assert "Group has been ..." in app.find_message()
    app.group.return_to_group_page()
    new_groups = app.group.get_list()
    modified_group = old_groups[0]
    if data_to_modify.name is not None:
        old_groups[0].name=data_to_modify.name
    assert (len(old_groups) == len(new_groups))
    assert sorted(new_groups) == sorted(old_groups)
