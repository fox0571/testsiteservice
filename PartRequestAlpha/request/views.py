import datetime
from django.shortcuts import render, redirect
from .models import Request, CheckForm, Partsinv
from django.utils import timezone
from .forms import RequestForm

# @require_http_methods(["GET"])
# def showAllRequests(request):
#     response = {}
#     try:
#         requests = Request.objects.order_by('-requestTime')
#         response['list']  = json.loads(serializers.serialize("json", requests))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except  Exception,e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
# @require_http_methods(["GET"])
# def showPendingRequests(request):
#     response = {}
#     try:
#         requests = Request.objects.order_by(requestStatue=False)
#         response['list']  = json.loads(serializers.serialize("json", requests))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except  Exception,e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
# @require_http_methods(["GET"])
# def showfinishedRequests(request):
#     response = {}
#     try:
#         requests = Request.objects.order_by(requestStatue=True)
#         response['list']  = json.loads(serializers.serialize("json", requests))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except  Exception,e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
def req_new(request):
    form=RequestForm()
    return render(request, 'request/request_new.html',{'form': form})

def submit(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        post = form.save()
        post.requestTime = timezone.now()
        post.save()
        return redirect('/request/all')
    else:
        form = RequestForm()

def available(request):
    form=CheckForm()
    return render(request, 'request/check.html',{'form': form})

def submita(request):

    form = CheckForm(request.POST)
    query = request.POST.get('number','0')
    print(query)
    result=Partsinv.objects.get(number=query)
    return render(request, 'request/availability.html', {'request':result})


def showAllRequests(request):
    request_list = Request.objects.order_by('-requestTime')
    return render(request, 'request/request_detail.html', {'request':request_list})

def showPendingRequests(request):
    request_list = Request.objects.filter(requestStatue=False)
    return render(request, 'request/request_detail.html', {'request':request_list})

def showFinishedRequests(request):
    request_list = Request.objects.filter(requestStatue=True)
    return render(request, 'request/request_detail.html', {'request':request_list})
