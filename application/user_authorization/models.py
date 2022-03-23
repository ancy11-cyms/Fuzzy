from django.db import models

# Create your models here.
class registrations(models.Model):
    
    mobile_number = models.CharField(max_length=20)
    def __str__(self):
        return self.mobile_number
    

class login(models.Model):
    
    loginobj = models.ForeignKey("registrations",on_delete=models.CASCADE,null=True)
    Full_Name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 10)
    gender = models.CharField(
        max_length = 1,
        choices=(
            ('M',"Male"),
            ('F',"Female")  
        )
    )
    def __str__(self):
        return self.Full_Name
    
class resumedata(models.Model):
    fname = models.CharField(max_length=20,null = True)
    objj = models.ForeignKey("login",on_delete=models.CASCADE,null=True)
    Qualification = models.CharField(max_length=20)
    Expireance = models.CharField(max_length = 2)
    Skills = models.CharField(max_length = 50)
    Picture = models.ImageField(upload_to ="userpic/")
    Marks = models.CharField(max_length=2)
    Hobbies = models.CharField(max_length=30)
    def __str__(self):
        return self.fname 

    

    
    


    






