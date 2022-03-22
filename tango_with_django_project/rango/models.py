from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'


        def __str__(self):
            return self.name


    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class courseTitle(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Course Title'


        def __str__(self):
            return self.name


    def __str__(self):
        return self.name

class startDate(models.Model):
    name = models.CharField(max_length=128, unique=True)
    date = models.IntegerField(default=2022)


    class Meta:
        verbose_name_plural = 'Start Date'


        def __str__(self):
            return self.name


    def __str__(self):
        return self.name

class desc(models.Model):
    name = models.CharField(max_length=128, unique=True)


    class Meta:
        verbose_name_plural = 'Description'


        def __str__(self):
            return self.name


    def __str__(self):
        return self.name
