from unittest import TestCase
from yex import Yex


class TestString(TestCase):
    def setUp(self):
        self.tpl = 'key: {{value}}'
        self.content = 'key: 42'
        self.data = {'value': 42}
        self.res = {'key': 42}

    def test_call(self):
        res = Yex(self.tpl)(self.data)
        self.assertEqual(res, self.res, 'Render by call instance')

    def test_lt(self):
        res = self.data > Yex(self.tpl)
        self.assertEqual(res, self.res, 'Render by lt')

    def test_render(self):
        res = Yex(self.tpl).render(self.data)
        self.assertEqual(res, self.res, 'Render common')

    def test_content(self):
        res = Yex(self.tpl).render_content(self.data)
        self.assertEqual(res, self.content, 'Render content')
