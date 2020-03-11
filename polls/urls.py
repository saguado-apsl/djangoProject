from django.urls import path
from . import views
from polls.views import  detail, result, vote

app_name = "polls"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/result/', result, name='result'),
    path('<int:question_id>/vote/', vote, name='vote'),
]