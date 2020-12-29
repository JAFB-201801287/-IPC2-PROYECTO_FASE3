from django.shortcuts import render, redirect
from .forms import *
import MySQLdb
from django.db.models import Q
from random import choice
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

#-------------------------------------------------------------------------------------------------------------
def login(request):
    form = inicio_sesion()
    texto_boton = "INICIAR SESION"
    variables = {
        "texto_boton": texto_boton,
        "form": form
    }
    if (request.method == "POST"):
        form = inicio_sesion(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            nombre_usuario = datos.get("nombre_usuario")
            contrasena = datos.get("contrasena")

            if((nombre_usuario == 'admin') and (contrasena == 'root1234')):
                return redirect('/administrador/cliente/')

            form = inicio_sesion()
            variables = {
                "texto_boton": texto_boton,
                "form": form
            }
        else:
            variables = {
                "texto_boton": texto_boton,
                "form": form
            }
    return render(request, 'administrador/login/index.html', variables)

#-------------------------------------------------------------------------------------------------------------
def lista_cliente(request):
    titulo_pantalla = "CLIENTES INDIVIDUALES"
    a = Cliente.objects.all().values_list()  # devuelve una lista

    if not a:
        print("NO HAY CLIENTES")
    variables = {
        "titulo" : titulo_pantalla,
        "lista": a
    }
    return render(request, 'administrador/cliente/index.html',variables)

# AGREGAR CLIENTE
#-------------------------------------------------------------------------------------------------------------
def agregar_cliente(request):
    form = cliente()
    titulo_pantalla = "AGREGAR NUEVO CLIENTE INDIVIDUAL"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cliente'
    mensaje_error = ""
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }
    if (request.method == "POST"):
        form = cliente(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            nombre_usuario = datos.get("nombre_usuario")
            contrasena = datos.get("contrasena")
            cui = datos.get("cui")
            nit = datos.get("nit")
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            fecha_nacimiento = datos.get("fecha_nacimiento")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Cliente(cui, nit, nombre, apellido, fecha_nacimiento) VALUES('" + str(cui) + "', '" + str(nit) + "', '" + nombre + "', '" + apellido +"', '" + fecha_nacimiento + "');"
            c.execute(consulta)
            db.commit()
            c.close()

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Usuario(nombre, contrasena, cui, intentos) VALUES('" + nombre_usuario + "', '" + contrasena + "', '" + str(cui) + "', '0');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = cliente()
            mensaje_error = "SE CREO EL CLIENTE INDIVIDUAL"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
        else:
            nombre= "INFORMACION INVALIDA"
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
    return render(request, 'administrador/formulario.html', variables)

#-------------------------------------------------------------------------------------------------------------
def lista_empresa(request):
    titulo_pantalla = "CLIENTES EMPRESARIALES"
    empresas = Empresa.objects.all()  # devuelve una lista

    if not empresas:
        print("NO HAY EMPRESAS")
    variables = {
        "titulo" : titulo_pantalla,
        "empresas": empresas
    }
    return render(request, 'administrador/empresa/index.html',variables)

# AGREGAR EMPRESA
#-------------------------------------------------------------------------------------------------------------
def agregar_empresa(request):
    form = empresa()
    titulo_pantalla = "AGREGAR NUEVO CLIENTE EMPRESARIAL"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_empresa'
    mensaje_error = ""
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }
    if (request.method == "POST"):
        form = empresa(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre_usuario = datos.get("nombre_usuario")
            contrasena = datos.get("contrasena")
            nombre = datos.get("nombre")
            nombre_comercial = datos.get("nombre_comercial")
            nombre_representante = datos.get("nombre_representante")
            tipo_empresa = datos.get("tipo_empresa")
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Empresa(nombre, nombre_comercial, nombre_representante, tipo_empresa) VALUES('" + nombre + "', '" + nombre_comercial + "', '" + nombre_representante + "', '" + tipo_empresa + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            id_empresa = Empresa.objects.last().id_empresa
            consulta = "INSERT INTO Usuario(nombre, contrasena, id_empresa, intentos) VALUES('" + nombre_usuario + "', '" + contrasena + "', '" + str(id_empresa) + "', '0');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = empresa()
            mensaje_error = "SE CREO EL CLIENTE EMPRESARIAL"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
        else:
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
    return render(request, 'administrador/formulario.html', variables)

#-------------------------------------------------------------------------------------------------------------
def lista_cuenta(request):
    titulo_pantalla = "CUENTAS"
    a = Cuenta.objects.all().select_related('id_usuario').order_by('id_cuenta') # devuelve una lista
    print(a)

    if not a:
        print("NO HAY CLIENTES")
    variables = {
        "titulo" : titulo_pantalla,
        "lista": a
    }
    return render(request, 'administrador/cuenta/index.html',variables)

# AGREGAR CUENTA
#-------------------------------------------------------------------------------------------------------------
def agregar_cuenta(request):
    form = cuenta()
    titulo_pantalla = "ABRIR CUENTA PARA CLIENTE"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cuenta'
    mensaje_error = ""
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }
    if (request.method == "POST"):
        form = cuenta(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            tipo_cuenta = datos.get("tipo_cuenta")
            tipo_moneda = datos.get("tipo_moneda")
            usuario = datos.get("usuario")
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Cuenta(monto, tipo_cuenta, tipo_moneda, id_usuario, estado) VALUES('" + str(monto) + "', '" + tipo_cuenta + "', '" + tipo_moneda + "', '" + str(usuario.id_usuario) + "', 'ACTIVA');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = cuenta()
            mensaje_error = "SE CREO LA CUENTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
        else:
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
                
            }
    return render(request, 'administrador/formulario.html', variables)

#-------------------------------------------------------------------------------------------------------------
def deposito(request):
    form = transaccion()
    titulo_pantalla = "DEPOSITO DE MONETARIO EN CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cuenta'
    mensaje_error = ""
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }
    if (request.method == "POST"):
        form = transaccion(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            tipo_moneda = datos.get("tipo_moneda")
            cuenta = datos.get("cuenta")

            if(cuenta.tipo_moneda == tipo_moneda):
                monto_anterior = cuenta.monto
                monto_despues = (cuenta.monto + monto)
            elif(cuenta.tipo_moneda == 'DOLLAR' and tipo_moneda == 'QUETZAL'):
                monto_anterior = cuenta.monto
                monto_despues = (cuenta.monto + (monto/7.87))
            elif(cuenta.tipo_moneda == 'QUETZAL' and tipo_moneda == 'DOLLAR'):
                monto_anterior = cuenta.monto
                monto_despues = (cuenta.monto + (monto*7.60))

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto_anterior) + "', '" + str(monto_despues) + "', '" + tipo_moneda + "', 'DEPOSITO', '" + str(cuenta.id_cuenta) +"');"
            c.execute(consulta)
            db.commit()
            c.close()

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "UPDATE Cuenta SET monto = '" + str(monto_despues) + "' WHERE id_cuenta = '" + str(cuenta.id_cuenta) + "';"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = transaccion()
            mensaje_error = "EL DEPOSITO SE EFECTUO CON EXITO"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
        else:
            mensaje_error = "ERROR NO SE PUDO HACER EL DEPOSITO"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
    return render(request, 'administrador/formulario.html', variables)

#-------------------------------------------------------------------------------------------------------------
def agregar_chequera(request):
    form = chequera()
    titulo_pantalla = "CREACION DE CHEQUERA"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cuenta'
    mensaje_error = ""
    mensaje_error = ""
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }
    if (request.method == "POST"):
        form = chequera(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cuenta = datos.get("cuenta")
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos

            flag = True
            for che in Chequera.objects.all().filter(id_cuenta=cuenta.id_cuenta):
                if(che.acabada == "EN USO"):
                    flag = False

            if(flag):
                db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "INSERT INTO Chequera(acabada, id_cuenta) VALUES('EN USO', '" + str(cuenta.id_cuenta) + "');"
                c.execute(consulta)
                db.commit()
                c.close()

                temp = Chequera.objects.last()

                for i in range(20):
                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "INSERT INTO Cheque(monto, autorizado, disponible, id_chequera, nombre) VALUES('0', 'NO', 'SI', '" + str(temp.id_chequera) + "', 'VACIO');"
                    c.execute(consulta)
                    db.commit()
                    c.close()
                mensaje_error = f"SE CREO LA CHEQUERA CODIGO { str(temp.id_chequera) } CON 20 CHEQUES"
            else:
                mensaje_error = "ERROR CHEQUERA EN USO"
            
            form = chequera()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
        else:
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
    return render(request, 'administrador/formulario.html', variables)

#-------------------------------------------------------------------------------------------------------------
def lista_usuarios(request):
    titulo_pantalla = "USUARIOS"
    usuarios = Usuario.objects.all()  # devuelve una lista

    if not usuarios:
        print("NO HAY USUARIOS")
    variables = {
        "titulo" : titulo_pantalla,
        "usuarios": usuarios
    }
    return render(request, 'administrador/usuario/index.html',variables)

#-------------------------------------------------------------------------------------------------------------
def activar_usuario(request):
    form = usuario()
    form.fields['usuario'].queryset = Usuario.objects.all().filter(intentos__gte=3)

    titulo_pantalla = "ACTIVAR USUARIO"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_usuario'
    mensaje_error = ""

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }

    if (request.method == "POST"):
        form = usuario(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usu = datos.get("usuario")
            longitud = 6
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
            p1 = ""
            p1 = p1.join([choice(valores) for i in range(longitud)])

            longitud = 2
            valores = "0123456789"
            p2 = ""
            p2 = p2.join([choice(valores) for i in range(longitud)])

            longitud = 2
            valores = "<=>@#%&+"
            p3 = ""
            p3 = p3.join([choice(valores) for i in range(longitud)])

            contrasena = p1 + p2 + p3

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "UPDATE Usuario SET intentos = '0', contrasena = '" + contrasena + "' WHERE id_usuario = '" + str(usu.id_usuario) + "';"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()

            form = usuario()
            form.fields['usuario'].queryset = Usuario.objects.all().filter(intentos__gte=3)
            mensaje_error = f"SE ACTIVO CON EXITO EL USUARIO ( CONTRASEÑA: { contrasena } )"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
        else:
            form.fields['usuario'].queryset = Usuario.objects.all().filter(intentos__gte=3)
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
    return render(request, 'administrador/formulario.html', variables)


def cobrar_cheque(request):
    form = a_correlativo()
    titulo_pantalla = "COBRAR CHEQUE"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cuenta'
    mensaje_error = ""
    mensaje_error = ""
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }
    if (request.method == "POST"):
        form = a_correlativo(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            correlativo = datos.get("correlativo")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos

            try:
                cheque =  Cheque.objects.select_related('id_chequera').get(id_cheque = correlativo)
                if(cheque.autorizado == "SI"):

                    id_cuenta = cheque.id_chequera.id_cuenta.id_cuenta
                    monto_anterior = cheque.id_chequera.id_cuenta.monto
                    monto_despues = (cheque.id_chequera.id_cuenta.monto - cheque.monto)
                    tipo_moneda = cheque.id_chequera.id_cuenta.tipo_moneda
                    monto= cheque.monto

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "UPDATE Cheque SET disponible = 'NO' WHERE id_cheque = '" + str(correlativo) + "';"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "UPDATE Cuenta SET monto = '" + str(monto_despues) + "' WHERE id_cuenta = '" + str(id_cuenta) + "';"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto_anterior) + "', '" + str(monto_despues) + "', '" + tipo_moneda + "', 'CHEQUE', '" + str(id_cuenta) +"');"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    mensaje_error = "SE COBRO EL CHEQUE"
            except ObjectDoesNotExist:
                print('No existe')
                mensaje_error = "NO SE PUDO COBRAR EL CHEQUE"
            
            form = a_correlativo()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
        else:
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje_error": mensaje_error
            }
    return render(request, 'administrador/formulario.html', variables)