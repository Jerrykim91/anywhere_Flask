from django.shortcuts import render

# 1. 클래스형 제네릭뷰

from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

# Model
from linkList.models import LinkList

# App Extend 
from django.views.generic import CreateView, UpdateView, DeleteView 
# #/ login_required 기능 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Portfolio.views import OwnerOnlyMixin

# Create your views here.


class linkLV(ListView):
    model = LinkList
    template_name = 'linkList/link_list.html'
    context_object_name = 'links'
    paginate_by = 4  # 한페이지에 보여주는 객체 리스트의 개수


class linkDV(DetailView):
    model = LinkList
    template_name = 'linkList/link_detail.html'


class linkCreateView(LoginRequiredMixin,CreateView):
    model = LinkList
    template_name = 'linkList/linklist_form.html'
    fields = ['title', 'url','content','tags']
    success_url = reverse_lazy('linkList:index') # redirect
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class linkChangeLV(LoginRequiredMixin,ListView):
    # model = LinkList
    template_name = 'linkList/link_change_list.html'
    
    def get_queryset(self):
        return LinkList.objects.filter(owner=self.request.user)


class linkUpdateView(OwnerOnlyMixin,UpdateView):
    model = LinkList
    fields = ['title', 'url','content','tags']
    success_url = reverse_lazy('linkList:index') # redirect
    # template_name = 'linkList/link_form.html'
    

class linkDeleteView(OwnerOnlyMixin,DeleteView):
    model = LinkList
    template_name = 'linkList/link_confirm_delete.html'
    success_url = reverse_lazy('linkList:index') # redirect
    

# TAG
class TagCloudTV(TemplateView):
    """
    docstring
    """
    template_name = 'linkList/taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    """
    docstring
    """
    model = LinkList
    template_name = 'linkList/taggit/taggit_linkList_list.html'

    def get_queryset(self):
        """
        docstring
        """
        return LinkList.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
