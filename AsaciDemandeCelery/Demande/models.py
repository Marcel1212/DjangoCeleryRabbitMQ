from django.db import models


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = '"article"'

    id_article = models.AutoField(primary_key=True)
    nom_article = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)
    flag_actif = models.BooleanField(default=False)
