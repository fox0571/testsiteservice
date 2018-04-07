from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Partsinv, CheckForm

# Create your views here.
def available(request):
    form=CheckForm()
    return render(request, 'request/check.html',{'form': form})

def submita(request):

    #print(query)
    #result=Partsinv.objects.get(number=query)
    form = CheckForm(request.POST)
    query = request.POST.get('number','0')
    print(query)
    result=Partsinv.objects.get(number=query)
    return render(request, 'request/availability.html', {'request':result})
    # if request.method == "POST":
    #     #form.clean_title()
    #     if form.is_valid():
    #         query=form.cleaned_data['number']
    #         result=Partsinv.objects.get(number=query)
    #         return render(request, 'request/availability.html', {'request':result})
    # return render(request, 'request/availability.html', {'form':form})
    #     #nu=request.POST.get('number')
        #result=Partsinv.objects.get(number=nu)
        #request_list = Request.objects.order_by('-req_time')
        #return HttpResponse("True")
        #print(result.id,result.item,result.number)
