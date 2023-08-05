from django.db import models





class Projects(models.Model):
    id_project = models.AutoField(primary_key=True)
    project_name = models.CharField()
    fk_customer = models.IntegerField()
    planned_start_date = models.DateField()
    planned_end_date = models.DateField()
    effective_start_date = models.DateField(blank=True, null=True)
    effective_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'