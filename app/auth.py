from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .models import User
from .decorators import login_required

    

def login(request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    
    if request.method == "POST":
        print(request.POST)
        us = User.objects.filter(email=request.POST['email'])
        if us:
            log_user = us[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):

                us = {
                    "id" : log_user.id,
                    "name": f"{log_user}",
                    "email": log_user.email,
                    "role": log_user.role
                }
                # variable de sesion
                request.session['user'] = us
                messages.success(request, "Logueado correctamente.")
                print('variable de sesion', us)
                print(us["name"])
                print(request.POST['email'])
                return redirect("/muro/")
            else:
                messages.error(request, "Password o Email  incorrectos.")
        else:
            messages.error(request, "Email o password incorrectos.")

        return redirect("/login")
    else:
        if 'user' in request.session:
            messages.warning(request,"Ya estás registrado o logeado.")
    
            return redirect('/muro/')
        else:

            # new = User.objects.last()
            #  request.session['user'] = {
            #     "id" : new.id,
            #     "name": f"{usuario_nuevo.name}",
            #     "email": usuario_nuevo.email
            # # }
            return render(request, 'login.html')


def registro(request):
    if request.method == "POST":

        errors = User.objects.validador_basico(request.POST)
        # print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                # print("DESDE EL FOR: ",key, value)
            
            request.session['register_name'] =  request.POST['name']
            request.session['register_email'] =  request.POST['email']

        else:
            request.session['register_name'] = ""
            request.session['register_email'] = ""

            password_encryp = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 

            usuario_nuevo = User.objects.create(
                name = request.POST['name'],
                email=request.POST['email'],
                password=password_encryp,
                role=request.POST['role']
            )

            messages.success(request, "El usuario fue agregado con exito.")
            

            request.session['user'] = {
                "id" : usuario_nuevo.id,
                "name": f"{usuario_nuevo.name}",
                "email": usuario_nuevo.email
            }
            #si se registra bien es redirigido a la pagina de Bienvenido
            return redirect("/muro/")
        #Si tiene algun error lo redirige a la misma pagina
        return redirect("/registro")
    else:

        #Si el metodo es "get" pregunta si está en sesion 
        #Si está lo mantiene en el muro
        if 'user' in request.session:
            messages.warning(request,"Ya estás registrado o logeado.")
            return redirect('/muro/')

        else:   
            #si no está en sesion renderiza la pagina registro.html
            context ={} 
            return render(request, 'registro.html',context)


def logout(request):

    if 'user' in request.session:
        del request.session['user']
        # del request.session['usuario']
    
    return redirect("/login")
@login_required
def editar(request, dato):
# def editar(request):
    if request.method == 'GET':
        
        context = {
        # 'editar' : User.objects.get(id=dato) 
        }

        # data = User.objects.get(id = dato)
        # print(f'{data.updated_at} + "aqui--->"') 
        return render(request, 'editar.html', context)

    if request.method == 'POST':
        # print(f'"este es el popst = "  {request.POST}')
        errors = User.objects.validador_basico(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
        #     # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
                print(errors)
                # request.session['show_titulo'] = request.POST['id']
                
                
                # request.session['name'] = request.POST['name']
                # request.session['email'] =request.POST['email']
                # request.session['show_release_date'] = request.POST['release_date']
                # request.session['show_descripcion'] =request.POST['descripcion']
                
                
        #     # redirigir al usuario al formulario para corregir los errores
            return redirect(f'/editar/{dato}/')

        else:   
            change = User.objects.get(id=dato)
            confirmar=0
            for r in User.objects.exclude(id=dato):
                print(r.email)
                print(change.email)
                if r.email == change.email:
                    confirmar = 1
                    print(confirmar)
            if confirmar == 0:
            # if change.title != request.POST['titulo']:
                print(change, "ok")

            # password_encryp = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 

                change.name = request.POST['name']
                change.email = request.POST['email']

                change.save()
                messages.success(request,"Los datos fueron actualizados exitosamente")

                request.session['user'] = {
                    "id": dato,
                    "name" : change.name,
                    "email": change.email
                }

                print("aqui voy")    
                return redirect("/muro/")

            else:
                print("por aqui")
                messages.warning(request,"EL email ya existe")
                return redirect(f'/editar/{dato}/')

            # change.password =password_encryp


                # change.release_date = request.POST['release_date']
                # change.description = request.POST['descripcion']

            # else:

            #     change.network = request.POST['plataforma']
            #     change.release_date = request.POST['release_date']
            #     change.description = request.POST['descripcion']
            # request.session['name'] = change.name
            # request.session['email'] = change.email
            # request.session['show_release_date'] = ""
            # request.session['show_descripcion'] = ""