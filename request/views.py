import datetime
from django.shortcuts import render, redirect

from .models import Request, RequestForm
from django.utils import timezone

def req_new(request):
    form=RequestForm()
    return render(request, 'request/request.html',{'form': form})
#
#def create_req(sksid,cn,sn,tn,add1,add2,city,state,zip,pn,des,qty):
#    time=timezone.now()+datetime.date()
#    return Request.objects.create(sksid=sksid,business_name=cn,serial_number=sn,tech_name=tn,ship_add1=add1,ship_add2=add2,ship_city=city,ship_state=state,ship_zip=zip,part_number=pn,part_name=des,part_qty=qty)

#changes just test git
def submit(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        #form.clean_title()
        #if form.is_valid():
        post = form.save()
        post.req_time = timezone.now()
        post.save()
        #request_list = Request.objects.order_by('-req_time')
        #return render(request, 'request/request_detail.html', {'request':request_list})
        return redirect('/request/all')
    else:
        form = RequestForm()
    #request_list = Request.objects.order_by('-req_time')
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return render(request, 'request/request_detail.html', {'request':request_list})
    #return render(request, 'request/request.html', {'form': form})

def showAllRequests(request):
    request_list = Request.objects.order_by('-req_time')
    #output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'request/request_detail.html', {'request':request_list})

def showPendingRequests(request):
    request_list = Request.objects.filter(req_statue=False)
    return render(request, 'request/request_detail.html', {'request':request_list})

def showFinishedRequests(request):
    request_list = Request.objects.filter(req_statue=True)
    return render(request, 'request/request_detail.html', {'request':request_list})
