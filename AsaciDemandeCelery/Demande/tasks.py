from __future__ import absolute_import, unicode_literals

import datetime
import time

from celery import shared_task, current_app, current_task
from .models import Article
from .celery import app
@shared_task
def add(x, y):
    return x + y


@shared_task
def creation_demande(id):
    id_demande = id
    return id_demande


@shared_task
def calcul_moyenne(note1, note2):
    print(note1)
    moyenne = float((note1 + note2) / 2)
    return moyenne


# @current_app.task(
#     queue='DateQueue',
#     max_retries=3,
#     rate_limit='10/s',)
@shared_task
def date_today():
    print('TASK DATE')
    # time.sleep(8)
    # print('Fin de traitement')
    return datetime.datetime.now()


@shared_task
def creation_article(nom_article, description, statut):
    new_article = Article(
        nom_article=nom_article,
        description=description,
        flag_actif=statut
    )
    new_article.save()
    id_arti = new_article.id_article
    return id_arti


@shared_task()
def creation_article(nom_article, description, statut):
    new_article = Article(
        nom_article=nom_article,
        description=description,
        flag_actif=statut
    )
    new_article.save()
    id_arti = new_article.id_article
    return id_arti


@app.task(name='Ajout article', default_retry_delay=1 * 60)
def creation_article_two(nom_article, description, statut):
    new_article = Article(
        nom_article=nom_article,
        description=description,
        flag_actif=statut
    )
    new_article.save()
    id_arti = new_article.id_article
    return id_arti