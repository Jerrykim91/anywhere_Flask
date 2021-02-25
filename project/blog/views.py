from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# 로그인
# from django.contrib.auth.decorators import login_required

# 1. 클래스형 제네릭뷰
from django.views.generic import ListView, DetailView  
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

# 2-1. 테이블 조회를 위한 모델 임포트
# from blog.models import Post, Category
from blog.models import Post, PhotoArt
# 2-2. 템플릿 뷰
from django.views.generic import TemplateView

# 3. comment
from django.conf import settings

# 4. search
from django.views.generic import FormView
from blog.forms import PostSearchForm 
from blog.forms import PostForm, PostEdit

from django.db.models import Q
from django.shortcuts import render  # render : 위에 제거하고 다시 작성

# 6. App Extend 
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin # login_required 기능 
from django.urls import reverse_lazy
from django.views import OwnerOnlyMixin


# Create your views here.

"""
# slug
https://cedo.tistory.com/43
https://djangopy.org/how-to/how-to-implement-categories-in-django/#conclusion
https://pjs21s.github.io/category-recursive/
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

# class addCategoryView(LoginRequiredMixin,CreateView):
#     model       = Category
#     template_name = 'blog/category.html'
#     fields = '__all__'



# def CategoryView(request, cats):
#     """
#     함수 사용 
#     """
#     category_posts = Post.objects.filter(category=cats.replace('-',' '))

#     return render(request,"blog/categories.html",{'cats':cats.title().replace('-',' '),'category_posts':category_posts})

#ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5  # 한페이지에 보여주는 객체 리스트의 개수


class AboutDV(TemplateView):
    """
    포트 폴리오
    """
    model = Post
    template_name = 'blog/post_about_me.html'

    # def get_context_data(self, **kwargs):
    #     context = super(indexView, self).get_context_data(**kwargs)
    #     return context


# DetailView
class PostDV(DetailView):
    model = Post
    img_posts = PhotoArt.objects.filter()

    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id']    = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url']   = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}" #ex)http://127.0.0.1:8000/blog/post/99
        context['disqus_title'] = f"{self.object.slug}"
        return context


# ArchiveView
class PostAV(ArchiveIndexView):
    """
    Archive
    """
    model = Post
    date_field = 'modify_dt'

# App Extend
class PostCreateView(LoginRequiredMixin,CreateView):
    # model          = Post # 생략가능 
    form_class     = PostForm
    template_name  = 'blog/post_form.html'
    success_url    = reverse_lazy('blog:index') # redirect

    # form(원본)
    # category_queryset = Category.objects.all().values_list('name','name')
    # fields         = ['category','title', 'slug','description','content','tags'] # 모델에서 가져 올 필드명 작성
    # initial        = {'slug':'Auto-Filling-Do-Not-input' }
    # widgets = {
    #         'category' :
    #             }

    def form_valid(self, form):  # 폼에 이상이 없으면 실행.
        form.instance.owner = self.request.user
        return super().form_valid(form)



class PostChangeLV(LoginRequiredMixin,ListView):
    model         = Post
    template_name = 'blog/post_change_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(OwnerOnlyMixin,UpdateView):
    model       = Post # 생략하면 에러 발생  : django.core.exceptions.ImproperlyConfigured 'someting'is missing a QuerySet.
    form_class  = PostEdit
    # fields      = ['category','title','slug','description','content','tags']
    success_url = reverse_lazy('blog:index') # redirect
    # template_name = 'blog/post_form.html'

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model         = Post
    success_url   = reverse_lazy('blog:index') # redirect
    template_name = 'blog/post_confirm_delete.html'

# date
class PostYAV(YearArchiveView):
    """
    docstring
    """
    model            = Post
    date_field       = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'


# TAG
class TagCloudTV(TemplateView):
    """
    docstring
    """
    template_name = 'blog/taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    """
    docstring
    """
    template_name = 'blog/taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        """
        docstring
        """
        return Post.objects.filter(tags__name= self.kwargs.get('tag'))


    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)    
        context['tagname'] = self.kwargs['tag']
        return context


# Search
class SearchFormView(FormView):     
    """
    docstring
    """
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self,form):
        """
        docstring
        """
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains = searchWord) | Q(description__icontains = searchWord) | Q(content__icontains = searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list


        return render(self.request, self.template_name, context) # No Redirection




