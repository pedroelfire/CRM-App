from django.db import models

# Create your models here.

class Notas(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return (f"{self.auto_increment_id}  Title: {self.title} Description:{self.description} ")