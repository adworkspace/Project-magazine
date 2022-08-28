from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from blog.models import Post,BlogComment
from blog.templatetags import get_dict

# Create your views here.
# This is views of BLOG
def blogHome(request):
    allPosts = Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)
    
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.slno not in repDict.keys():
            repDict[reply.parent.slno]=[reply]
        else:
            repDict[reply.parent.slno].append(reply)
    print(repDict)
    print("hello world")
    context={'post':post,'comments':comments,'user':request.user,'repDict':repDict}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postslno=request.POST.get("postslno")
        post=Post.objects.get(slno=postslno)
        parentslno=request.POST.get("parentslno")
        if parentslno=="":
            if len(comment)>3:
                comment=BlogComment(comment=comment,user=user,post=post)
                messages.success(request,"successfully commented.")
        else:
            parent=BlogComment.objects.get(slno=parentslno)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"successfully replied.")
        comment.save()
        
    return redirect(f'/blog/{post.slug}')
