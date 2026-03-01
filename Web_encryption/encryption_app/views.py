from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cryptography.fernet import Fernet
import os
import mimetypes


#рендеринг индекса
@csrf_exempt
def cryptographer(request):
    if request.method == 'POST':
        crypto_file =request.FILES.get('cryptographer_file')
        # mime_type, _ = mimetypes.guess_type(crypto_file)
        # if mime_type is not None or mime_type.startswith('text'):
        #     encrypted_data = encrypt_text_file(crypto_file)
            # print(f"Файл {crypto_file} не является текстовым (тип: {mime_type}). Пропуск.")
            # return    
        
    if crypto_file:
        print(crypto_file)
    else:
        print("Файл не загружен")   
        
    return HttpResponse(201)

@csrf_exempt
def codebreaker(request):
    if request.method == 'POST':
        cobr_file = request.FILES.get('codebreaker_file')

    if cobr_file:
        print(cobr_file)
    else:
        print("Файл не загружен")    
    return HttpResponse(201)




def encrypt_text_file(file_path, base_dir="encrypted_files"):
    """Шифрует текстовый файл, создавая отдельную папку и уникальный ключ."""
    # 1. Определяем тип файла
    # mime_type, _ = mimetypes.guess_type(file_path)
    # if mime_type is None or not mime_type.startswith('text'):
    #     print(f"Файл {file_path} не является текстовым (тип: {mime_type}). Пропуск.")
    #     return

    # 2. Создаем уникальную папку для файла
    file_name = os.path.basename(file_path)
    target_dir = os.path.join(base_dir, file_name + "_secure")
    os.makedirs(target_dir, exist_ok=True)

    # 3. Генерируем уникальный ключ
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # 4. Шифруем файл
    with open(file_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = fernet.encrypt(file_data)

    # 5. Сохраняем зашифрованный файл и ключ
    with open(os.path.join(target_dir, file_name + ".fernet"), 'wb') as f:
        f.write(encrypted_data)
    with open(os.path.join(target_dir, "key.key"), 'wb') as f:
        f.write(key)

    print(f"Файл {file_name} зашифрован в {target_dir}")

def decrypt_text_file(target_dir, original_file_name):
    """Дешифрует файл, используя ключ из папки."""
    key_path = os.path.join(target_dir, "key.key")
    encrypted_file_path = os.path.join(target_dir, original_file_name + ".fernet")

    if not os.path.exists(key_path) or not os.path.exists(encrypted_file_path):
        print("Ключ или зашифрованный файл не найдены.")
        return

    with open(key_path, 'rb') as f:
        key = f.read()
    fernet = Fernet(key)

    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)

    # Сохраняем расшифрованный файл
    output_path = os.path.join(target_dir, "decrypted_" + original_file_name)
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
    print(f"Файл дешифрован: {output_path}")









@csrf_exempt
def index(request):
    # if request.method == 'POST':
    #     homework={
    #         'files': request.FILES.get('cryptographer_files')
    #     }      
    #     print(homework)
    try:
        context = {'username': request.user.username}
        return render(request,"index.html",context)    
    except AttributeError as e:
        return render(request,"index.html")
    # try:
    #     context = {'username': request.user.username}
    #     if request.method == 'POST' and request.FILES['file']:
    #         uploaded_file = request.FILES['file']
    #         # Сохранение файла или обработка
    #         # fs = FileSystemStorage()
    #         # fs.save(uploaded_file.name, uploaded_file)
    #         print("Yes")
    #     else:
    #         print("No")               
    #     return render(request,"index.html",context)    
    # except AttributeError as e:
    #     return render(request,"index.html")    

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

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('nickname')
        password = request.POST.get('password')
        #\n-это перенос строки
        print("Ник: ",username,'\n',"Пароль: ",password,sep='')
        # Авторизация здесь ищется зарегистрированого пользователя
        user=authenticate(request,username=username,password=password)
        if user is not None: #Если пользователь есть
            print('yes')
            login(request, user )
            return JsonResponse({'status':'success'}) 
        else:
            print('no')
            login(request, user )
            return JsonResponse({'status':'error'})  
    return render(request,"reg.html")

def logout_view(request):
    logout(request)
    return redirect('index')