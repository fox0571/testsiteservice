from django.db import models
from django.forms import ModelForm

SHIPPING_METHOD = (
    ('NDA','NEXT DAY AIR'),
    ('2NDA','SECOND DAY AIR'),
    ('GROUND','GROUND'),
)

STATES = (
    ("AL","Alabama"),("AK","Alaska"),("AS","American Samoa"),("AZ","Arizona"),
    ("AR","Arkansas"),("CA","California"),("CO","Colorado"),("CT","Connecticut"),
    ("DE","Delaware"),("DC","District Of Columbia"),("FM", "Federated States Of Micronesia"),
    ("FL", "Florida"),("GA", "Georgia"),("GU", "Guam"),("HI", "Hawaii"),("ID", "Idaho"),
    ("IL", "Illinois"),("IN", "Indiana"),("IA", "Iowa"),("KS", "Kansas"),("KY", "Kentucky"),
    ("LA", "Louisiana"),("ME", "Maine"),("MH", "Marshall Islands"),("MD", "Maryland"),
    ("MA", "Massachusetts"),("MI", "Michigan"),("MN", "Minnesota"),("MS", "Mississippi"),
    ("MO", "Missouri"),("MT", "Montana"),("NE", "Nebraska"),("NV", "Nevada"),
    ("NH", "New Hampshire"),("NJ", "New Jersey"),("NM", "New Mexico"),("NY", "New York"),
    ("NC", "North Carolina"),("ND", "North Dakota"),("MP", "Northern Mariana Islands"),("OH", "Ohio"),
    ("OK", "Oklahoma"),("OR", "Oregon"),("PW", "Palau"),("PA", "Pennsylvania"),("PR", "Puerto Rico"),
    ("RI", "Rhode Island"),("SC", "South Carolina"),("SD", "South Dakota"),("TN", "Tennessee"),
    ("TX", "Texas"),("UT", "Utah"),("VT", "Vermont"),("VI", "Virgin Islands"),("VA", "Virginia"),
    ("WA", "Washington"),("WV", "West Virginia"),("WI", "Wisconsin"),("WY", "Wyoming"),
)
class Address(models.Model):
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=30,choices=STATES)
    zipCode=models.CharField(max_length=12)

class Person(models.Model):
    businessName=models.CharField(max_length=200)
    address=models.ForeignKey(
        'Address',
        on_delete=models.CASCADE,
    )
    contactName=models.CharField(max_length=20,blank=True)
    email=models.EmailField(max_length=254,blank=True)
    phone=models.CharField(max_length=15,blank=True)

class Request(models.Model):
    SKSID=models.CharField(max_length=30)
    serialNumber=models.CharField(max_length=50)
    customer=models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        related_name='+',
    )
    tech=models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        related_name='+',
    )
    shippingAddress=models.ForeignKey(
        'Address',
        on_delete=models.CASCADE,
    )
    shippingMethod=models.CharField(max_length=20,choices=SHIPPING_METHOD,blank=True)
    partNumber=models.CharField(max_length=20)
    partName=models.CharField(max_length=50)
    partQty=models.IntegerField()
    requestTime=models.DateField(auto_now_add=True)
    requestStatue=models.NullBooleanField()
    tracking=models.CharField(max_length=50)
    def __str__(self):
        return self.sksid
# class Request(models.Model):
#     sksid=models.CharField(max_length=30)
#     serial_number=models.CharField(max_length=50)
#     business_name=models.CharField(max_length=200)
#     business_add1=models.CharField(max_length=200)
#     business_add2=models.CharField(max_length=50)
#     business_city=models.CharField(max_length=50)
#     business_state=models.CharField(max_length=50)
#     business_zip=models.CharField(max_length=10)
#     tech_name=models.CharField(max_length=200)
#     ship_add1=models.CharField(max_length=200)
#     ship_add2=models.CharField(max_length=50)
#     ship_city=models.CharField(max_length=50)
#     ship_state=models.CharField(max_length=50)
#     ship_zip=models.CharField(max_length=10)
#     ship_method=models.CharField(max_length=20,choices=SHIPPING_METHOD)
#     part_number=models.CharField(max_length=20)
#     part_name=models.CharField(max_length=50)
#     part_qty=models.IntegerField()
#     req_time=models.DateField(auto_now_add=True)
#     req_statue=models.NullBooleanField()
#     tracking=models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.sksid

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields=['SKSID','serialNumber','customer', \
                'tech','shippingAddress','shippingMethod', \
                'partNumber','partName','partQty']
# class RequestForm(ModelForm)
#     class Meta:
#         model = Request
#         fields=['sksid','business_name','serial_number', \
#                 'tech_name','ship_add1','ship_add2', \
#                 'ship_city','ship_state','ship_zip', \
#                 'part_number','part_name','part_qty','ship_method']
#     def clean_title(self):
#         return self.cleaned_data['title'].capitalize()
