from django.db import models

# Create your models here.

# it shows the way the data will be trated

# MODEL TO HANDLE THE TOPICS

class Topic(models.Model):
    """Topic that user gets to know"""
    text = models.CharField(max_lenght=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns representation of the model as a string"""
        return self.text
