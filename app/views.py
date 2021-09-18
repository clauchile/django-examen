from app.models import Cita, Me_gusta, User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http.response import JsonResponse
# import bcrypt, time
# from .decorators import login_required
# # from datetime import datetime, time, timedelta
# from django.utils import timezone




def index(request):
    print(request.session)
    # if 'user' in request.session:
    #         messages.warning(request,"Ya estás logeado.")
    return redirect("/login/")
# @login_required
def muro(request):

    if request.method == 'GET':
      
        # cuenta = Message.objects.filter(user__id = request.session['user']['id']).count()
        # fil = Comment.objects.filter(user__id = request.session['user']['id'])
        context = {
            # 'saludo': 'Hola',
            'cita_list': Cita.objects.order_by('-created_at'),
            # 'comentario_list':Comment.objects.order_by('-created_at'),
            # 'id_delete': fil,
            # 'cuenta': cuenta
        }
        
        return render(request, 'muro.html', context)

    else:
        # errors = Cita.objects.validador_basico(request.POST)
        if not request.POST['autor']:
            messages.warning(request, "Debe escribir el autor")

            return redirect( '/muro/' )    

        if not request.POST['cita']:
            messages.warning(request, "Debe escribir una cita")
            return redirect( '/muro/' )    


        if len( request.POST['autor']) < 4:
            messages.warning(request, "El autor debe tener mas de 3 caracteres")
            return redirect( '/muro/' )    

        if len( request.POST['cita']) < 10:
            messages.warning(request, "La cita debe tener al menos 10 caracteres")
            
              

            return redirect( '/muro/' )    
        # print(request.session.usuario.name)
        else:
            print(request.POST)

            # print(nombre_sesion)
            # val = request.POST.get('')
            usuario = User.objects.get(id = request.session['user']['id'])
            # c = request.POST['comment']
            nueva_cita = Cita.objects.create(
                    
                    autor = request.POST['autor'],
                    cita = request.POST['cita'],
                    user = usuario
            )
            # print(nueva_cita)
            # nueva_cita(save)
            messages.success(request,"Cita publicada")
            return redirect( '/muro/' )

def like(request,val):

    if request.method == 'GET':

        # cuenta= Me_gusta.objects.filter(cita__id = val).filter(user__id = request.session['user']['id']).count()
        # .filter(user__id = request.session['user']['id']).count()

        # 'playerJ' : Player.objects.filter(first_name = "Joshua").filter(all_teams__league__name__contains =
        #  "Atlantic Federation of Amateur Baseball Players") ,

        # if cuenta < 1:
        if not Me_gusta.objects.filter(cita__id = val).filter(user__id = request.session['user']['id']):
            # print('la cuenta es ',cuenta)
            usuario = User.objects.get(id = request.session['user']['id'])
            nuevo_like = Me_gusta.objects.create(
                        megusta = 'True',
                        cita = Cita.objects.get(id = val),
                        user = usuario,
                )
            context = {
                'saludo': 'Hola',

                'megusta': nuevo_like,
                    # 'comentario_list': Comment.objects.all().order_by('-created_at'),
                    # 'mensaje_list': Message.objects.all().order_by('-created_at'),
                    # 'cuenta': Message.objects.filter(user__id = request.session['user']['id']).count()
                }
                
                # return render(request, 'muro.html', context)
            return redirect("/muro/")
        else:
            messages.error(request, "Ya dio like a esta cita")

            return redirect("/muro/")
            print(request.POST)
           
    #         usuario = User.objects.get(id = request.session['user']['id'])
    #         msg = Message.objects.get(id = request.POST['msgnum'])
           
    #         nuevo_Comentario = Comment.objects.create(
    #                 comentario = request.POST['comentario'],
    #                 message = msg,
    #                 user = usuario,
    #         )
    #         print(nuevo_Comentario)
    #         messages.success(request,"comentario publicado")
    #     return redirect( f'/muro/{val}/' )

def cita_delete(request,num):
    # elim = Cita.objects.get(id = num)
    # elim.delete()
    # messages.success(request, "La cita fue eliminada")

   
    return redirect('/muro/')

def cita_delete_ajax(request, num):
    elim = Cita.objects.get(id = num)
    elim.delete()

    contexto = {
        'saludo' : 'hola'
        # 'resultado':True,
        # 'nombre' : curso.nombre,
        # 'descripcion' : curso.descripcion
    }
    # messages.success(request, "La cita fue eliminada")

    return JsonResponse(contexto)
        

def cita_usuario(request, num): 
    
    if request.method == 'GET':
        # elim = Cita.objects.filter(id__ = request.session['user'][num])
        citauser = Cita.objects.filter(user__id = num)
        usuariocita = User.objects.get(id= num)
        print(citauser)
        context = {
            # 'saludo': 'Hola',
            # 'cita_list': Cita.objects.get(id = num).order_by('-created_at'),
            'cita_list': citauser,
            'usuario': usuariocita
            # 'comentario_list':Comment.objects.order_by('-created_at'),
            # 'id_delete': fil,
            # 'cuenta': cuenta
        }
        
        return render(request, 'citasdeusuario.html', context)

    else:

        if not request.POST['cita']:
            messages.warning(request, "Debe escribir una cita")
            return redirect( '/muro/' )    

        elif not request.POST['autor']:
            messages.warning(request, "Debe escribir el autor")

            return redirect( '/muro/' )    

        elif len( request.POST['autor']) < 4:
            messages.warning(request, "El autor debe tener mas de 3 caracteres")
            return redirect( '/muro/' )    

        elif len( request.POST['cita']) < 10:
            messages.warning(request, "La cita debe tener al menos 10 caracteres")
            


            return redirect( '/muro/' )    
        # print(request.session.usuario.name)
        else:
            print(request.POST)

            usuario = User.objects.get(id = request.session['user']['id'])

            nueva_cita = Cita.objects.create(
                    
                    autor = request.POST['autor'],
                    cita = request.POST['cita'],
                    user = usuario
            )
            print(nueva_cita)
            # nueva_cita(save)
            messages.success(request,"Mensaje publicado")
            return redirect( '/muro/' )   






#             # datos = request.POST[]
# @login_required
# def delete(request,num):

#     dato = Comment.objects.get(id=num)

#     dato.delete()
#     messages.success(request, f" el comentario ha sido borrado con exito")
#     return redirect(f'/muro')
# @login_required


# def calculate_minutos(fecha):
#     today = timezone.now()

#     resultado = (today.year - fecha.year)*3652460 + (today.month - fecha.month)*302460 + (today.day - fecha.day)*2460 + (today.hour-fecha.hour)*60 + (today.minute-fecha.minute)
#     print(resultado)
#     return resultado

