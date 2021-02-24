from django.contrib import admin
from linkList.models import LinkList


# 마크다운
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

@ admin.register(LinkList)
class LinkListAdmin(MarkdownxModelAdmin):
    list_display =('id', 'title', 'url', 'tag_list')
    search_fields = ('title', 'content')

    def get_queryset(self, request):
        """
        get_queryset를 오버 라이딩  post와 tag가 다대다 관계
        한번에 쿼리로 가지고 오기 위함
        prefetch_related => 다대다에서 쿼리 횟수를 줄여 성능을 높일때 사용
        """
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        """
        tag의 네임을 콤마로 연결하여 보여주기 위함,
        """
        return ','.join(o.name for o in obj.tags.all())