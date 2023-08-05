from django.db import models




class SysRecStates(models.Model):
    id_sys_rec_status = models.AutoField(primary_key=True)
    sys_rec_status = models.CharField()

    class Meta:
        managed = False
        db_table = 'sys_rec_states'