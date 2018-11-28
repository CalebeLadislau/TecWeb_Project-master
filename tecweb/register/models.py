from datetime import timezone
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Aluno(models.Model):
    ra = models.IntegerField(validators = [MaxValueValidator(10)], null = True)
    nome = models.CharField(max_length = 100, null = False)
    dt_nascimento = models.DateField()
    email = models.CharField(max_length = 100, null = False)
    celular = models.CharField(max_length = 20)
    foto = models.CharField(max_length = 255)

    @staticmethod
    def save_aluno(ra, nome, dt_nascimento, email, celular, foto):

        Aluno.objects.create(ra=ra,
                             nome=nome,
                             dt_nascimento=dt_nascimento,
                             email=email,
                             celular=celular,
                             foto=foto)

        return True


class Professor(models.Model):
    nome = models.CharField(max_length = 100, null = False)
    apelido = models.CharField(max_length = 50)
    usuario = models.CharField(null = False, validators = [MaxValueValidator(30), MinValueValidator(3)], max_length = 30)
    dt_nascimento = models.DateField()
    email = models.CharField(max_length = 100, null = False)
    celular = models.CharField(max_length = 20)

    @staticmethod
    def save_professor(nome, apelido, usuario, dt_nascimento, email, celular):
        Professor.objects.create(nome=nome,
                                 apelido=apelido,
                                 usuario=usuario,
                                 dt_nascimento=dt_nascimento,
                                 email=email,
                                 celular=celular)

        return True


class Disciplina(models.Model):
    nome = models.CharField(max_length = 100, null = False)
    data = models.DateField(models.DateField(default=timezone.now))
    status = models.CharField(null = False, max_length = 100)
    plano_ensino = models.CharField(max_length = 200, null = True)
    carga_horaria = models.DecimalField(null = False, validators = [MaxValueValidator(3)], decimal_places=2, max_digits = 5)
    competencias = models.CharField(max_length=300, null=True)
    habilidades = models.CharField(max_length=300, null=True)
    ementa = models.CharField(max_length=500, null=True)
    conteudo_prog = models.CharField(max_length=100, null=True)
    biblio_basica = models.CharField(max_length=200, null=True)
    biblio_compl = models.CharField(max_length=200, null=True)
    percent_prat = models.IntegerField(validators = [MaxValueValidator(3)], null = False)
    percent_teo = models.IntegerField(validators=[MaxValueValidator(3)], null = False)
    nome_cood = models.CharField(max_length=50, null=False)

    @staticmethod
    def save_disciplina(nome, data, status, plano_ensino, carga_horaria, competencias,
                        habilidades, ementa, conteudo_prog, biblio_basica, biblio_compl, percent_prat, percent_teo, nome_cood):

        Disciplina.objects.create(nome=nome,
                                  status=status,
                                  data=data,
                                  plano_ensino=plano_ensino,
                                  carga_horaria=carga_horaria,
                                  competencias=competencias,
                                  habilidades=habilidades,
                                  ementa=ementa,
                                  conteudo_prog=conteudo_prog,
                                  biblio_basica=biblio_basica,
                                  biblio_compl=biblio_compl,
                                  percent_prat=percent_prat,
                                  percent_teo=percent_teo,
                                  nome_cood=nome_cood)

        return True