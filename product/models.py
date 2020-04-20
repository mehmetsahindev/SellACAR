from django.db import models


# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=40)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    VITES = (
        ('yarıoto', 'Yarı Otomatik'),
        ('tamoto', 'Tam Otomatik'),
        ('manuel', 'Manuel'),
    )
    DURUM = (
        ('sıfır', 'Sıfır'),
        ('ikinciel', 'İkinci El'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    renk = models.CharField(max_length=50)
    year = models.IntegerField()
    kilometre = models.IntegerField()
    vites = models.CharField(max_length=20, choices=VITES, default='Belirtilmedi')
    durum = models.CharField(max_length=20, choices=DURUM, default='Belirtilmedi')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
