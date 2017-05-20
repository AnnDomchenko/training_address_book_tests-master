import pytest
from web_api.addressbook_api import AddressBookAPI
from models.group import Group
from models.contacts import Contact
import random
import json
import os.path
from data.test_groups import test_groups
from db_api.addressbook_orm import AddressbookORM

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store",default="config.json")

@pytest.fixture(scope="session")
def config(request):
    file_name=request.config.getoption("--config")
    file_name=os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def app(request, config):
    browser = request.config.getoption("--browser")
    addr_api = AddressBookAPI(browser=browser, base_url=config['web']["base_url"])
    yield addr_api
    addr_api.destroy()

@pytest.fixture(scope="session")
def db(config):
    dbfixture=AddressbookORM(**config['db'])
    yield dbfixture
    # dbfixture.destroy()


@pytest.fixture(scope="session")
def init_login(app, config):
    app.session.login(username=config['web']["username"], password=config['web']["password"])
    yield
    app.session.logout()

@pytest.fixture
def init_group(app, init_login):
    if not app.group.is_element_present:
        test_group = Group(name="test name")
        app.group.create(test_group)


# def random_string(maxlen):
#     length=random.randrange(maxlen)
#     symbols=string.ascii_letters+string.digits+" " #+string.punctuation
#     return "".join([random.choice(symbols) for _ in range(length)])
#
# names=["", "jjj", "789"]
# headers=["", "jjj", "789"]
# footers=["", "jjj", "789"]

# test_groups=[
#     Group(name=random.string(20), header=random.string(50), footer=random.string(50))
#     #for name in names
#     #for footer in footers
#     #for header in headers
# ]

@pytest.fixture(params=[0, "random", -1], ids=["first", "random in middle", "last"])
def index(request, app):
    if request.param == "random":
        return random.randrange(1, app.group.count()-1)
    return request.param

@pytest.fixture(params=test_groups, ids=[repr(g)for g in test_groups])
def test_group(request):
    return request.param

