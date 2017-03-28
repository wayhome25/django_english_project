from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import re
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'bsr/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bsr/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if len(post.video_url) == 0 :
                post.save()
            if len(post.video_url2) == 0 :
                post.save()
            if len(post.video_url) > 40 :
                post.video_key1 = post.video_url1[-11:]
                post.save()
            if len(post.video_url2) > 40 :
                post.video_key2 = post.video_url2[-11:]
                post.save()
            if 0 < len(post.video_url) < 40 :
                # post.video_url 저장
                post.video_key = post.video_url[17:17+11]
                regx_time =  r't=\d{0,2}m?\d{0,2}s?'
                result_time = re.search(regx_time, post.video_url)
                result_time = result_time.group(0)
                result_time = re.findall(r'\d+', result_time)
                if len(result_time) > 1:
                    post.video_time =  int(result_time[0])*60+int(result_time[1])
                else:
                    post.video_time = int(result_time[0])
                post.save()
            if 0 < len(post.video_url2) < 40 :
                # post.video_url2 저장
                post.video_key2 = post.video_url2[17:17+11]
                regx_time =  r't=\d{0,2}m?\d{0,2}s?'
                result_time = re.search(regx_time, post.video_url2)
                result_time = result_time.group(0)
                result_time = re.findall(r'\d+', result_time)
                if len(result_time) > 1:
                    post.video_time2 =  int(result_time[0])*60+int(result_time[1])
                else:
                    post.video_time2 = int(result_time[0])
                post.save()
            return redirect('study:post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'bsr/post_new.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if len(post.video_url) == 0 :
                post.video_key = None
                post.save()
            if len(post.video_url2) == 0 :
                post.video_key2 = None
                post.save()
            if len(post.video_url) > 40 :
                post.video_key1 = post.video_url1[-11:]
                post.save()
            if len(post.video_url2) > 40 :
                post.video_key2 = post.video_url2[-11:]
                post.save()
            if 0 < len(post.video_url) < 40 :
                # post.video_url 저장
                post.video_key = post.video_url[17:17+11]
                regx_time =  r't=\d{0,2}m?\d{0,2}s?'
                result_time = re.search(regx_time, post.video_url)
                result_time = result_time.group(0)
                result_time = re.findall(r'\d+', result_time)
                if len(result_time) > 1:
                    post.video_time =  int(result_time[0])*60+int(result_time[1])
                else:
                    post.video_time = int(result_time[0])
                post.save()
            if 0 < len(post.video_url2) < 40 :
                # post.video_url2 저장
                post.video_key2 = post.video_url2[17:17+11]
                regx_time =  r't=\d{0,2}m?\d{0,2}s?'
                result_time = re.search(regx_time, post.video_url2)
                result_time = result_time.group(0)
                result_time = re.findall(r'\d+', result_time)
                if len(result_time) > 1:
                    post.video_time2 =  int(result_time[0])*60+int(result_time[1])
                else:
                    post.video_time2 = int(result_time[0])
                post.save()
            return redirect('study:post_detail', pk=post.pk)
    else:
        if post.author == request.user:
            form = PostForm(instance=post)
            return render(request, 'bsr/post_edit.html', {'form':form})
        else:
            return render(request, 'bsr/warning.html')


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
        return redirect('study:post_list')
    else:
        return render(request, 'bsr/warning.html')
