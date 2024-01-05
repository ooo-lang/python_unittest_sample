import unittest

# テスト対象クラスのためインポートする必要がある
import Persons as PersonsClass


class PersonsTest(unittest.TestCase):
    """
    unittest.TestCaseを継承したPersonTestクラス
    'test_'で始まるメソッドは全てテストケースとみなす
    """

    persons = PersonsClass.Persons()  # Personクラスのインスタンス化
    user_id = []  # 取得したuser_idを格納する変数
    user_name = []  # user_nameを格納する変数

    # Person.set_nameメソッドをチェックするテストケース
    def test_0_set_name(self):
        print("\nStart set_name test\n")
        for i in range(4):
            # nameの生成
            name = 'name' + str(i)
            # 比較用に別でユーザー名をlistに格納して取っておく
            self.user_name.append(name)

            # Persons.set_nameを呼び出して、ユーザー名をセット
            user_id = self.persons.set_name(name)

            # user_idがNoneではないかチェック
            self.assertIsNotNone(user_id)

            # user_idを別でlistに格納して取っておく
            self.user_id.append(user_id)

        # 確認用
        print("user_id length = ", len(self.user_id))
        print(self.user_id)
        print("user_name length = ", len(self.user_name))
        print(self.user_name)
        print("\nFinish set_name test\n")

    # Person.get_nameメソッドをチェックするテストケース
    def test_1_get_name(self):
        print("\nStart get_name test\n")

        length = len(self.user_id)  # ユーザー登録情報の合計
        print("user_id length = ", length)
        print("user_name length = ", len(self.user_name))
        for i in range(6):
            # user_idの合計以下の場合は、そのuser_idに基づいたuser_nameを返す
            if i < length:
                # user_nameに登録した名前と一致するか
                self.assertEqual(self.user_name[i], self.persons.get_name(self.user_id[i]))
            else:
                print("Testing for get_name no user test")
                # もし、合計数を超えた場合に指定されたメッセージが返されるか
                self.assertEqual('There is no such user', self.persons.get_name(i))
        print("\nFinish get_name test\n")

    def test_2_del_name(self):
        print("\nStart del_name test\n")

        print("user_id length = ", len(self.user_id))
        print("user_name length = ", len(self.user_name))

        print("user_id：", self.user_id)
        print("user_name：", self.user_name)

        # 削除するユーザーのIDを指定
        within_range_index = 2

        # persons.del_name()を呼出
        within_range_del_result = self.persons.del_name(self.user_name[within_range_index])

        # 戻り値がNoneではないか
        self.assertIsNotNone(within_range_del_result)

        # 該当するユーザーIDの名前が削除成功しているかどうか
        self.assertTrue(within_range_del_result)

        # user_idとuser_nameからも削除
        self.user_id.remove(within_range_index)
        self.user_name.remove(self.user_name[within_range_index])

        print("user_id length = ", len(self.user_id))
        print("user_name length = ", len(self.user_name))

        print("user_id：", self.user_id)
        print("user_name：", self.user_name)

        # ～ 存在しないnameでもテスト ～


if __name__ == '__main__':
    unittest.main()
