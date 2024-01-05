import unittest


class MyTestCase(unittest.TestCase):
    def test_a_and_b(self):
        a = 1
        b = 1
        self.assertEqual(a, b, 'a and b are not equal')

    def test_is_str(self):
        a = '1'
        self.assertTrue(type(a) is str, 'a is not str')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # s.split(2)で空白数の違う値を指定するとTypeErrorが発生するか確認
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
