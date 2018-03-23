from django.shortcuts import render

from .models import Request
from .forms import NameForm

def req(request):
    return render(request, 'request/request.html')

def create_req(sksid,cn,sn,tn,add1,add2,city,state,zip,pn,des,qty):
    time=timezone.now()+datetime.date()
    return Request.objects.create(sksid=sksid,business_name=cn,serial_number=sn,tech_name=tn,ship_add1=add1,ship_add2=add2,ship_city=city,ship_state=state,ship_zip=zip,part_number=pn,part_name=des,part_qty=qty)


def submit(request):
    form=NameForm(request.GET)
    q=create_req
