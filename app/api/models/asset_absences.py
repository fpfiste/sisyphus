from django.db import models
from . import AssetAbsenceCodes

class AssetAbsences(models.Model):
    id_asset_absence = models.AutoField(primary_key=True)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()
    fk_asset = models.ForeignKey('Assets', models.DO_NOTHING, db_column='fk_asset')
    fk_asset_absence_code = models.ForeignKey(AssetAbsenceCodes, models.DO_NOTHING, db_column='fk_asset_absence_code')

    class Meta:
        managed = False
        db_table = 'asset_absences'