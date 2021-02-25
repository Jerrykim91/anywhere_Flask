from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

#----------------------------------------------------------------
from blog.models import Post, Category

# object
cats = Category.objects.all().values_list('name','name')


class PostForm(forms.ModelForm):  # 모델폼 상속
    class Meta:
        model = Post
        fields = ('category','title', 'description','content','image','owner','tags') # 모델에서 가져 올 필드명 작성
        widgets = {  # 이 속성의 추가로 입력항목에 부트스트랩의 클래스를 추가해 넣을 수 있다.
            'category': forms.Select(choices = cats, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),     
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        initial        = {'slug':'Auto-Filling-Do-Not-input'}
        # 이 속성의 추가로 나타내는 내용을 표시할 수 있음.
        # labels = {  
        #     'subject': '제목',
        #     'content': '내용',
        # }


class PostEdit(forms.ModelForm):  
    """
    """
    class Meta:
        model   = Post
        fields  = ['category','title','slug','description','content','image','owner','tags']
        # 이 속성의 추가로 입력항목에 부트스트랩의 클래스를 추가해 넣을 수 있다.
        widgets = {  
            'category'   : forms.Select(choices = cats, attrs={'class': 'form-control'}),
            'title'      : forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),     
            'content'    : forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            }
        initial = {'slug':'Auto-Filling-Do-Not-input',
                  'tags':'You can not input plz contact Manager'}

# #----------------------------------------------------------------

