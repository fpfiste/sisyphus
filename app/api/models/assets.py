from django.db import models
from . import AssetTypes

class Assets(models.Model):
    id_asset = models.AutoField(primary_key=True)
    fk_asset_type = models.ForeignKey(AssetTypes, models.DO_NOTHING, db_column='fk_asset_type')
    asset_description = models.CharField()
    fk_employee = models.IntegerField(blank=True, null=True)
    asset_internal_alias = models.CharField()
    year_of_production = models.IntegerField(blank=True, null=True)
    asset_km_counter = models.CharField(blank=True, null=True)
    fk_sys_rec_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assets'