from django.db import models



  



class PhoneNO(models.Model):
    STATUS=(
        ('Home','Home'),
        ('Mobile','Mobile'),
        ('Office','Office'),

    )
    
    Number=models.IntegerField(null=True)
    Phonetype=models.CharField(max_length=200,null=True,choices=STATUS) 
    # persondetail=models.ForeignKey(Persondetail,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.Number)

class Email(models.Model):
    
    email = models.CharField(max_length=200,null=True)
    STATUS=(
        ('Home','Home'),
        ('college','college'),
        ('Office','Office'),

    )
    emailtype = models.CharField(max_length=200,null=True,choices=STATUS)
    # persondetail=models.ForeignKey(Persondetail,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.email)
    

class Persondetail(models.Model):
    
    Name = models.CharField(max_length=200,null=True)
    Address=models.CharField(max_length=200,null=True)
    complete=models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now_add=True)
    phoneno=models.ForeignKey(PhoneNO,null=True,on_delete=models.SET_NULL)
    email=models.ForeignKey(Email,null=True,on_delete=models.SET_NULL)

    
    def __str__(self):
        return str(self.Name)
    # Assuming you have an Email object and you want to update a Persondetail instance with it
    # def __str__(self):
    #     return self.Address
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
     

