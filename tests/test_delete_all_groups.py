import pytest
import random

@pytest.fixture(params=[0, "random", -1], ids=["first", "random", "last"])
def index(app, request):
    if request.param=="random":
        return random.randrange(1, app.group.count())
    return request.param

def test_delete_all_groups(app, init_login, init_group, index):
    app.group.open_group_page()
    total_groups=app.group.count()
    while total_groups != 0:
        app.group.delete_by_number(index)
        assert "Group has been removed." in app.find_message()
        app.group.return_to_group_page()