from django.db import models

# Create your models here.
class category(models.Model):
    Field = models.CharField(
        max_length = 6,
        choices=(
            ('it',"IT"),
            ('non-it',"NON IT")
        )

    )
    def __str__(self):
        return self.Field
class skill(models.Model):
    skill = models.CharField(max_length=20)

    def __str__(self):
        return self.skill
class company(models.Model):
    categories = models.ForeignKey("category",on_delete=models.CASCADE)
    skills = models.ForeignKey("skill",on_delete=models.CASCADE)
    HR = models.ForeignKey("HR",on_delete=models.CASCADE)

    company = models.CharField(max_length=20)

    def __str__(self):
        return self.company

class HR(models.Model):
    HR_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.HR_Name

class user(models.Model):
  
   user = models.CharField(max_length=20)

   def __str__(self):
        return self.user

class FeedBack(models.Model):
    company_namee = models.ForeignKey("company",on_delete = models.CASCADE)
    user_name = models.ForeignKey("user",on_delete = models.CASCADE)
    Ratings = models.CharField(
        max_length = 1,
        choices=(
            ('1',"one"),
            ('2',"two"),
            ('3',"three"),
            ('4',"four"),
            ('5',"five")
        )

    )
    Enter_Your_Feedback = models.CharField(max_length=30)

    def __str__(self):
        return self.Ratings
        

