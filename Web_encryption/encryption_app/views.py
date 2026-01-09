from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
#рендеринг индекса
def index(request):
    if request.method == 'POST':
        crfile = request.POST.get('crfile')
        return JsonResponse({'status':'success','message':'Файл зашифрован'})
    if request.method == 'POST':
        cdfile= request.POST.get('cdfile')
        return JsonResponse({'status':'success','message':'Файл дешифрован'})

    return render(request,"index.html")