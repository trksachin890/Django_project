from django.db import models
# yesma maile user haleko xaina so yeslai paxi halka modification garu parla 
class Mrsachin(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=254)
    phoneno = models.CharField(max_length=12)
    hobby = models.CharField(max_length=50)
    familyno = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Family(models.Model):
    mrsachin = models.ForeignKey(Mrsachin, on_delete=models.CASCADE)
    fathername = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    
    def __str__(self):
        return self.fathername

class Sibling(models.Model):
    mrsachin = models.ForeignKey(Mrsachin, on_delete=models.CASCADE)
    brothername = models.CharField(max_length=50)
    sistername = models.CharField(max_length=50)
    
    def __str__(self):
        return self.brothername

class CV(models.Model):
    mrsachin = models.OneToOneField(Mrsachin, on_delete=models.CASCADE)
    cv = models.ImageField(upload_to='cv/', max_length=255,blank=True, null=True)
    
    
    def __str__(self):
        return str(self.cv)
