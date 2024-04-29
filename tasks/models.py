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
    STATUS=(
        ('Home','Home'),
        ('college','college'),
        ('Office','Office'),

    )
    email = models.CharField(max_length=200,null=True)
    Personid = models.CharField(max_length=200,null=True)
    emailtype = models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
        return self.Personid
     
class Persondetail(models.Model):
    phoneNO=models.ForeignKey(PhoneNO,null=True,on_delete=models.SET_NULL)
    email=models.ForeignKey(Email,null=True,on_delete=models.SET_NULL)

    Name = models.CharField(max_length=200,null=True)
    Address=models.CharField(max_length=200,null=True)
    complete=models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    # def __str__(self):
    #     return self.Address


