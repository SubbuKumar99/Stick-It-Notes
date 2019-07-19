from django.shortcuts import render
from .forms import UserContentForm
from django.shortcuts import redirect
from .models import PostStorage
import json
from django.core import serializers
# Create your views here.
def homePage(request):
    post = PostStorage.objects.all()
    post_json = serializers.serialize('json',post)
    return render(request,'posts/index.html',{'post':post,'post_json':post_json})

def newPost(request):
    if request.method == 'POST':
        form = UserContentForm(request.POST)
        if form.is_valid():
            # process this data
            Post = PostStorage()
            Post.author = form.cleaned_data['user_author']
            Post.title = form.cleaned_data['user_title']
            Post.content = form.cleaned_data['user_content']
            Post.colour = form.cleaned_data['user_colour']
            Post.save()
            return redirect('homePage')
    else:
        form = UserContentForm()

    return render(request,'posts/post.html',{'form': form})

# class ArticleSerializer(ModelSerializer):
#     class Meta:
#         fields = ('author')
