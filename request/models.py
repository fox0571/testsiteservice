from django.db import models
from django.forms import ModelForm

SHIPPING_METHOD = (
    ('NDA','NEXT DAY AIR'),
    ('2NDA','SECOND DAY AIR'),
    ('GROUND','GROUND'),
)

class Request(models.Model):
    sksid=models.CharField(max_length=30)
    serial_number=models.CharField(max_length=50)
    business_name=models.CharField(max_length=200)
    business_add1=models.CharField(max_length=200)
    business_add2=models.CharField(max_length=50)
    business_city=models.CharField(max_length=50)
    business_state=models.CharField(max_length=50)
    business_zip=models.CharField(max_length=10)
    tech_name=models.CharField(max_length=200)
    ship_add1=models.CharField(max_length=200)
    ship_add2=models.CharField(max_length=50)
    ship_city=models.CharField(max_length=50)
    ship_state=models.CharField(max_length=50)
    ship_zip=models.CharField(max_length=10)
    ship_method=models.CharField(max_length=20,choices=SHIPPING_METHOD)
    part_number=models.CharField(max_length=20)
    part_name=models.CharField(max_length=50)
    part_qty=models.IntegerField()
    req_time=models.DateField(auto_now_add=True)
    req_statue=models.NullBooleanField()
    tracking=models.CharField(max_length=50)

    def __str__(self):
        return self.sksid

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields=['sksid','business_name','serial_number', \
                'tech_name','ship_add1','ship_add2', \
                'ship_city','ship_state','ship_zip', \
                'part_number','part_name','part_qty','ship_method']
    def clean_title(self):
        return self.cleaned_data['title'].capitalize()
