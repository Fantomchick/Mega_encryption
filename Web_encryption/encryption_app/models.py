from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    return f"crypto_files/{filename}"

class File_Base(models.Model):
    data_file = models.FileField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.data_file.name if self.data_file else "No file"