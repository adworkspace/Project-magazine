from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Post

# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'home/home.html',context)


def about(request):
    return render(request,'home/about.html')
 

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<4:
            messages.error(request,'Please fill the form correctly....')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your message submitted successfully')
    return render(request,'home/contact.html')


def search(request):
    query=request.GET['query']
    if len(query)>50:
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPosts= allPostsTitle.union(allPostsContent)
    if allPosts.count()==0:
        messages.warning(request,"No search result found ! Try again.")
    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)



# Authentication APIs...

def handleSignup(request):
    if request.method=='POST':
        # Get parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        
        # Check Inputs
        if len(username)>15:
            messages.error(request,"Username must be under 15 characters.")
            return redirect("home")
        if not username.isalnum():
            messages.error(request,"Username should contains letters and numbers")
            return redirect("home")
        if pass1 != pass2:
            messages.error(request,"Password doesnot match.")
            return redirect("home")


        # Create User
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Acount created successfully!")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method=="POST":
        print("success")
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        print(loginusername)
        print(f"pw={loginpass}")

        user= authenticate(request,username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in.")
            print("success")
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials.")
            print("Faliure")
            return redirect("home")
    else:
        return HttpResponse("404 - Not Found")


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out!!!")
    return redirect("home")



def profile(request):
    return render(request,"home/profile.html")

