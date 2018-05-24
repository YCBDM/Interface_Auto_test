import sys
import random
import pytest

sys.path.append("../..")
from util.case import Case

case = Case()


def setup_module(module):
    case.http.set_env('dev')
    case.load_data('test_user_data.xlsx')


def test_user_login_normal():
    case.run()


def test_user_login_not_exists():
    case.run()


def test_user_login_passwd_wrong():
    case.run()


def test_user_reg_random_name():
    random_name = random.choice(['E', 'V', 'O', 'Y', 'C', 'Z', 'D', 'M', 'L']) + chr(random.randint(0x4e00, 0x9fbf))
    case.run({"random_name": random_name})
    case.check_db('checkUserPassword', {"name": random_name, "password": "e10adc3949ba59abbe56e057f20f883e"})


if __name__ == '__main__':
    pytest.main(["-q", "test_user.py"])
