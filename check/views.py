from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Partsinv, CheckForm

# Create your views here.
def available(request):
    form=CheckForm()
    return render(request, 'request/check.html',{'form': form})

def submita(request):
    #query = request.GET['number']
    #print(query)
    #result=Partsinv.objects.get(number=query)
    print("stop here1")
    if request.method == "POST":
        form = CheckForm(request.POST)
        print(form.errors)
        #form.clean_title()
        if form.is_valid():
            print("stop here3")
            query=form.cleaned_data['number']
            result=Partsinv.objects.get(number=query)
            return render(request, 'request/availability.html', {'request':result})
        else:
            # Do something in case if form is not valid
            raise Http404
        #nu=request.POST.get('number')
        #result=Partsinv.objects.get(number=nu)
        #request_list = Request.objects.order_by('-req_time')
        #return HttpResponse("True")
        #print(result.id,result.item,result.number)

    else:
        form=CheckForm()
        return render(request, 'request/check.html',{'form': form})
