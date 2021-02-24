
# # 1. 클래스형 제네릭뷰
from django.views.generic import TemplateView
# 테이블 레코드 
from django.views.generic import CreateView
# 유저 모델의 객체를 생성
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# 뷰처리 진입 단계에서 적절한 권한 을 갖추었는지 판별 
from django.contrib.auth.mixins import AccessMixin


# Create your views here.

# TemplateView
class HomeView(TemplateView):
    template_name = 'blog/home.html'

# User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = '관리자만 수정 & 삭제 가능합니다.'


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            """
            소유자 검증 
            """
            return self.handle_no_permission()
        return super().dispatch(request, *args,**kwargs)


# # prevent from other's update/delete
# class OwnerRequiredMixin(object):
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if self.request.user != self.object.owner:
#             return permission_denied(self.request,
#                                      exception="Only creator of this object can update/delete the object.")
#         return self.render_to_response(self.get_context_data())

