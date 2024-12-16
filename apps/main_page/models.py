from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return "Banner"
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннера'


class Houses(models.Model):
    image = models.ImageField(upload_to='houses/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    addres = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    first_description = models.CharField(max_length=255)
    second_description = models.CharField(max_length=255)

    def __str__(self):
        return self.addres
    
    class Meta:
        verbose_name = 'Обьект(Дом)'
        verbose_name_plural = 'Обьекты(Дома)'


class MiniCards(models.Model):
    image = models.ImageField(upload_to='mini_cards/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Мини карточка'
        verbose_name_plural = 'Мини карточки'



STARS = ((i, str(i)) for i in range(1, 6))
class Reviews(models.Model):
    image = models.ImageField(upload_to='reviews/')
    star = models.IntegerField(choices=STARS)
    name = models.CharField(max_length=255)
    description = models.TextField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class OurAgents(models.Model):
    image = models.ImageField(upload_to='our_agents/')
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    link1 = models.URLField()
    link2 = models.URLField()
    link3 = models.URLField()
    link4 = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Наши агенты'
        verbose_name_plural = 'Наши агенты'


class Footer(models.Model):
    addres = models.CharField(max_length=255)
    number1 = models.CharField(max_length=255)
    number2 = models.CharField(max_length=255)
    mail = models.EmailField()


class Advantages(models.Model):
    image = models.ImageField(upload_to='advantages/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Numbers(models.Model):
    number = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = 'Цифры'
        verbose_name_plural = 'Цифры'