from django.db import models
from django.urls import reverse  # 빨간색 책 139page + 검색해보기 # URL 패턴을 만들어 주는 내장함수
from photo.fields import ThumbnailImageField

# Create your models here.
class Album(models.Model):
    """
    docstring
    """
    name        = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)  # 설명
    owner       = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER',blank=True, null=True)

    class Meta:
        """
        메타 데이터 
        """
        ordering = ('name',)

    def __str__(self):
        """
        docstring
        """
        return self.name

    def get_absolute_url(self):
        """
        docstring
        """
        return reverse('photo:album_detail', args=(self.id,))


class Photo(models.Model):
    """
    docstring
    """
    album       = models.ForeignKey(Album, on_delete=models.CASCADE)
    title       = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image       = ThumbnailImageField(upload_to='photo/%y/%m')
    upload_dt   = models.DateTimeField('Upload Date', auto_now_add=True)
    owner       = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER',blank=True, null=True)

    class Meta:
        """
        docstring
        """
        ordering = ('title',)

    def __str__(self):
        """
        docstring
        """
        return self.title

    def get_absolute_url(self):
        """
        docstring
        """
        return reverse('photo:photo_detail', args=(self.id,))



