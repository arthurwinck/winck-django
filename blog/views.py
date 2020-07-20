from django.shortcuts import render
from .models import Posts
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from .filters import PostsFilterAlt
from django.db.models import Q
# Create your views here.

def blog_index(request):
    #ordenar os posts
    posts = Posts.objects.all().order_by('date')
    filterPosts = PostsFilterAlt(request.GET,queryset=posts)
    posts = filterPosts.qs

    #renderizar a pagina html para o browser

    if 'term' in request.GET:
        term = request.GET.get('term')
        query = Posts.objects.filter(title__icontains=term)

        postsList = []
        for post in query:
            postsList.append(post.title)

        postsJson = JsonResponse(postsList, safe=False)

        return postsJson

    if 'search' in request.GET:
        q = request.GET.get('search')
        posts = Posts.objects.filter(title__icontains=q)

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request,"blog/blog_index.html",{'page_obj': page_obj, 'filterPosts': filterPosts})

def blog_details(request,slug):
    #return HttpResponse(slug)
    posts = Posts.objects.get(slug=slug)
    return render(request,'blog/blog_details.html',{'posts':posts})
