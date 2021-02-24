from django.db import models
from django.urls import reverse  
from taggit.managers import TaggableManager # 태그
from photo.fields import ThumbnailImageField

from django.contrib.auth.models import User
from django.utils.text import slugify


# 마크다운
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

# models.py
class Category(models.Model):
    name          = models.CharField(max_length=150)

    def __str__(self):    
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_list') # args=(self.slug,)




class Post(models.Model):

    owner        = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER',blank=True, null=True)
    title        = models.CharField(verbose_name='TITLE', max_length=100)
    slug         = models.SlugField('SLUG', unique= True, allow_unicode= True, help_text='one world for title alias.') # 글의 별칭 -> 게시물검색  # 슬러그 자세한 내용은 -> 파란색 75page
    description  = models.CharField('DESCRIPTION', max_length=100,blank= True, help_text= 'simple description text.')
    # content      = models.TextField('CONTENT')
    content      = MarkdownxField('CONTENT')
    create_dt    = models.DateTimeField('CREATE DATE', auto_now_add=True) # 글 작성시간
    modify_dt    = models.DateTimeField('MODIFY DATE', auto_now=True) # 글 수정 시간 
    tags         = TaggableManager(blank=True)
    
    STATUS_CHOICES = (
        ('d', '비공개'),
        ('p', '회원 공개'),
        ('w', '모두에게 공개')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    # 이미지 
    image    = models.ImageField(upload_to='photo/%y/%m', blank=True, null=True)    
    
    # category 
    category     = models.CharField(max_length=150, null=True, blank=True, default='code')

    class Meta:

        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

   

    def __str__(self):

        """
        객체의 문자열 표현 매소드 
        객체의 문자열을 객체 title 속성으로 표시 
        """
        return self.title

    def get_absolute_url(self):
        """
        docstring
        """
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        """
        get_previous_by_modify_dt: 장고의 내장함수로 modify_dt()를 기준으로 최신포스트를 반환
        """
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        """
        # get_next_by_필드명()은 Django의 내장함수
        """
        return self.get_next_by_modify_dt()

# 추가
    def save(self, *args, **kwargs):
        """
        객체의 내용을 데이터베이스에 저장
        """
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs) # 부모 클래스 save를 호출 테이블에 반영

    def formatted_markdown(self):
        """
        마크다운
        """
        return markdownify(self.content)


# 이미지 
# class PhotoArt(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='post/%y/%m', blank=True, null=True)

    # def __str__(self):
    #     """
    #     docstring
    #     """
    #     return self.title

    # def get_absolute_url(self):
    #     """
    #     docstring
    #     """
    #     return reverse('blog:post_detail')