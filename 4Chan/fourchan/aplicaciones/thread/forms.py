from django import forms
from .models import Post


class PostForm(forms.ModelForm):


	class Meta:
		model = Post 
		fields = ['name','content', 'image', 'categories']
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'content': forms.Textarea(attrs={'class':'form-control'}),
			'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
			
		}
		labels = {
			'name':'','content':'','image':'','categories':''
		}