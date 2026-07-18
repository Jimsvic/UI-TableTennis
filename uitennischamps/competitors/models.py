from django.db import models

# Create your models here.

class Bio(models.Model):
    bioId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    initials = models.CharField(max_length=10)
    lastName = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=15)

    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ],
        default='Other'
    )

    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bios"

    def __str__(self):
        return f"{self.firstName} {self.initials} {self.lastName}"