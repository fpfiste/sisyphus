from django.db import models




class TaskStates(models.Model):
    id_task_state = models.AutoField(primary_key=True)
    task_state = models.CharField()

    class Meta:
        managed = False
        db_table = 'task_states'