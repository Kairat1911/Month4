from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feature(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Device(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    image = models.ImageField(upload_to='devices/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name


class Review(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.device.name} - {self.created_at}'