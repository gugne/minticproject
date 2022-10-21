from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def registrarse (request):
    if request.method == 'POST':
        #Valores de los formularios
        nombres = request.POST['nombres']#name= del html
        apellidos = request.POST['apellidos']
        usuario = request.POST['usuario']
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        contraseña2 = request.POST['contraseña2']
        
    #Comprobar si la contraseña coincide
        if contraseña == contraseña2:
            #Verificar que no exista usuario
            if User.objects.filter(username=usuario).exists(): #username(primero la db)= usuario (variable creada arriba con el POST)
                #si el usuario existe, muestra alerta
                messages.error(request, 'El usuario escogido ya está en uso.')
                return redirect ('registrarse')
            else:
                #si el usuario no existe, checa el correo electrónico
                if User.objects.filter(email=email).exists():
                    #si el correo  existe, muestra alerta
                    messages.error(request, 'El correo electrónico elegido ya está en uso.')
                    return redirect ('registrarse')
                else:
                    #Todo en orden
                    usuario = User.objects.create_user(username=usuario, password=contraseña, email=email, first_name=nombres, last_name=apellidos )
                    #crea el usuario, ahora podemos autenticar directamente o enviar a página de loggeo
                    #loggear después de registrar
                        #auth.login(request, usuario)
                        #messages.success(request, 'Felicidades, ahora estás loggeado.') #este mensaje sale pero al ir al /admin, toca mirar como ponerlo en la vista 
                        #return redirect ( 'index' )
                    #No loggear
                    usuario.save();
                    messages.success(request, 'Felicidades, usuario registrado. Ya puedes ingresar.')
                    return redirect ('ingresar')
                     
        #Si las contraseñas no coinciden, muestra alerta y vuelte al formulario
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect ('registrarse')
    #eing?
    else:
        return render (request, 'usuarios/registrarse.html')

def ingresar (request):
    if request.method == 'POST':
        usuario = request.POST['usuario']#name= del html
        contraseña = request.POST['contraseña']
        
        #compara db con variables.POST
        usuario= auth.authenticate(username=usuario, password=contraseña)
        
        #Si usuario no es null
        if usuario is not None:
            #loggea
            auth.login(request, usuario)
            messages.success(request, 'Sesión iniciada exitosamente!.')
            return redirect ('dashboard')
        else:
            #no match
            messages.error(request, 'Credenciales incorrectas, intente nuevamente')
            return redirect ( 'ingresar' )
    #eing?
    else:
        return render (request, 'usuarios/ingresar.html')

def salir (request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Tu sesión se ha cerrado exitosamente.')
    return redirect ('index')

def dashboard (request):
    return render (request, 'usuarios/dashboard.html')