from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}
        if not postData['email']:
            errors['no_registrado'] = "no estás registrado"

        if len(postData['name']) < 2:
            errors['firstname_len'] = " El nombre debe tener al menos 2 caracteres"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Correo inválido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "El nombre debe contener unicamente letras"


        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "Contraseña y confirmar contraseña no coinciden "

        # if len(postData['cita']) < 10:
        #     errors['cita'] = "La cita debe tener mas de 10 caracteres"

        # if len(postData['autor']) < 4:
        #     errors['autor'] = "El autor debe tener mas de 4 caracteres"
        
        return errors

# author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

class Cita(models.Model):
    cita= models.CharField(max_length=255)
    autor =models.CharField(max_length=255)
    user = models.ForeignKey(User,related_name = "citas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cita} ({self.autor})"

    def __repr__(self):
    
        return f"{self.cita} ({self.autor})"

class Me_gusta(models.Model):
    megusta= models.BooleanField()   
    user= models.ForeignKey(User,related_name = "likes", on_delete = models.CASCADE)
    cita = models.ForeignKey(Cita,related_name = "citas_likes", on_delete = models.CASCADE)


# class Message(models.Model):
#     mensaje = models.CharField(max_length=255)
#     user= models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



# class Comment(models.Model):
#     comentario = models.CharField(max_length=255)
#     message = models.ForeignKey(Message, related_name = "comments", on_delete = models.CASCADE)
#     user= models.ForeignKey(User, related_name = "usuarios", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.comentario} ({self.message})"

#     def __repr__(self):
#         return f"{self.comentario} ({self.message})"
