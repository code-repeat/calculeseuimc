from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def imc(request):
    imc_result = ''
    if request.GET.get('height') and request.GET.get('weight') != '':
        height = float(request.GET.get('height'))
        weight = float(request.GET.get('weight'))
        imc_result = round(weight / height ** 2, 2)


    return render(request, 'imc/imcapp.html', {'imc':imc_result})
