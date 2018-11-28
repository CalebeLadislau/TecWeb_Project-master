import datetime

from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Aluno, Professor, Disciplina

class AlunoRegister(generics.ListAPIView):
    template_name = 'register/cadastroAluno.html'

    def get(self, request, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, **kwargs):
        ra = request.POST.get('ra')
        name = request.POST.get('name')
        birthday = request.POST.get('birthdate')
        email = str(request.POST.get('email'))
        cel = request.POST.get('cel')
        foto = 'example'

        Aluno.save_aluno(ra, name, birthday, email, cel, foto)

        return render(request, template_name=self.template_name)


class ProfessorRegister(generics.ListAPIView):
    template_name = 'register/cadastroProfessor.html'

    def get(self, request, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, **kwargs):
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        user = request.POST.get('user')
        birthday = request.POST.get('birthdate')
        email = str(request.POST.get('email'))
        cel = request.POST.get('cel')

        Professor.save_professor(name, nickname, user, birthday, email, cel)

        return render(request, template_name=self.template_name)


class DisciplinaRegister(generics.ListAPIView):
    template_name = 'register/cadastroDisciplina.html'

    def get(self, request, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, **kwargs):
        nome = request.POST.get('name')
        plano_ensino = request.POST.get('txtPlanoEnsino')
        date = request.POST.get('date')
        carga_horaria = request.POST.get('cargaHoraria')
        competencias = str(request.POST.get('Competencias'))
        habilidades = request.POST.get('Habilidade')
        ementa = request.POST.get('Ementa')
        conteudo_prog = request.POST.get('Programatico')
        biblio_basica = request.POST.get('BibliografiaBasica')
        biblio_compl = request.POST.get('BibliografiaComplementar')
        percent_prat = request.POST.get('percentualPratico')
        percent_teo = request.POST.get('percentualTeorico')
        nome_cood = None
        status = None

        for x in request.POST.getlist('select-status'):
            status = x

        for x in request.POST.getlist('select-option'):
            nome_cood = x



        Disciplina.save_disciplina(nome, date, status, plano_ensino, carga_horaria, competencias,habilidades, ementa, conteudo_prog, biblio_basica, biblio_compl, percent_prat, percent_teo, nome_cood)

        return render(request, template_name=self.template_name)