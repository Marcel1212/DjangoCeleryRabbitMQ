# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DataMl(models.Model):
    id_data = models.AutoField()
    type_data = models.CharField(max_length=255, blank=True, null=True)
    data_spec = models.CharField(max_length=1000, blank=True, null=True)
    flag_actif = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_ml'
