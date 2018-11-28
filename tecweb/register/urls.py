from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastroAluno/$', views.AlunoRegister.as_view()),
    url(r'^cadastroProfessor/$', views.ProfessorRegister.as_view()),
    url(r'^cadastroDisciplina/$', views.DisciplinaRegister.as_view())
]