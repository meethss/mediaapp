from django.forms import ModelForm
from .models import Blog

class BlogCreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'post_date', 'category_id']
