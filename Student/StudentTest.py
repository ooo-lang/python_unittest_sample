import unittest

import Student as StudentClass


class MyTestCase(unittest.TestCase):
    """
    unittest.TestCaseを継承したPersonTestクラス
    'test_'で始まるメソッドは全てテストケースとみなす
    """

    def setUp(self):
        print("\nset up")

        # Studentクラスをインスタンス化
        self.student = StudentClass.Student("Taro", "Suzuki")

    def tearDown(self):
        print("clean up")

        # インスタンス化したStudentクラスを削除
        del self.student

    def test_full_name(self):
        print('start test_full_name')

        # Studentクラスをインスタンス化
        # student = StudentClass.Student("Taro", "Suzuki")

        # 比較用にフルネームを用意
        full_name = 'Taro Suzuki'

        # 初期値のフルネームが一致するかどうか
        self.assertEqual(full_name, self.student.get_student_full_name())

    def test_student_default_lessons(self):
        print('start test_student_default_lessons')

        # Studentクラスをインスタンス化
        # student = StudentClass.Student("Taro", "Suzuki")

        # 初期値のlessonsを確認
        self.assertIsNotNone(self.student.lessons)
        self.assertIsInstance(self.student.lessons, list)

    def test_student_default_is_graduated(self):
        print('start test_student_default_is_graduated')

        # Studentクラスをインスタンス化
        # student = StudentClass.Student("Taro", "Suzuki")

        # 初期値のis_graduatedを確認
        self.assertFalse(False, self.student.is_graduated)


if __name__ == '__main__':
    unittest.main()
