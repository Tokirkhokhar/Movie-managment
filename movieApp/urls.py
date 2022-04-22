
from multiprocessing import context
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showMovie ,name='showMovielist'),
    path('actor/', views.showActor , name="showActiorList"),
     path('upvote/<int:m_id>', views.upVote, name='UpVote'),
      path('downvote/<int:m_id>', views.downVote, name='downVote'),
]
