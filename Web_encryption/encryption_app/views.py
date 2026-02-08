from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#рендеринг индекса
def index(request):
    try:
        context = {'username': request.user.username}
        if request.method == 'POST' and request.FILES['file']:
            uploaded_file = request.FILES['file']
            # Сохранение файла или обработка
            # fs = FileSystemStorage()
            # fs.save(uploaded_file.name, uploaded_file)
            print("Yes")
        else:
            print("No")               
        return render(request,"index.html",context)    
    except AttributeError as e:
        return render(request,"index.html")

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('nickname')
        password = request.POST.get('password')
        email = request.POST.get('email')
        cod_email= request.POST.get('codEmail')
        password_proverka = request.POST.get('passwordProverka')
        user=User.objects.create_user(username,email,password)
        login(request, user)
        #\n-это перенос строки
        #print("Ник: ",username,'\n',"Пароль: ",password,"Почта",email,'\n',"Код",cod_email,'\n',"Пароль проверка",password_proverka,sep='')
        return JsonResponse({'status':'success'})

    return render(request,"reg.html")

def logout_view(request):
    logout(request)
    return redirect('index')