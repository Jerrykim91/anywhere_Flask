from django.db import models
from django.urls import reverse  # 빨간색 책 139page + 검색해보기 # URL 패턴을 만들어 주는 내장함수

# Create your models here.

"""
models.CharField - 짧은 문자열 정보
models.TextField - 글자수 제한없는 텍스트
models.DateTimeField - 날짜와 시간
models.ForeignKey - 다른 모델에 대한 링크

$ python manage.py makemigrations blog

"""

class Post(models.Model):

    title = models.CharField(verbose_name='TITLE', max_length=100)
    slug = models.SlugField('SLUG', unique= True, allow_unicode= True, help_text='one world for title alias.') # 글의 별칭 -> 게시물검색  # 슬러그 자세한 내용은 -> 파란색 75page
    description = models.CharField('DESCRIPTION', max_length=100,blank= True, help_text= 'simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE',auto_now_add=True) # 글 작성시간
    modify_dt =  models.DateTimeField('MODIFY DATE',auto_now=True) # 글 수정 시간 

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



# 게시는 글 작업해보고 올리자!

# 참고 :  https://amamov.tistory.com/107
# on_delete=models.CASCADE 구문이 어떤 동작을 하는지 : https://hashcode.co.kr/questions/1673/%EC%9E%A5%EA%B3%A0-%EA%B5%AC%EB%AC%B8-%EC%A7%88%EB%AC%B8-%EC%9E%85%EB%8B%88%EB%8B%A4