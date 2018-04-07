from django.db import models
from django.forms import ModelForm

# Create your models here.
class Partsinv(models.Model):
    item = models.CharField(db_column='Item', blank=True, null=True,max_length=100)  # Field name made lowercase.
    number = models.CharField(primary_key=True,max_length=20,blank=True)
    group_id = models.CharField(db_column='Group_ID', blank=True, null=True,max_length=100)  # Field name made lowercase.
    class_id = models.CharField(db_column='Class_ID', blank=True, null=True,max_length=100)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='Inventory', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.number

    class Meta:
        managed = False
        db_table = 'partsinv'

class CheckForm(ModelForm):
    class Meta:
        model = Partsinv
        fields=['number']
