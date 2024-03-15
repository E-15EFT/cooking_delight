from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import UploadMovie
from .forms import UploadMovieForm, CommentForm
# Create your views here.    
def home(request):
    queryset = UploadMovie.objects.all()
    page = request.GET.get("page")
    paginator = Paginator(queryset, 5000)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render(request, "home.html", {"movies": movies})

def play_movie(request, slug):
    instance = get_object_or_404(UploadMovie, slug=slug)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.upload_movie = instance
                new_comment.save()
                comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    comments = instance.comments.all()
    instance.views = instance.views + 1
    instance.save()
    return render(request, "play_movie.html", {"instance": instance, "form":comment_form, "comments":comments})
    return HttpResponseRedirect()
def like(request, slug):
    instance = get_object_or_404(UploadMovie, slug=slug)
    # Check if the user has already liked this movie
    liked_cookie_name = f"liked_{instance.id}"
    if liked_cookie_name not in request.COOKIES:
        # If the user hasn't liked the movie, increment the likes count and set the cookie
        instance.likes += 1
        instance.save()
        # Set the cookie to track that the user has liked this movie
        response = redirect("play-movie", instance.slug)
        response.set_cookie(liked_cookie_name, "true", max_age=2592000)  # Cookie lasts for 30 days
        return response
    # If the user has already liked the movie, redirect back to the movie page
    return redirect("play-movie", instance.slug)
# @login_required(login_url="/login/")
# def add_movie(request):   
#         if request.method == "POST":
#             fm = UploadMovieForm(request.POST, request.FILES)
#             if fm.is_valid():
#                 obj = fm.save(commit=False)
#                 obj.slug = slugify(obj.title)
#                 obj.user = request.user
#                 obj.save()
#                 fm.save_m2m()
#                 messages.success(request, "Movie Uploaded Successfully")
#                 return HttpResponseRedirect("/")
#         fm = UploadMovieForm()
#         return render(request, "add_movie.html", {"form": fm})


from django.utils.text import slugify
from django.db import IntegrityError
from django.http import JsonResponse

@login_required(login_url="/login/")
def add_movie(request):
    if request.method == "POST":
        fm = UploadMovieForm(request.POST, request.FILES)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.slug = generate_unique_slug(obj.title)
            obj.user = request.user
            obj.save()
            fm.save_m2m()
            return JsonResponse({'success': True})
        else:
            errors = fm.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        fm = UploadMovieForm()
        return render(request, "add_movie.html", {"form": fm})

def generate_unique_slug(title, max_length=1300):
    base_slug = slugify(title)[:max_length]
    slug = base_slug
    counter = 1
    while True:
        try:
            # Check if the slug already exists
            UploadMovie.objects.get(slug=slug)
            # If it does, append a counter and try again
            slug = f"{base_slug}-{counter}"
            counter += 1
        except UploadMovie.DoesNotExist:
            # If the slug is unique, return it
            return slug
        # Add a safeguard to avoid infinite loop
        if counter > 2000:
            raise IntegrityError("Unable to generate unique slug")