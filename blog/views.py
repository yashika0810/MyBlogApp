from django.views import generic
from .models import Post
from django.http import HttpResponse
from .forms import CreateBlog
from django.shortcuts import render, get_object_or_404, redirect


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def createblog(request):
    if request.method == "POST":
        form = CreateBlog(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                print('error saving')
    else:
        form = CreateBlog()
    return render(request,'blog/create.html',{'create':form})


def random(request):
    return render(request,'blog/random.html')

def edit(request, id):
    update_blog = Post.objects.get(id=id)
    return render(request,'blog/edit.html', {'edit':update_blog})

def update(request, id):

    if id:
        updateblog = get_object_or_404(Post, pk=id)
    else:
        updateblog = Post(id=id)

    form = CreateBlog(request.POST or None, instance=updateblog)
    if request.POST and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/edit.html', {'edit': form})

def delete(request, id):
    author = Post.objects.get(id=id)
    author.delete()
    return redirect("home")



