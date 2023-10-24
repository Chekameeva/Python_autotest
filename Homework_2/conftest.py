import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def add_post_selector():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def add_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def add_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def add_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def save_post():
    # return """//*[@id="create-item"]/div/div/div[7]/div/button/div"""
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def check_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def title_name():
    return f"{testdata['title']}"