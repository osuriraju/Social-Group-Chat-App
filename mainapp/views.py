from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, PostFrom, ProfilePicForm
from .models import PostModel, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.


@login_required(login_url='/login')
def index(request):
    data = PostModel.objects.all()
    pic = UserProfile.objects.all()

    if request.method == 'POST':
        postid = request.POST.get('postid')
        userid = request.POST.get('userid')
        
        if postid:
            postdata = PostModel.objects.get(id = postid)
            postdata.delete()
            return redirect('/index')

        elif userid:
            userdata = User.objects.filter(id = userid).first()
            print(userdata)
            if userdata:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(userdata)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(userdata)
                except:
                    pass
        else:
            return render(request, 'mainapp/Index.html', {'data': data, 'pict':pic})
    return render(request, 'mainapp/Index.html', {'data': data, 'pict':pic})



def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index')

    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})




@login_required(login_url='/login')
@permission_required("mainapp.add_postmodel", raise_exception=False)
def addpost(request):
    if request.method == 'POST':
        form = PostFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/index')
    else:
        form = PostFrom()
    
    return render(request, 'mainapp/addpost.html', {'form':form})


def addprofilepic(request):

    profile = UserProfile.objects.get(user_id = request.user.id)

    
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)

        if form.is_valid():

            if profile is not None:
                profile.delete()

            pict = form.save(commit=False)
            
            pict.user = request.user
            pict.save()
            return redirect('/index')
    else:
        form = ProfilePicForm()
    return render(request, 'mainapp/addprofilepic.html', {'form':form, 'profile':profile})

