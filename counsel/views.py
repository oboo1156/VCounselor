from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, CommentForm, CommentReplyForm
from .models import Client, Comment, CommentReply, Counsellor
from django.contrib.auth.decorators import login_required

#from django.http import Http404


@login_required
def home(request):
    stories = Client.objects.all()
    return render(request, 'home.html', {'stories': stories})


def counsellor(request):
    counsellors = Counsellor.objects.all()
    return render(request, 'counsellor.html', {'counsellors': counsellors})


@login_required
def create_story(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('counsel:home')
    else:
        form = ClientForm()
    return render(request, "create_story.html", {'form': form})


@login_required
def comment(request, pk):
    client = get_object_or_404(Client, id=pk)
    comments = Comment.objects.filter(client=client)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            commented = form.save(commit=False)
            commented.client = client
            commented.save()
            return redirect('counsel:comment', pk=pk)
    else:
        form = CommentForm()
    context = {'comments': comments, 'client': client, 'form': form}
    return render(request, 'comments.html', context)


def comment_reply(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment_replies = CommentReply.objects.filter(comment=comment)


    if request.method != 'POST':
        form = CommentReplyForm()
    else:
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            comment_reply = form.save(commit=False)
            comment_reply.comment = comment
            comment_reply.save()
            return redirect('counsel:comment_reply', pk=pk)

    context = {'comment': comment, 'comment_replies': comment_replies, 'form': form,}
    return render(request, 'comment_reply.html', context)


@login_required
def delete_story(request, pk):
    story = get_object_or_404(Client, id=pk)
    # if story.owner != request.user:
    #     raise Http404
    if request.method == 'POST':
        story.delete()
        return redirect('counsel:home')
    return render(request, 'delete_story.html', {'story': story})


