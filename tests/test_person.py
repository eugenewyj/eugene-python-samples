# -*- coding: utf-8 -*-

from .context import sample

import unittest


class BasicTestSuite(unittest.TestCase):
    """基础测试样例"""

    @staticmethod
    def test_person_show_age():
        tk = sample.person.Person('TK', 'tk@mail.com')
        print(tk._email)
        assert 'tk@mail.com' == tk._email


if __name__ == '__main__':
    unittest.main()

