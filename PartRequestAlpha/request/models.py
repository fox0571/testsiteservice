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
    def __str__(self):
        return self.businessName

class Part(models.Model):
    partNumber=models.CharField(max_length=20)
    partName=models.CharField(max_length=50)
    partInventory=models.IntegerField()
    def __str__(self):
        return self.partNumber

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
        related_name='+',
    )
    shippingMethod=models.CharField(max_length=20,choices=SHIPPING_METHOD,blank=True)
    part=models.ForeignKey(
        'Part',
        on_delete=models.CASCADE,
        related_name='+',
    )
    partQty=models.IntegerField()
    requestTime=models.DateField(auto_now_add=True)
    requestStatue=models.NullBooleanField()
    tracking=models.CharField(max_length=50)

    def __str__(self):
        return self.SKSID


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields=['SKSID','serialNumber','customer.businessName', \
                'tech','shippingAddress','shippingMethod', \
                'part','partQty']
