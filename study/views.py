from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.utils import timezone
import re
from .models import Post, Comment
from .forms import PostForm, CommentForm, CreateUserForm


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('study:post_list')
    else:
        form = CreateUserForm()
    return render(request, 'registration/signup.html', {'form' : form})


def post_list(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 5)
    try:
        posts_page = paginator.page(page)
    except PageNotAnInteger:
        posts_page = paginator.page(1)
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages)

    return render(request, 'bsr/post_list.html', {'posts':posts_page})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect('study:post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'bsr/post_detail.html', {'post':post, 'form':form})

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
            if len(post.video_url) == 28 :
                post.video_key = post.video_url[-11:]
                post.save()
            if len(post.video_url2) == 28 :
                post.video_key2 = post.video_url2[-11:]
                post.save()
            if len(post.video_url) > 29 :
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
            if len(post.video_url2) > 29 :
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
            if len(post.video_url) == 28 :
                post.video_key = post.video_url[-11:]
                post.video_time = None
                post.save()
            if len(post.video_url2) == 28 :
                post.video_key2 = post.video_url2[-11:]
                post.video_time2 = None
                post.save()
            if len(post.video_url) > 29 :
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
            if len(post.video_url2) > 29 :
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

# @login_required
# def comment_edit(request, pk):
#     pass

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author == request.user:
        post_pk = comment.post.pk
        comment.delete()
        return redirect('study:post_detail', pk=post_pk)
    else:
        return render(request, 'bsr/warning.html')

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_date = timezone.now()
            comment.save()
        return redirect('study:post_detail', pk=post.pk)

    else:
        form_edit = CommentForm(instance=comment)
        return render(request, 'bsr/post_detail.html', {'post':post, 'form_edit':form_edit, 'pk':comment.pk})
