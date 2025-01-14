from django.db import models


    
class Visite(models.Model):
    code = models.CharField(max_length=20, verbose_name="Code Visite")
    ref_pat = models.CharField(max_length=50, verbose_name="Référence Patient")
    specialite = models.CharField(max_length=50, verbose_name="Spécialité")
    service = models.CharField(max_length=50, verbose_name="Service")

    def __str__(self):
        return f"{self.code} - {self.ref_pat} - {self.specialite} - {self.service}"

    
class Avis(models.Model):
    EMOJIS = [
        ('😊', 'Satisfait'),
        ('😐', 'Neutre'),
        ('😞', 'Mécontent'),
    ]


    emoji = models.CharField(max_length=10, choices=EMOJIS, default='😊')
    visite = models.ForeignKey(Visite, on_delete=models.SET_NULL, related_name='avis', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emoji} -{self.date}"

class Setting(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} : {self.value}"
    

