from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary,Answer,GameQ,GameA,Studyq,Studya,Scienceq,Sciencea,Talentq,Talenta
from ..models import Futureq,Futurea,Healthq,Healtha,Lifeq,Lifea,Workq,Worka
from ..models import Occultq,Occulta,Hobbyq,Hobbya,Jokeq,Jokea
# class LoggedInTestCase(TestCase):
#     """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

#     def setUp(self):
#         """テストメソッド実行前の事前設定"""

#         # テストユーザーのパスワード
#         self.password = '<ログインパスワード>'

#         # 各インスタンスメソッドで使うテスト用ユーザーを生成し
#         # インスタンス変数に格納しておく
#         self.test_user = get_user_model().objects.create_user(
#             username='<ログインユーザー名>',
#             email='<ログインユーザーのメールアドレス>',
#             password=self.password)

#         # テスト用ユーザーでログインする
#         self.client.login(email=self.test_user.email, password=self.password)


class TestDiaryCreateView(TestCase):
    """DiaryCreateView用のテストクラス"""

    def test_create_diary_success(self):
        """質問処理が成功することを検証する"""

        # Postパラメータ
        params = {'title': 'テストタイトル',
                  'name':'名前',
                  'content': '本文',
                  'photo1': '',
                  'photo2': '',
                  'photo3': ''}

        # 新規質問作成処理(Post)を実行
        response = self.client.post(reverse_lazy('ampapp:diary_create'), params)

        # 質問リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('ampapp:diary_list'))

        # 質問データがDBに登録されたかを検証
        self.assertEqual(Diary.objects.filter(title='テストタイトル').count(), 1)

    def test_create_diary_failure(self):
        """新規質問作成処理が失敗することを検証する"""

        # 新規質問作成処理(Post)を実行
        response = self.client.post(reverse_lazy('ampapp:diary_create'))

        # 必須フォームフィールドが未入力によりエラーになることを検証
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')


# class TestDiaryUpdateView(LoggedInTestCase):
#     """DiaryUpdateView用のテストクラス"""

#     def test_update_diary_success(self):
#         """質問編集処理が成功することを検証する"""

#         # テスト用質問データの作成
#         diary = Diary.objects.create(user=self.test_user, title='タイトル編集前')

#         # Postパラメータ
#         params = {'title': 'タイトル編集後'}

#         # 質問編集処理(Post)を実行
#         response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk': diary.pk}), params)

#         # 質問詳細ページへのリダイレクトを検証
#         self.assertRedirects(response, reverse_lazy('diary:diary_detail', kwargs={'pk': diary.pk}))

#         # 質問データが編集されたかを検証
#         self.assertEqual(Diary.objects.get(pk=diary.pk).title, 'タイトル編集後')

#     def test_update_diary_failure(self):
#         """質問編集処理が失敗することを検証する"""

#         # 質問編集処理(Post)を実行
#         response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk': 999}))

#         # 存在しない質問データを編集しようとしてエラーになることを検証
#         self.assertEqual(response.status_code, 404)


# class TestDiaryDeleteView(LoggedInTestCase):
#     """DiaryDeleteView用のテストクラス"""

#     def test_delete_diary_success(self):
#         """質問削除処理が成功することを検証する"""

#         # テスト用質問データの作成
#         diary = Diary.objects.create(user=self.test_user, title='タイトル')

#         # 質問削除処理(Post)を実行
#         response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk': diary.pk}))

#         # 質問リストページへのリダイレクトを検証
#         self.assertRedirects(response, reverse_lazy('diary:diary_list'))

#         # 質問データが削除されたかを検証
#         self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 0)

#     def test_delete_diary_failure(self):
#         """質問削除処理が失敗することを検証する"""

#         # 質問削除処理(Post)を実行
#         response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk': 999}))

#         # 存在しない質問データを削除しようとしてエラーになることを検証
#         self.assertEqual(response.status_code, 404)
