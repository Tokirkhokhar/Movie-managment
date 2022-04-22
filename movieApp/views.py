from itertools import count
from django.shortcuts import render
from .models import Movielist,Actorlist,Role
from django.forms.models import model_to_dict

# Create your views here.
def showMovie(request):
    movies = Movielist.objects.all()
    mArr = []
    temp = {}
    for movie in movies:
        role = Role.objects.filter(m_id = movie.Id)
        print(len(role)) #Ha bahdu hu j karu
        #setattr(movie, noa , len(role) )
        temp = model_to_dict(movie)
        temp["noa"] = len(role)
        mArr.append(temp)
    return render(request , 'movieApp/show_movielist.html',{'movies':mArr,'role':role})

def showActor(request):
    actors = Actorlist.objects.all()
    mArr = []
    temp = {}
    for actor in actors:
        role = Role.objects.filter(a_id = actor.Id)
        print(len(role)) #Ha bahdu hu j karu
        #setattr(actor, noa , len(role) )
        temp = model_to_dict(actor)
        temp["noa"] = len(role)
        mArr.append(temp)
    return render(request , 'movieApp/show_actorlist.html',{'actors':mArr,'role':role})


def upVote(request , m_id):
    movie = Movielist.objects.filter(Id = m_id)
    temp = movie[0].vote + 1
    movie.update(vote = temp)
    return render(request, 'movieApp/Thanks.html' )

def downVote(request , m_id):
    movie = Movielist.objects.filter(Id = m_id)
    temp = movie[0].vote - 1 
    if temp<0:
        temp =0 
    movie.update(vote = temp)
    return render(request, 'movieApp/Thanks.html' )