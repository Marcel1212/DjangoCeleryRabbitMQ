from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import request, JsonResponse
from .tasks import calcul_moyenne, date_today, creation_article, creation_article_two


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @login_required(login_url='/login/')
def index(request):
    moy = calcul_moyenne.delay(int(10), int(15))
    moyenne = calcul_moyenne(int(10), int(15))
    # Date
    date_p = date_today.delay()
    date = date_today()
    # Ajout en BD
    nom_art = 'La revenche des trouillards 6 '
    descrip_art = 2
    stat = False
    tache = creation_article.delay(nom_art, descrip_art, stat)
    creation_article_two.delay(nom_art, descrip_art, stat)
    # Recuperation de l'ID de la tache
    print(tache)
    information = {
        'message': 'Succes',
        'process_id': str(moy),
        'moyenne': moyenne,
        'date_process': str(date_p),
        'date': date
    }
    return JsonResponse(data=information, safe=False, status=status.HTTP_200_OK)
