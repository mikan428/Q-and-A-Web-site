from django.urls import path 
from  . import views

app_name='ampapp'
urlpatterns = [

    # ホームa
    path('',views.index,name="index"),

    # 問い合わせb
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),


    # 検索c
    path('search/', views.Search, name='search'),

   

    # リスト１
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    
    # path('diary-detail/<int:pk>/', DiaryDetailView.as_view(), name="diary_detail"),
    
    # 詳細２
    path('diary-detail/<int:pk>/<int:id>/', views.detailfunc, name="diary_detail"),
    # 質問作成３
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    # 回答作成４
    path('answer/<int:pk>/<int:id>/', views.AnView.as_view(), name="answer"),
    
    


    # リスト：ゲーム8
    path('game-list/', views.GameListView.as_view(), name="game_list"),

    # 詳細:ゲーム9
    path('game-detail/<int:pk>/<int:id>/', views.detailgame, name="game_detail"),

    # 質問作成:ゲーム10
    path('game-create/', views.GameCreateView.as_view(), name="game_create"),

    # 回答作成:ゲーム11
    path('game-answer/<int:pk>/<int:id>/', views.GameanView.as_view(), name="game_answer"),
    
    # リスト：学習14
    path('study-list/', views.StudyListView.as_view(), name="study_list"),
    
    # 詳細:学習15
    path('study-detail/<int:pk>/<int:id>/', views.detailstudy, name="study_detail"),

    # 質問作成:学習16
    path('study-create/', views.StudyCreateView.as_view(), name="study_create"),

    # 回答作成:学習17
    path('study-answer/<int:pk>/<int:id>/', views.StudyanView.as_view(), name="study_answer"),

  

    # リスト：科学20
    path('science-list/', views.ScienceListView.as_view(), name="science_list"),

    # 詳細:科学21
    path('science-detail/<int:pk>/<int:id>/', views.detailscience, name="science_detail"),

    # 質問作成:科学22
    path('science-create/', views.ScienceCreateView.as_view(), name="science_create"),

    # 回答作成:科学23
    path('science-answer/<int:pk>/<int:id>/', views.ScienceanView.as_view(), name="science_answer"),




    # リスト：タレント26
    path('talent-list/', views.TalentListView.as_view(), name="talent_list"),

    # 詳細:タレント27
    path('talent-detail/<int:pk>/<int:id>/', views.detailtalent, name="talent_detail"),

    # 質問作成:タレント28
    path('talent-create/', views.TalentCreateView.as_view(), name="talent_create"),

    # 回答作成:タレント29
    path('talent-answer/<int:pk>/<int:id>/', views.TalentanView.as_view(), name="talent_answer"),

   
    # リスト：将来32
    path('future-list/', views.FutureListView.as_view(), name="future_list"),

    # 詳細:将来33
    path('future-detail/<int:pk>/<int:id>/', views.detailfuture, name="future_detail"),

    # 質問作成:将来34
    path('future-create/', views.FutureCreateView.as_view(), name="future_create"),

    # 回答作成:将来35
    path('future-answer/<int:pk>/<int:id>/', views.FutureanView.as_view(), name="future_answer"),

    
    # リスト：健康38
    path('health-list/', views.HealthListView.as_view(), name="health_list"),

    # 詳細:健康39
    path('health-detail/<int:pk>/<int:id>/', views.detailhealth, name="health_detail"),

    # 質問作成:健康40
    path('health-create/', views.HealthCreateView.as_view(), name="health_create"),

    # 回答作成:健康41
    path('health-answer/<int:pk>/<int:id>/', views.HealthanView.as_view(), name="health_answer"),

   
    # リスト：人生44
    path('life-list/', views.LifeListView.as_view(), name="life_list"),

    # 詳細:人生45
    path('life-detail/<int:pk>/<int:id>/', views.detaillife, name="life_detail"),

    # 質問作成:人生46
    path('life-create/', views.LifeCreateView.as_view(), name="life_create"),

    # 回答作成:人生47
    path('life-answer/<int:pk>/<int:id>/', views.LifeanView.as_view(), name="life_answer"),

    
    # リスト：作品50
    path('work-list/', views.WorkListView.as_view(), name="work_list"),

    # 詳細:作品51
    path('work-detail/<int:pk>/<int:id>/', views.detailwork, name="work_detail"),

    # 質問作成:作品52
    path('work-create/', views.WorkCreateView.as_view(), name="work_create"),

    # 回答作成:作品53
    path('work-answer/<int:pk>/<int:id>/', views.WorkanView.as_view(), name="work_answer"),


    # リスト：オカルト56
    path('occult-list/', views.OccultListView.as_view(), name="occult_list"),

    # 詳細:オカルト57
    path('occult-detail/<int:pk>/<int:id>/', views.detailoccult, name="occult_detail"),

    # 質問作成:オカルト58
    path('occult-create/', views.OccultCreateView.as_view(), name="occult_create"),

    # 回答作成:オカルト59
    path('occult-answer/<int:pk>/<int:id>/', views.OccultanView.as_view(), name="occult_answer"),

    
    # リスト：趣味62
    path('hobby-list/', views.HobbyListView.as_view(), name="hobby_list"),

    # 詳細:趣味63
    path('hobby-detail/<int:pk>/<int:id>/', views.detailhobby, name="hobby_detail"),

    # 質問作成:趣味64
    path('hobby-create/', views.HobbyCreateView.as_view(), name="hobby_create"),

    
    # 回答作成:趣味65
    path('hobby-answer/<int:pk>/<int:id>/', views.HobbyanView.as_view(), name="hobby_answer"),

    # リスト：ネタ68
    path('joke-list/', views.JokeListView.as_view(), name="joke_list"),

    # 詳細:ネタ69
    path('joke-detail/<int:pk>/<int:id>/', views.detailjoke, name="joke_detail"),

    # 質問作成:ネタ70
    path('joke-create/', views.JokeCreateView.as_view(), name="joke_create"),

    # 回答作成:ネタ71
    path('joke-answer/<int:pk>/<int:id>/', views.JokeanView.as_view(), name="joke_answer"),

    






    













    









    

    


]
