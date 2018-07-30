from django.shortcuts import render


def post_list(request):
    return render(request, 'article/post_list.html')


def poster_detail(request):
    return render(request, 'article/poster_detail.html')




