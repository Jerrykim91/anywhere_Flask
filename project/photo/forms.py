from django.forms import inlineformset_factory # 인라인 폼셋을 반환
from photo.models import Album, Photo


"""
온라인 폼셋
메인 폼에 딸려있는 하위 폼셋을 말함 

테이블 간의 관계가 일 대 다인경우 다 테이블의 레코드를 여러개 한꺼번에 입력 받기 위한 폼이다. 
"""

PhotoInlineFormSet = inlineformset_factory(
    Album, Photo,
    fields= ['image','title', 'description'],
    extra= 2
    )