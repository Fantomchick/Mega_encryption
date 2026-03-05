from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt
from cryptography.fernet import Fernet
from django.urls import reverse
from .models import File_Base
import os
from django.conf import settings


def get_or_create_user_key(user):
    """
    Функция ищет ключ пользователя в media/keys/username/key.key.
    Если ключа нет — создает его.
    """
    # Папка ключей конкретного пользователя
    user_key_dir = os.path.join(settings.MEDIA_ROOT, 'keys', user.username)
    key_path = os.path.join(user_key_dir, 'key.key')

    # Если папки или ключа нет — создаем
    if not os.path.exists(key_path):
        os.makedirs(user_key_dir, exist_ok=True)
        new_key = Fernet.generate_key()
        with open(key_path, 'wb') as key_file:
            key_file.write(new_key)
        return new_key
    else:
        with open(key_path, 'rb') as key_file:
            existing_key = key_file.read()
        return existing_key 
#рендеринг индекса
@csrf_exempt
def cryptographer(request):
    if request.method == 'POST':
        crypto_file =request.FILES.get('cryptographer_file')
        if not request.user.is_authenticated:
           return JsonResponse({'error': 'Вы должны быть авторизованы'}, status=403)
        
        if not crypto_file:
            return JsonResponse({'error': 'Файл не выбран'}, status=400)

        # 1. Сохраняет файл в БД (в папку по умолчанию из модели)
        file_instance = File_Base.objects.create(data_file=crypto_file)
        original_path = file_instance.data_file.path
        
        try:
            # 2. Получает ЛИЧНЫЙ ключ пользователя
            user_key = get_or_create_user_key(request.user)
            fernet = Fernet(user_key)

            # 3. Читает и шифруем данные
            with open(original_path, 'rb') as f:
                data = f.read()
            
            encrypted_data = fernet.encrypt(data)

            # 4. Сохраняет зашифрованный файл (добавляем .encrypted)
            enc_path = original_path + ".encrypted"
            with open(enc_path, 'wb') as f:
                f.write(encrypted_data)

            # 5. Удаляет оригинал и чистим запись в БД (как в задании)
            crypto_dir = os.path.join(settings.MEDIA_ROOT, 'crypto_files')
            encrypted_filename = crypto_file.name
            encrypted_path = os.path.join(crypto_dir, encrypted_filename)
            os.remove(encrypted_path)

            # 6. Возвращает URL для скачивания через AJAX
            download_url = reverse('download_file', kwargs={'filename': os.path.basename(enc_path)})
            

            return JsonResponse({
                'status': 'success',
                'download_url': download_url
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Вы должны быть авторизованы'}, status=403)

def download_file(request, filename):
    """Вспомогательный view для отдачи файла"""
    # Путь к файлу в папке media/crypto_files/
    file_path = os.path.join(settings.MEDIA_ROOT, 'crypto_files', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    return JsonResponse({'error': 'Файл не найден'}, status=404)        


@csrf_exempt
def codebreaker(request):
    print('Yes')
    if request.method == 'POST':
        encrypted_file = request.FILES.get('codebreaker_file')
        if not request.user.is_authenticated:
           return JsonResponse({'error': 'Вы должны быть авторизованы'}, status=403)
        if not encrypted_file:
            return JsonResponse({'error': 'Файл не выбран'}, status=400)
        print('Yes')
        # Сохраняем загруженный .encrypted файл во временную папку media/crypto_files/
        crypto_dir = os.path.join(settings.MEDIA_ROOT, 'crypto_files')
        os.makedirs(crypto_dir, exist_ok=True)
        print('Yes')
        encrypted_filename = encrypted_file.name
        encrypted_path = os.path.join(crypto_dir, encrypted_filename)

        with open(encrypted_path, 'wb') as f:
            for chunk in encrypted_file.chunks():
                f.write(chunk)
        print('Yes')
        try:
            # Получаем ключ пользователя
            user_key = get_or_create_user_key(request.user)
            fernet = Fernet(user_key)
            print('Yes')
            # Читаем зашифрованные данные
            with open(encrypted_path, 'rb') as f:
                encrypted_data = f.read()
            print('Yes')
            # Расшифровываем
            decrypted_data = fernet.decrypt(encrypted_data)
            print('Yes')
            # Формируем имя исходного файла (убираем .encrypted)
            if encrypted_filename.endswith('.encrypted'):
                original_filename = encrypted_filename[:-10]
            else:
                original_filename = encrypted_filename + '.decrypted'
            print('Yes')
            decrypted_path = os.path.join(crypto_dir, original_filename)
            print('Yes')
            # Сохраняем расшифрованный файл
            with open(decrypted_path, 'wb') as f:
                f.write(decrypted_data)

            # Удаляем зашифрованный файл
            os.remove(encrypted_path)
            print('Yes9')
            # Возвращаем URL для скачивания расшифрованного файла
            download_url = reverse('download_file', kwargs={'filename': original_filename})

            return JsonResponse({
                'status': 'success',
                'download_url': download_url
            })
        except Exception as e:
            # Если ошибка дешифровки (например, неправильный ключ)
            return JsonResponse({'error': f'Ошибка дешифровки: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Вы должны быть авторизованы'}, status=403)


@csrf_exempt
def index(request):
    try:
        context = {'username': request.user.username}
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