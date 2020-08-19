from accounts.models import CustomUser
from django.db import models

# Create your models here.

class Diary(models.Model):
    """質問モデル"""
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)  
    
    class Meta:
         verbose_name_plural = 'Diary'
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    """質問回答"""
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文')
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Answer'
    
    def __str__(self):
        return self.content


# ゲーム質問
class GameQ(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文')
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)  
    class Meta:
         verbose_name_plural = 'GameQ'
    
    def __str__(self):
        return self.title

# ゲーム回答
class GameA(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文')
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    gameq = models.ForeignKey(GameQ, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'GameA'
    
    def __str__(self):
        return self.content



# 学習質問
class Studyq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
   
    class Meta:
         verbose_name_plural = 'Studyq'
    
    def __str__(self):
        return self.title

# 学習回答
class Studya(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    studyq = models.ForeignKey(Studyq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Studya'
    
    def __str__(self):
        return self.content




# 科学質問
class Scienceq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Scienceq'
    
    def __str__(self):
        return self.title

# 科学回答
class Sciencea(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    scienceq = models.ForeignKey(Scienceq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Sciencea'
    
    def __str__(self):
        return self.content


# 質問:タレント
class Talentq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
   
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Talentq'
    
    def __str__(self):
        return self.title

# 回答:タレント
class Talenta(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    talentq = models.ForeignKey(Talentq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Talenta'
    
    def __str__(self):
        return self.content



# 質問:将来
class Futureq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Futureq'
    
    def __str__(self):
        return self.title

# 回答:将来
class Futurea(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    futureq = models.ForeignKey(Futureq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Futurea'
    
    def __str__(self):
        return self.content



# 質問:健康
class Healthq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Healthq'
    
    def __str__(self):
        return self.title

# 回答:健康
class Healtha(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    healthq = models.ForeignKey(Healthq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Healtha'
    
    def __str__(self):
        return self.content



# 質問:人生
class Lifeq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Lifeq'
    
    def __str__(self):
        return self.title

# 回答:人生
class Lifea(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    lifeq = models.ForeignKey(Lifeq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Lifea'
    
    def __str__(self):
        return self.content



# 質問:作品
class Workq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Workq'
    
    def __str__(self):
        return self.title

# 回答:作品
class Worka(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    workq = models.ForeignKey(Workq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Worka'
    
    def __str__(self):
        return self.content



# 質問:オカルト
class Occultq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Occultq'
    
    def __str__(self):
        return self.title

# 回答:オカルト
class Occulta(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    occultq = models.ForeignKey(Occultq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Occulta'
    
    def __str__(self):
        return self.content



# 質問:趣味
class Hobbyq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Hobbyq'
    
    def __str__(self):
        return self.title

# 回答:趣味
class Hobbya(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文',null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    hobbyq = models.ForeignKey(Hobbyq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Hobbya'
    
    def __str__(self):
        return self.content




# 質問:ネタ
class Jokeq(models.Model):
    
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文',  null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Jokeq'
    
    def __str__(self):
        return self.title

# 回答:趣味
class Jokea(models.Model):
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT,null=True)
    name = models.CharField(verbose_name='名前', max_length=40)
    content = models.TextField(verbose_name='本文', null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True,null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    jokeq = models.ForeignKey(Jokeq, on_delete=models.CASCADE,null=True)
    read =  models.IntegerField(null=True, blank=True, default=0)
    
    best =  models.IntegerField(null=True, blank=True, default=0)
    
    ip_address = models.CharField('IPアドレス', max_length=20)
    class Meta:
         verbose_name_plural = 'Jokea'
    
    def __str__(self):
        return self.content






