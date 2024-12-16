from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return "Баннер"
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class Contacts(models.Model):
    location = models.CharField(max_length=255)
    open_hours = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class FormUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
