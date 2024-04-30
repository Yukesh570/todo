from django.db import models


class PhoneNO(models.Model):
    STATUS=(
        ('Home','Home'),
        ('Mobile','Mobile'),
        ('Office','Office'),

    )
    user_id=models.IntegerField(null=True)
    Number=models.IntegerField(null=True)
    Phonetype=models.CharField(max_length=200,null=True,choices=STATUS)
    vars=1

    def __num__(self):
        return "userid",vars
    vars=vars +1


class Email(models.Model):
    
    email = models.CharField(max_length=200,null=True)
    Personid = models.CharField(max_length=200,null=True)
    STATUS=(
        ('Home','Home'),
        ('college','college'),
        ('Office','Office'),

    )
    emailtype = models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
        return self.Personid
     
class Persondetail(models.Model):
    
    Name = models.CharField(max_length=200,null=True)
    Address=models.CharField(max_length=200,null=True)
    complete=models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now_add=True)
    phoneno=models.ForeignKey(PhoneNO,null=True,on_delete=models.SET_NULL)
    email=models.ForeignKey(Email,null=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.Name
    # def __str__(self):
    #     return self.Address


class searchform(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
 

class Task(models.Model):
     
    Name = models.CharField(max_length=200,null=True)
    Address=models.CharField(max_length=200,null=True)
    complete=models.BooleanField(default=False,)
   

    def __str__(self):
        return self.Name  
     

