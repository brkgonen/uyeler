from django.db import models


class User(models.Model):
    isim = models.CharField(max_length=80)
    email = models.EmailField(max_length=50, unique=True)
    tel_numara = models.CharField(max_length=10)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    aktif = models.BooleanField(default=True)


    def __str__(self):
        return self.isim
