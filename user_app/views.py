
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from mediaplayer.models import UploadMovie
# Create your views here.
def public_profile(request, username):
    # if request.user.is_authenticated:
    user = get_object_or_404(User, username=username)
    session_user = request.user
    instance = UploadMovie.objects.filter(user=user).order_by("-id")
    posts = UploadMovie.objects.filter(user__username=user)
    video_count = posts.count()
    return render(
        request,
        "profile.html",
        {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "profile_pic": user.profile.profile_pic.url,
            "instances": instance,
            'video_count':video_count
        },
    )


# Sigup
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Congratulations!! your account has been created"
                )
                return HttpResponseRedirect("/login/")
        else:
            form = SignUpForm()
        return render(request, "signup.html", {"form": form})
    else:
        return HttpResponseRedirect("/")


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully !!")
                    return HttpResponseRedirect("/")
        else:
            form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        return HttpResponseRedirect("/")


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(f'/public-profile/{user}/')  # Redirect to profile detail view
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
