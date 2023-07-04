from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,
                            unique=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,
                            unique=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'size'
        verbose_name_plural = 'sizes'
    
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'gender'
        verbose_name_plural = 'genders'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    size = models.ForeignKey(Size,
                             related_name='sizes',
                             on_delete=models.CASCADE)
    gender_ru = models.ForeignKey(Gender,
                               related_name='genders_ru',
                               on_delete=models.CASCADE)
    gender_tm = models.ForeignKey(Gender,
                               related_name='genders_tm',
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    production_ru = models.CharField(max_length=150)
    production_tm = models.CharField(max_length=150)
    color_ru = models.CharField(max_length=200)
    color_tm = models.CharField(max_length=200)
    
    description_ru = models.TextField(blank=True)
    description_tm = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    stock = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.CharField(max_length=150)
    production = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    user_number = models.IntegerField()
    user_address = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['product']

    
    def __str__(self):
        return self.product


