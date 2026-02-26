import os
import mimetypes
from cryptography.fernet import Fernet

def encrypt_text_file(file_path, base_dir="encrypted_files"):
    """Шифрует текстовый файл, создавая отдельную папку и уникальный ключ."""
    # 1. Определяем тип файла
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None or not mime_type.startswith('text'):
        print(f"Файл {file_path} не является текстовым (тип: {mime_type}). Пропуск.")
        return

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

# --- Использование ---
# Создадим примеры текстовых файлов
with open("doc1.txt", "w") as f: f.write("Секрет номер один один")
with open("doc2.txt", "w") as f: f.write("Секрет номер два")

# Шифруем файлы (можно вызывать много раз)
encrypt_text_file("doc1.txt")
encrypt_text_file("doc2.txt")

# Дешифровка (пример для первого файла)
# Укажите путь к созданной папке
decrypt_text_file("encrypted_files/doc1.txt_secure", "doc1.txt")