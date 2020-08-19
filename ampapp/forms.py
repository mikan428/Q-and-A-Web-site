from django import forms
from django.core.mail import EmailMessage
from .models import Diary ,Answer,GameQ,Studyq,Scienceq,Talentq,Futureq,Healthq,Lifeq,Workq,Occultq,Hobbyq,Jokeq

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'
 
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()

class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        self.fields['title'].initial = 'ak'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AnswerCreateForm(forms.ModelForm):

     class Meta:
        
        model = Answer
        fields = ('content', 'photo1', 'photo2', 'photo3',)
    
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = GameQ
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class StudyCreateForm(forms.ModelForm):
    class Meta:
        model = Studyq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ScienceCreateForm(forms.ModelForm):
    class Meta:
        model = Scienceq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class TalentCreateForm(forms.ModelForm):
    class Meta:
        model = Talentq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class FutureCreateForm(forms.ModelForm):
    class Meta:
        model = Futureq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class HealthCreateForm(forms.ModelForm):
    class Meta:
        model = Healthq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LifeCreateForm(forms.ModelForm):
    class Meta:
        model = Lifeq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class WorkCreateForm(forms.ModelForm):
    class Meta:
        model = Workq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class OccultCreateForm(forms.ModelForm):
    class Meta:
        model = Occultq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class HobbyCreateForm(forms.ModelForm):
    class Meta:
        model = Hobbyq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class JokeCreateForm(forms.ModelForm):
    class Meta:
        model = Jokeq
        fields = ('name','title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = '名無し'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



  