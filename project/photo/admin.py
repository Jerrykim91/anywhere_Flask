from django.contrib import admin
from photo.models import Album, Photo

# # Register your models here.

class PhotoInline(admin.StackedInline):
    """
    docstring
    """
    model = Photo
    extra = 2


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """
    docstring
    """
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """
    docstring
    """
    list_display = ('id', 'title', 'upload_dt')