import pytest
import random

# @pytest.fixture(params=[0, "random", -1], ids=["first", "random", "last"])
# def index(app, request):
#     if request.param=="random":
#         return random.randrange(1, app.group.count())
#     return request.param

def test_delete_all_groups(app):
    app.group.open_group_page()
    total_groups=app.group.count()
    app.group.delete_groups()
    assert total_groups is None
