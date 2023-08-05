from django.db import models


class AssetAbsenceCodes(models.Model):
    id_asset_absence_code = models.AutoField(primary_key=True)
    asset_absence_code = models.CharField()
    asset_absence_code_abbreviation = models.CharField()

    class Meta:
        managed = False
        db_table = 'asset_absence_codes'
