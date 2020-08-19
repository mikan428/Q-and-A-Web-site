import logging
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView,FormView,CreateView,View

from .forms import InquiryForm,DiaryCreateForm,AnswerCreateForm,GameCreateForm,StudyCreateForm,ScienceCreateForm,TalentCreateForm
from .forms import FutureCreateForm,HealthCreateForm,LifeCreateForm,WorkCreateForm,OccultCreateForm,HobbyCreateForm,JokeCreateForm

from .models import Diary,Answer,GameQ,GameA
from .models import Studyq,Studya,Scienceq,Sciencea,Talentq,Talenta
from .models import Futureq,Futurea,Healthq,Healtha,Lifeq,Lifea,Workq,Worka
from .models import Occultq,Occulta,Hobbyq,Hobbya,Jokeq,Jokea

from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
# Create your views here. 
from django.http import HttpResponse, JsonResponse
from itertools import chain

#  追加 検索用
from django.contrib import messages
from django.db.models import Q
#  追加時間制限用
from django.utils import timezone
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

logger = logging.getLogger(__name__)

# ページネーション用に、Pageオブジェクトを返す。
def paginate_query(request, queryset, count):
  paginator = Paginator(queryset, count)
  page = request.GET.get('page')
  try:
    page_obj = paginator.page(page)
  except PageNotAnInteger:
    page_obj = paginator.page(1)
  except EmptyPage:
    page_obj = paginatot.page(paginator.num_pages)
  return page_obj



# ホーム部分a
def index(request):
    diary = Diary.objects.filter().order_by('-created_at')[:5]
    life = Lifeq.objects.all()
    params = {
        'diary':diary,
        'life':life,
    }
    return render(request, 'index.html', params)

# 問い合わせ部分b
class InquiryView(FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージ送った')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


# 検索c
def Search(request):
    blog = Diary.objects.order_by('-created_at')
    #   検索機能の処理 
    keyword = request.GET.get('keyword')
    if keyword:
        blog = blog.filter(
                 Q(content__icontains=keyword)
               )
        messages.success(request, '「{}」の検索結果'.format(keyword))
        return render(request, 'search.html', {'blog': blog })
    else:
    
         return render(request, 'index.html')



# diary_listの部分１
class DiaryListView(ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Diary.objects.all().order_by('-created_at')
        return diaries


#  詳細２
def detailfunc(request, pk,id):
    object = Diary.objects.get(pk=pk)
    obj = Diary.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'diary_detail.html', params)  

#  質問のフォーム部分3
class DiaryCreateView(CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    
    success_url = reverse_lazy('ampapp:diary_list')

   

    def form_valid(self, form):
        diary = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        diary.ip_address = client_addr 
        diary.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分4
class AnView(CreateView):
    
    model = Answer
    fields = ('name', 'content','photo1')
    template_name = 'answer.html'
 
    def form_valid(self, form):
        
        diary_id = self.kwargs['id']
        diary_pk = self.kwargs['pk']
        diary = get_object_or_404(Diary, pk=diary_pk)
        

        # 紐づく記事を設定する

        answer = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        answer.ip_address = client_addr 
        answer.diary = diary
        answer.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:diary_detail', pk=diary_pk,id=diary_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial



    
  


# リスト：ゲーム8
class GameListView(ListView):
    model = GameQ
    template_name = 'game_list.html'
    context_object_name = 'game_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = GameQ.objects.all().order_by('-created_at')
        return diaries
# 詳細: ゲーム9
def detailgame(request, pk,id):
    object = GameQ.objects.get(pk=pk)
    obj = GameQ.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'game_detail.html', params)  

#  質問のフォーム部分10
class GameCreateView(CreateView):
    model = GameQ
    template_name = 'game_create.html'
    form_class = GameCreateForm
    success_url = reverse_lazy('ampapp:game_list')

    def form_valid(self, form):
        gameq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        gameq.ip_address = client_addr 
        gameq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分11
class GameanView(CreateView):
    
    model = GameA
    fields = ('name','content','photo1')
    template_name = 'game_answer.html'
 
    def form_valid(self, form):
        

        game_id = self.kwargs['id']
        game_pk = self.kwargs['pk']
        game = get_object_or_404(GameQ, pk=game_pk)

        # 紐づく記事を設定する
        gameA = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        gameA.ip_address = client_addr 
        gameA.gameq = game
        gameA.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:game_detail', pk=game_pk,id=game_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial



# リスト：学習14
class StudyListView(ListView):
    model = Studyq
    template_name = 'study_list.html'
    context_object_name = 'study_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Studyq.objects.all().order_by('-created_at')
        return diaries

# 詳細: 学習15
def detailstudy(request, pk,id):
    object = Studyq.objects.get(pk=pk)
    obj = Studyq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=1) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'study_detail.html', params)  

#  質問のフォーム部分16
class StudyCreateView(CreateView):
    model = Studyq
    template_name = 'study_create.html'
    form_class = StudyCreateForm
    success_url = reverse_lazy('ampapp:study_list')

    def form_valid(self, form):
        studyq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        studyq.ip_address = client_addr 
        studyq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分:学習17
class StudyanView(CreateView):
    
    model = Studya
    fields = ('name' ,'content','photo1')
    template_name = 'study_answer.html'
 
    def form_valid(self, form):
        

        study_id = self.kwargs['id']
        study_pk = self.kwargs['pk']
        study = get_object_or_404(Studyq, pk=study_pk)

        # 紐づく記事を設定する
        studya = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        studya.ip_address = client_addr 
        studya.studyq = study
        studya.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:study_detail', pk=study_pk,id=study_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial


# リスト：科学20
class ScienceListView(ListView):
    model = Scienceq
    template_name = 'science_list.html'
    context_object_name = 'science_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Scienceq.objects.all().order_by('-created_at')
        return diaries

# 詳細: 科学21
def detailscience(request, pk,id):
    object = Scienceq.objects.get(pk=pk)
    obj = Scienceq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=1) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'science_detail.html', params)  

#  質問部分:科学22
class ScienceCreateView(CreateView):
    model = Scienceq
    template_name = 'science_create.html'
    form_class = ScienceCreateForm
    success_url = reverse_lazy('ampapp:science_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr 
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)


#  回答作成部分:科学23
class ScienceanView(CreateView):
    
    model = Sciencea
    fields = ('name', 'content','photo1')
    template_name = 'science_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Scienceq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr 
        sciencea.scienceq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:science_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial


# リスト：タレント26
class TalentListView(ListView):
    model = Talentq
    template_name = 'talent_list.html'
    context_object_name = 'talent_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Talentq.objects.all().order_by('-created_at')
        return diaries

# 詳細: タレント27
def detailtalent(request, pk,id):
    object = Talentq.objects.get(pk=pk)
    obj = Talentq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'talent_detail.html', params)  

#  質問部分:タレント28
class TalentCreateView(CreateView):
    model = Talentq
    template_name = 'talent_create.html'
    form_class = TalentCreateForm
    success_url = reverse_lazy('ampapp:talent_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr 
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分:タレント29
class TalentanView(CreateView):
    
    model = Talenta
    fields = ( 'name','content','photo1')
    template_name = 'talent_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Talentq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr 
        sciencea.talentq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:talent_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial



# リスト：将来33
class FutureListView(ListView):
    model = Futureq
    template_name = 'future_list.html'
    context_object_name = 'future_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Futureq.objects.all().order_by('-created_at')
        return diaries

# 詳細: 将来34
def detailfuture(request, pk,id):
    object = Futureq.objects.get(pk=pk)
    obj = Futureq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'future_detail.html', params)  

#  質問部分:将来34
class FutureCreateView(CreateView):
    model = Futureq
    template_name = 'future_create.html'
    form_class = FutureCreateForm
    success_url = reverse_lazy('ampapp:future_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr 
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分:将来35
class FutureanView(CreateView):
    
    model = Futurea
    fields = ( 'name','content','photo1')
    template_name = 'future_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Futureq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr 
        sciencea.futureq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:future_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial



# リスト：健康38
class HealthListView(ListView):
    model = Healthq
    template_name = 'health_list.html'
    context_object_name = 'health_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Healthq.objects.all().order_by('-created_at')
        return diaries

# 詳細: 健康39
def detailhealth(request, pk,id):
    object = Healthq.objects.get(pk=pk)
    obj =  Healthq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'health_detail.html', params)  

#  質問部分:健康40
class  HealthCreateView(CreateView):
    model =  Healthq
    template_name = 'health_create.html'
    form_class =  HealthCreateForm
    success_url = reverse_lazy('ampapp:health_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分:健康41
class HealthanView(CreateView):
    
    model = Healtha
    fields = ( 'name','content','photo1')
    template_name = 'health_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Healthq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr
        sciencea.healthq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:health_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial



# リスト：人生44
class LifeListView(ListView):
    model = Lifeq
    template_name = 'life_list.html'
    context_object_name = 'life_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Lifeq.objects.all().order_by('-created_at')
        return diaries

# 詳細: 人生45
def detaillife(request, pk,id):
    object = Lifeq.objects.get(pk=pk)
    obj = Lifeq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'life_detail.html', params)  

#  質問部分:人生46
class LifeCreateView(CreateView):
    model = Lifeq
    template_name = 'life_create.html'
    form_class = LifeCreateForm
    success_url = reverse_lazy('ampapp:life_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr 
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)


#  回答作成部分:人生47
class LifeanView(CreateView):
    
    model = Lifea
    fields = ('name', 'content','photo1')
    template_name = 'life_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Lifeq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr 
        sciencea.lifeq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:life_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial




# リスト：作品50
class WorkListView(ListView):
    model = Workq
    template_name = 'work_list.html'
    context_object_name = 'work_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Workq.objects.all().order_by('-created_at')
        return diaries

# 詳細: 作品51
def detailwork(request, pk,id):
    object = Workq.objects.get(pk=pk)
    obj =  Workq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'work_detail.html', params)  

#  質問部分:作品52
class  WorkCreateView(CreateView):
    model =  Workq
    template_name = 'work_create.html'
    form_class =  WorkCreateForm
    success_url = reverse_lazy('ampapp:work_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr 
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)
    
#  回答作成部分:作品53
class WorkanView(CreateView):
    
    model = Worka
    fields = ( 'name','content','photo1')
    template_name = 'work_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Workq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr 
        sciencea.workq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:work_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial



# リスト：オカルト56
class OccultListView(ListView):
    model = Occultq
    template_name = 'occult_list.html'
    context_object_name = 'occult_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Occultq.objects.all().order_by('-created_at')
        return diaries

# 詳細: オカルト57
def detailoccult(request, pk,id):
    object = Occultq.objects.get(pk=pk)
    obj =  Occultq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'occult_detail.html', params)  

#  質問部分:オカルト58
class  OccultCreateView(CreateView):
    model =  Occultq
    template_name = 'occult_create.html'
    form_class =  OccultCreateForm
    success_url = reverse_lazy('ampapp:occult_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr 
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分:オカルト59
class OccultanView(CreateView):
    
    model = Occulta
    fields = ( 'name','content','photo1')
    template_name = 'occult_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Occultq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr 
        sciencea.occultq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:occult_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial
    




# リスト：趣味62
class HobbyListView(ListView):
    model = Hobbyq
    template_name = 'hobby_list.html'
    context_object_name = 'hobby_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Hobbyq.objects.all().order_by('-created_at')
        return diaries

# 詳細: 趣味63
def detailhobby(request, pk,id):
    object = Hobbyq.objects.get(pk=pk)
    obj =  Hobbyq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'hobby_detail.html', params)  

#  質問部分:趣味64
class  HobbyCreateView(CreateView):
    model =  Hobbyq
    template_name = 'hobby_create.html'
    form_class =  HobbyCreateForm
    success_url = reverse_lazy('ampapp:hobby_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr 
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)
    
#  回答作成部分:趣味65
class HobbyanView(CreateView):
    
    model = Hobbya
    fields = ('name', 'content','photo1')
    template_name = 'hobby_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Hobbyq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr 
        sciencea.hobbyq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:hobby_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial



# リスト：ネタ68
class JokeListView(ListView):
    model = Jokeq
    template_name = 'joke_list.html'
    context_object_name = 'joke_list'
    paginate_by = 10
    

    def get_queryset(self):
        diaries = Jokeq.objects.all().order_by('-created_at')
        return diaries

# 詳細: ネタ69
def detailjoke(request, pk,id):
    object = Jokeq.objects.get(pk=pk)
    obj =  Jokeq.objects.get(id=id)
    check = timezone.now() - datetime.timedelta(weeks=3) < obj.created_at
    params = {
        'object':object,
        'check':check,
    }
    return render(request, 'joke_detail.html', params)  

#  質問部分:ネタ70
class  JokeCreateView(CreateView):
    model =  Hobbyq
    template_name = 'joke_create.html'
    form_class =  JokeCreateForm
    success_url = reverse_lazy('ampapp:joke_list')

    def form_valid(self, form):
        scienceq = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        scienceq.ip_address = client_addr
        scienceq.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)

#  回答作成部分:ネタ71
class JokeanView(CreateView):
    
    model = Jokea
    fields = ( 'name','content','photo1')
    template_name = 'joke_answer.html'
 
    def form_valid(self, form):
        

        science_id = self.kwargs['id']
        science_pk = self.kwargs['pk']
        science = get_object_or_404(Jokeq, pk=science_pk)

        # 紐づく記事を設定する
        sciencea = form.save(commit=False)
        client_addr =self.request.META.get('REMOTE_ADDR')
        sciencea.ip_address = client_addr
        sciencea.jokeq = science
        sciencea.save()
        
        # 記事詳細にリダイレクト
        return redirect('ampapp:joke_detail', pk=science_pk,id=science_id)
    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = '名無し'   #testモデルのuserを初期値としてセット
        return initial
    






    

    



    
