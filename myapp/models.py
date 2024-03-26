from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    qualification = models.CharField(max_length=100)
    dob = models.DateField()

    class Meta:
        db_table = "office"

        def __str__(self):
            return self.name
