from django.shortcuts import render
from About_Me.models import Me, Interests

# Create your views here.
def index(request):
    me = Me.objects.get_queryset()
    context = {}
    for m in me:
        context['name'] = m.name
        context['about_me'] = m.about_me
        context['profile_photo'] = m.profile_photo
        context['github_link'] = m.github_link
        context['linkedin_link'] = m.linkedin_link
        context['twitter_link'] = m.twitter_link

    context['interests'] = me.photos.get_queryset()
    return render(request, "About_Me/home.html", context)
