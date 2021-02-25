from django.contrib import admin
from blog.models import Post
from blog.models import PhotoArt
# from blog.models import Category, PhotoArt

# 마크다운
from markdownx.admin import MarkdownxModelAdmin

# # Register your models here.
class PhotoInline(admin.TabularInline):
    model = PhotoArt

@ admin.register(Post) # 데코레이터
class PostAdmin(MarkdownxModelAdmin):
    """
    admin 사이트에서 어떤모습으로 
    보여줄지를 정의하는 클래스
    """
    # 보여줄 필드 
    list_display = ('id', 'title', 'owner','modify_dt','tag_list')
    list_display_links = ['id', 'title']
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    inlines = [PhotoInline, ] # Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
  
    # 자동으로 채워질 필드 설정 
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ','.join(o.name for o in obj.tags.all())

    # actions = ['make_published', 'make_draft']

    # # admin action 추가
    # def make_published(self, request, queryset):
    #     updated_count = queryset.update(Mystatus='p') #queryset.update
    #     self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count)) #django message framework 활용
    # make_published.short_description = '지정 포스팅을 Published 상태로 변경'

    # def make_draft(self, request, queryset):
    #     updated_count = queryset.update(Mystatus='d') #queryset.update
    #     self.message_user(request, '{}건의 포스팅을 draft 상태로 변경'.format(updated_count)) #django message framework 활용
    # make_draft.short_description = '지정 포스팅을 draft 상태로 변경'

    


# Category
# admin.site.register(Category)

# PhotoArt
admin.site.register(PhotoArt)

