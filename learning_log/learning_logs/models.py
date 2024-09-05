from django.db import models


# Create your models here.

# it shows the way the data will be trated

# MODEL TO HANDLE THE TOPICS

class Topic(models.Model):
    """Topic that user gets to know"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns representation of the model as a string"""
        return self.text


class Entry(models.Model):
    """Concrete infromation about progress in studying"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns represantation of model as string"""
        count = 0 
        for i in range(0, len(self.text)):
            if (self.text[i] != " "):
                count+=1
            
        if count < 50:
            return f"{self.text[:50]}"
        else: 
            return f"{self.text[:50]}..."
            