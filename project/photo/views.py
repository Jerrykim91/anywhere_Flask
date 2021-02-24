
from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from Portfolio.views import OwnerOnlyMixin
from photo.forms import PhotoInlineFormSet 


# Create your views here.

"""
urls.py 에서 바로 model 지정가능 함 책 207 페이지 참조 
"""

class AlbumLV(ListView):
    model = Album
    template_name = 'photo/album_list.html'


class AlbumDV(DetailView):
    model = Album
    template_name = 'photo/album_detail.html'
    

class PhotoDV(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'
    

## --- Album
class AlbumCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ('name','description')
    success_url = reverse_lazy('photo:index')
    # template_name = ".html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context =  self.get_context_data()
        formset = context['formset'] 
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('photo:album_detail', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))
       

class AlbumChLV(LoginRequiredMixin, ListView):
    model = Album
    template_name = "photo/album_change_list.html"
    
    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumUV(OwnerOnlyMixin,UpdateView):
    model = Album
    fields = ('name','description')
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context =  self.get_context_data()
        formset = context['formset'] 

        if form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
       

class AlbumDelV(OwnerOnlyMixin,DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')


## ---- photo

class PhotoCV(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('album','title','image','description')
    success_url = reverse_lazy('photo:index')
    template_name = "photo/photo_form.html"
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        

class PhotoChLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = "photo/photo_change_list.html"
    
    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUV(OwnerOnlyMixin,UpdateView):
    model = Photo
    fields = ('album','title','image','description')
    success_url = reverse_lazy('photo:index')


class PhotoDelV(OwnerOnlyMixin,DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')


