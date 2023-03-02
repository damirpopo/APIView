from django.db import models

class Category(models.Model):
    categ = models.CharField(max_length=300)

    def __str__(self):
        return self.categ

class Author(models.Model):
    firm = models.CharField(max_length=30)
    strana= models.CharField(max_length=30)

    def __str__(self):
        return self.firm


class Product(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=100)
    price= models.IntegerField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE,null=True)
    author= models.ForeignKey(Author, on_delete= models.CASCADE,null=True)


    def __str__(self):
        return self.name