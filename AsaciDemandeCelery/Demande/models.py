from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


# Create your models here.
class Article(ExportModelOperationsMixin('Article'), models.Model):
    class Meta:
        db_table = '"article"'

    id_article = models.AutoField(primary_key=True)
    nom_article = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)
    flag_actif = models.BooleanField(default=False)


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    worker = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()
    periodic_task_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class ApiKey(models.Model):
    id_api = models.IntegerField(primary_key=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=1000, blank=True, null=True)
    flag_actif = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_key'