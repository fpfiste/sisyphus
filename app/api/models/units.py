from django.db import models
class Units(models.Model):
    id_unit = models.AutoField(primary_key=True)
    unit = models.CharField()
    unit_abbreviation = models.CharField()

    class Meta:
        managed = False
        db_table = 'units'