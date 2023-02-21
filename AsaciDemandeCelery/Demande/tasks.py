from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task, current_app


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
#     rate_limit='10/s')
@shared_task
def date_today():
    exit()
    return datetime.datetime.now()
