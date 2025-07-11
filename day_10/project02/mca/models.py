from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    course=models.CharField(max_length=25)
    marks=models.FloatField(null=False)

    def __str__(self):
        return self.roll_no+' '+ self.name
    
class FacultyModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    Subject=models.CharField(max_length=25)

    def __str__(self):
        return self.name+' '+ self.Subject
    

    


