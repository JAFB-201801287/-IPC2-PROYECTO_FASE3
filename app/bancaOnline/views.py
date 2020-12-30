from django.shortcuts import render, redirect
from .forms import *
import MySQLdb
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def index(request):
    return render(request, 'index.html')

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


            try:
                user = Usuario.objects.get(nombre = nombre_usuario)
                if(user.contrasena == contrasena and user.intentos < 3):
                    request.session["user"] = user.id_usuario

                    if(user.id_empresa != None):
                        request.session["esEmpresa"] = True
                    else:
                        request.session["esEmpresa"] = False

                    return redirect('/cliente/inicio/')
                else: 
                    intentos = user.intentos + 1
                    id_usuario = user.id_usuario
                    host = 'localhost'
                    db_name = 'banca_virtual'
                    user = 'root'
                    contra = 'FloresB566+'
                    #puerto = 3306
                    #Conexion a base de datos sin uso de modulos

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "UPDATE Usuario SET intentos = '" + str(intentos) + "' WHERE id_usuario = '" + str(id_usuario)  + "';"
                    c.execute(consulta)
                    db.commit()
                    c.close()
            except ObjectDoesNotExist:
                print('No existe')

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
    return render(request, 'cliente/login/index.html', variables)

def inicio(request):
    id_usuario = request.session['user']
    user = Usuario.objects.get(id_usuario=id_usuario)
    titulo_pantalla = f"CUENTAS DEL USUARIO NO. { str( user.id_usuario ) }"
    cuentas = Cuenta.objects.all().filter(id_usuario= user.id_usuario)
    prestamos = Prestamo.objects.select_related('id_usuario').all().filter(id_usuario=id_usuario) # devuelve una lista


    form = estado()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    variables = {
        "titulo" : titulo_pantalla,
        "cuentas": cuentas,
        "prestamos": prestamos,
        "user": user,
        "form": form
    }

    if (request.method == "POST"):
        form = estado(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cuenta = datos.get("cuenta")

            request.session['id_cuenta'] = cuenta.id_cuenta

            return redirect('/cliente/cuenta/estado/')
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "cuentas": cuentas,
                "prestamos": prestamos,
                "user": user,
                "form": form
            }
    return render(request, 'cliente/inicio/index.html', variables)


def deposito(request):
    id_usuario = request.session['user']

    form = transaccion()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    titulo_pantalla = "DEPOSITO MONETARIO EN CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
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
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario)
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario)
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)

def activar_cuenta(request):
    id_usuario = request.session['user']

    form = estado()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='SUSPENDIDA')

    titulo_pantalla = "ACTIVAR CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }

    if (request.method == "POST"):
        form = estado(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cuenta = datos.get("cuenta")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('0', '" + str(cuenta.monto) + "', '" + str(cuenta.monto) + "', '" + cuenta.tipo_moneda + "', 'ACTIVAR CUENTA', '" + str(cuenta.id_cuenta) +"');"
            c.execute(consulta)
            db.commit()
            c.close()

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "UPDATE Cuenta SET estado = 'ACTIVA' WHERE id_cuenta = '" + str(cuenta.id_cuenta) + "';"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()

            form = estado()
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='SUSPENDIDA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='SUSPENDIDA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)

def suspender_cuenta(request):
    id_usuario = request.session['user']

    form = estado()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    titulo_pantalla = "SUSPENDER CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }

    if (request.method == "POST"):
        form = estado(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cuenta = datos.get("cuenta")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('0', '" + str(cuenta.monto) + "', '" + str(cuenta.monto) + "', '" + cuenta.tipo_moneda + "', 'SUSPENDER CUENTA', '" + str(cuenta.id_cuenta) +"');"
            c.execute(consulta)
            db.commit()
            c.close()

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "UPDATE Cuenta SET estado = 'SUSPENDIDA' WHERE id_cuenta = '" + str(cuenta.id_cuenta) + "';"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()

            form = estado()
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)

def transferencia_propias(request):
    id_usuario = request.session['user']

    form = cuentas_propias()
    form.fields['cuenta1'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
    form.fields['cuenta2'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    titulo_pantalla = "TRANSACCIONES ENTRE CUENTAS PROPIAS"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'
    mensaje = ''

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje": mensaje
    }

    if (request.method == "POST"):
        form = cuentas_propias(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            cuenta1 = datos.get("cuenta1")
            cuenta2 = datos.get("cuenta2")
            if(cuenta1.id_cuenta != cuenta2.id_cuenta):
                if(cuenta1.tipo_moneda == cuenta2.tipo_moneda):
                    monto1_anterior = cuenta1.monto
                    monto1_despues = (cuenta1.monto - monto)
                    monto2_anterior = cuenta2.monto
                    monto2_despues = (cuenta2.monto + monto)
                elif(cuenta1.tipo_moneda == 'DOLLAR' and cuenta2.tipo_moneda == 'QUETZAL'):
                    monto1_anterior = cuenta1.monto
                    monto1_despues = (cuenta1.monto - (monto/7.87))
                    monto2_anterior = cuenta2.monto
                    monto2_despues = (cuenta2.monto + (monto/7.87))
                elif(cuenta1.tipo_moneda == 'QUETZAL' and cuenta2.tipo_moneda == 'DOLLAR'):
                    monto1_anterior = cuenta1.monto
                    monto1_despues = (cuenta1.monto - (monto*7.60))
                    monto2_anterior = cuenta2.monto
                    monto2_despues = (cuenta2.monto + (monto*7.60))

                host = 'localhost'
                db_name = 'banca_virtual'
                user = 'root'
                contra = 'FloresB566+'
                #puerto = 3306
                #Conexion a base de datos sin uso de modulos

                db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto1_anterior) + "', '" + str(monto1_despues) + "', '" + cuenta1.tipo_moneda + "', 'EMISION DE TRANSFERENCIA', '" + str(cuenta1.id_cuenta) +"');"
                c.execute(consulta)
                db.commit()
                c.close()

                db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "UPDATE Cuenta SET monto = '" + str(monto1_despues) + "' WHERE id_cuenta = '" + str(cuenta1.id_cuenta) + "';"
                c.execute(consulta)
                db.commit()
                c.close()

                db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto2_anterior) + "', '" + str(monto2_despues) + "', '" + cuenta1.tipo_moneda + "', 'RESEPCION DE TRANSFERENCIA', '" + str(cuenta2.id_cuenta) +"');"
                c.execute(consulta)
                db.commit()
                c.close()

                db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                c = db.cursor()
                consulta = "UPDATE Cuenta SET monto = '" + str(monto2_despues) + "' WHERE id_cuenta = '" + str(cuenta2.id_cuenta) + "';"
                c.execute(consulta)
                db.commit()
                c.close()
                #form.save()
                mensaje = "SE LOGRO HACER EL TRASPASO MONETARIO ENTRE CUENTAS"
            else:
                mensaje = "ERROR A ESCOGIDO LA MISMA CUENTA PARA HACER LA TRANSACCION"

            form = cuentas_propias()
            form.fields['cuenta1'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            form.fields['cuenta2'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
        else:
            form.fields['cuenta1'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            form.fields['cuenta2'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
    return render(request, 'cliente/formulario/index.html', variables)

def transferencia_terceros(request):
    id_usuario = request.session['user']

    form = cuentas_terceros()
    form.fields['cuenta1'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    titulo_pantalla = "TRANSACCIONES ENTRE CUENTAS PROPIAS"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'
    mensaje = ''

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje": mensaje
    }

    if (request.method == "POST"):
        form = cuentas_terceros(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            cuenta1 = datos.get("cuenta1")
            no_cuenta = datos.get("no_cuenta")

            try:
                cuenta2 = Cuenta.objects.get(id_cuenta = no_cuenta)
                if(cuenta1.id_cuenta != cuenta2.id_cuenta):
                    if(cuenta1.tipo_moneda == cuenta2.tipo_moneda):
                        monto1_anterior = cuenta1.monto
                        monto1_despues = (cuenta1.monto - monto)
                        monto2_anterior = cuenta2.monto
                        monto2_despues = (cuenta2.monto + monto)
                    elif(cuenta1.tipo_moneda == 'DOLLAR' and cuenta2.tipo_moneda == 'QUETZAL'):
                        monto1_anterior = cuenta1.monto
                        monto1_despues = (cuenta1.monto - (monto/7.87))
                        monto2_anterior = cuenta2.monto
                        monto2_despues = (cuenta2.monto + (monto/7.87))
                    elif(cuenta1.tipo_moneda == 'QUETZAL' and cuenta2.tipo_moneda == 'DOLLAR'):
                        monto1_anterior = cuenta1.monto
                        monto1_despues = (cuenta1.monto - (monto*7.60))
                        monto2_anterior = cuenta2.monto
                        monto2_despues = (cuenta2.monto + (monto*7.60))

                    host = 'localhost'
                    db_name = 'banca_virtual'
                    user = 'root'
                    contra = 'FloresB566+'
                    #puerto = 3306
                    #Conexion a base de datos sin uso de modulos

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto1_anterior) + "', '" + str(monto1_despues) + "', '" + cuenta1.tipo_moneda + "', 'EMISION DE TRANSFERENCIA', '" + str(cuenta1.id_cuenta) +"');"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "UPDATE Cuenta SET monto = '" + str(monto1_despues) + "' WHERE id_cuenta = '" + str(cuenta1.id_cuenta) + "';"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto2_anterior) + "', '" + str(monto2_despues) + "', '" + cuenta1.tipo_moneda + "', 'RESEPCION DE TRANSFERENCIA', '" + str(cuenta2.id_cuenta) +"');"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "UPDATE Cuenta SET monto = '" + str(monto2_despues) + "' WHERE id_cuenta = '" + str(cuenta2.id_cuenta) + "';"
                    c.execute(consulta)
                    db.commit()
                    c.close()
                    #form.save()
                    mensaje = "SE LOGRO HACER EL TRASPASO MONETARIO ENTRE CUENTAS"
                else:
                    mensaje = "ERROR A ESCOGIDO LA MISMA CUENTA PARA HACER LA TRANSACCION"
            except ObjectDoesNotExist:
                mensaje = "ERROR NO EXISTE EL NUMERO DE CUENTA"

            form = cuentas_terceros()
            form.fields['cuenta1'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
        else:
            form.fields['cuenta1'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            mensaje = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
    return render(request, 'cliente/formulario/index.html', variables)

def cliente_chequera(request):
    id_usuario = request.session['user']

    form = estado()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    titulo_pantalla = "ESCOGER CUENTA DE CHEQUERA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }

    if (request.method == "POST"):
        form = estado(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cuenta = datos.get("cuenta")

            request.session["cuenta"] = cuenta.id_cuenta
            return redirect('/cliente/chequera1/')
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='SUSPENDIDA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)

def cliente_chequera1(request):
    id_cuenta = request.session['cuenta']

    form = c_chequera()
    form.fields['chequera'].queryset = Chequera.objects.all().filter(id_cuenta=id_cuenta)

    titulo_pantalla = "ESCOGER CHEQUERA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_chequera'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }

    if (request.method == "POST"):
        form = c_chequera(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            chequera = datos.get("chequera")

            request.session["chequera"] = chequera.id_chequera
            return redirect('/cliente/chequera2/')
        else:
            form.fields['chequera'].queryset = Chequera.objects.all().filter(id_cuenta=id_cuenta)
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)


def cliente_chequera2(request):
    id_chequera = request.session['chequera']

    form = c_cheque()
    form.fields['cheque'].queryset = Cheque.objects.all().filter(id_chequera=id_chequera)
    cheques = Cheque.objects.all().filter(id_chequera=id_chequera).select_related('id_chequera')

    titulo_pantalla = "ESCOGER CHEQUE"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_chequera1'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "cheques": cheques
    }

    if (request.method == "POST"):
        form = c_cheque(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cheque = datos.get("cheque")

            request.session["cheque"] = cheque.id_cheque
            return redirect('/cliente/cheque/')
        else:
            form.fields['cheque'].queryset = Cheque.objects.all().filter(id_chequera=id_chequera)
            cheques = Cheque.objects.all().filter(id_chequera=id_chequera)
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "cheques": cheques
            }
    return render(request, 'cliente/chequera/index.html', variables)


def cliente_cheque(request):
    id_cheque = request.session['cheque']

    form = c_monto()
    #form.fields['cheque'].queryset = Cheque.objects.all().filter(id_chequera=id_chequera)

    titulo_pantalla = "PRE-AUTORIZACION DE CHUEQUES"
    texto_boton = "AUTORIZAR"
    regresar = 'cliente_chequera2'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }

    if (request.method == "POST"):
        form = c_monto(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            nombre = datos.get("nombre")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos            

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = f"UPDATE Cheque SET nombre = '" + nombre + "', monto = '" + str(monto) + "', autorizado = 'SI' WHERE id_cheque = '" + str(id_cheque) + "';"
            c.execute(consulta)
            db.commit()
            c.close()

            return redirect('/cliente/chequera2/')
        else:
            #form.fields['cheque'].queryset = Cheque.objects.all().filter(id_chequera=id_chequera)
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)
    

def lista_prestamo(request):
    id_usuario = request.session['user']
    user = Usuario.objects.get(id_usuario=id_usuario)
    titulo_pantalla = f"PRESTAMOS DEL USUARIO NO. { str(user.id_usuario) }"
    prestamos = Prestamo.objects.select_related('id_usuario').all().filter(id_usuario=id_usuario)
    pagos_prestamo = Pagoprestamo.objects.all()
    bandera = False


    form = buscar_prestamo()
    form.fields['prestamos'].queryset = Prestamo.objects.all().filter(id_usuario=id_usuario)

    variables = {
        "titulo" : titulo_pantalla,
        "prestamos": prestamos,
        "user": user,
        "form": form,
        "pagos_prestamo": pagos_prestamo,
        "bandera": bandera
    }

    if (request.method == "POST"):
        form = buscar_prestamo(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            prestamo = datos.get("prestamos")

            pagos_prestamo = Pagoprestamo.objects.select_related().all().filter(id_prestamo=prestamo.id_prestamo)
            request.session['prestamo'] = prestamo.id_prestamo
            bandera = True

            form.fields['prestamos'].queryset = Prestamo.objects.all().filter(id_usuario=id_usuario)
            variables = {
                "titulo" : titulo_pantalla,
                "prestamos": prestamos,
                "user": user,
                "form": form,
                "pagos_prestamo": pagos_prestamo,
                "bandera": bandera
            }
        else:
            bandera = False
            form.fields['prestamos'].queryset = Prestamo.objects.all().filter(id_usuario=id_usuario)
            variables = {
                "titulo" : titulo_pantalla,
                "prestamos": prestamos,
                "user": user,
                "form": form,
                "pagos_prestamo": pagos_prestamo,
                "bandera": bandera
            }
    return render(request, 'cliente/prestamo/index.html', variables)

def agregar_prestamo(request):
    id_usuario = request.session['user']
    form = prestamo()
    titulo_pantalla = "PEDIR PRESTAMO"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_prestamo'
    mensaje_error = ""
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje_error": mensaje_error
    }
    if (request.method == "POST"):
        form = prestamo(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            tipo_prestamo = datos.get("tipo_prestamo")
            descripcion = datos.get("descripcion")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306

            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Prestamo(monto, descripcion, tipo_prestamo, id_usuario) VALUES('" + str(monto) + "', '" + descripcion + "', '" + tipo_prestamo +"', '" + str(id_usuario) + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()

            form = prestamo()
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
    return render(request, 'cliente/formulario/index.html', variables)

def auto_prestamo(request):
    id_usuario = request.session['user']

    form = prestamo_automatico()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
    form.fields['prestamos'].queryset = Prestamo.objects.all().filter(id_usuario=id_usuario).filter(aprobado='SI')

    titulo_pantalla = "PAGO DE CUOTA DE PRESTAMO AUTOMATICO"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_prestamo'
    mensaje = ''

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje": mensaje
    }

    if (request.method == "POST"):
        form = prestamo_automatico(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            cuenta = datos.get("cuenta")
            prestamo = datos.get("prestamos")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO PrestamoAutomatico(monto, id_prestamo, id_cuenta) VALUES('" + str(monto) +"', '" + str(prestamo.id_prestamo) + "', '" + str(cuenta.id_cuenta) + "');"
            c.execute(consulta)
            db.commit()
            c.close()


            mensaje = "SE A CREADO EL PAGO DE PRESTAMO AUTOMATICO"

            form = prestamo_automatico()
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            form.fields['prestamos'].queryset = Prestamo.objects.all().filter(id_usuario=id_usuario).filter(aprobado='SI')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            form.fields['prestamos'].queryset = Prestamo.objects.all().filter(id_usuario=id_usuario).filter(aprobado='SI')
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
    return render(request, 'cliente/formulario/index.html', variables)

def pagar_automatico(request): 
    id_usuario = request.session['user']
    id_prestamo = request.session['prestamo'] 
    form = inicio_sesion()
    titulo_pantalla = "PAGO AUTOMATICO PRESTAMO NO. " + str(id_prestamo)
    texto_boton = "ACEPTAR"
    regresar = 'cliente_prestamo'
    mensaje = ''
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje": mensaje
    }
    if (request.method == "POST"):
        form = inicio_sesion(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            nombre_usuario = datos.get("nombre_usuario")
            contrasena = datos.get("contrasena")


            try:
                host = 'localhost'
                db_name = 'banca_virtual'
                user = 'root'
                contra = 'FloresB566+'

                usuario = Usuario.objects.get(id_usuario = id_usuario)

                pa = Prestamoautomatico.objects.filter(id_prestamo = id_prestamo).select_related('id_prestamo').last()
                if(usuario.contrasena == contrasena):
                    monto_despues = (pa.id_prestamo.monto - pa.monto)
                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(pa.monto) + "', '" + str(pa.id_cuenta.monto) + "', '" + str(monto_despues) + "', '" + pa.id_cuenta.tipo_moneda + "', 'PAGO PRESTAMO', '" + str(pa.id_cuenta.id_cuenta) +"');"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "UPDATE Prestamo SET monto = '" + str(monto_despues) + "' WHERE id_prestamo = '" + str(pa.id_prestamo.id_prestamo) +"';"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "INSERT INTO PagoPrestamo(monto, interes, tipo_pago, id_prestamo, id_cuenta) VALUES('" + str(pa.monto) + "', '0', 'PAGO AUTOMATICO', '" + str(id_prestamo) + "', '" + str(pa.id_cuenta.id_cuenta) + "');"
                    c.execute(consulta)
                    db.commit()
                    c.close()

                    mensaje = f"SE A PAGADO { str(pa.monto) }"
                else: 
                    mensaje = "ERROR CREDENCIALES DE USUARIO NO ACEPTADAS"
            except ObjectDoesNotExist:
                print('No existe')

            form = inicio_sesion()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
        else:
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
    return render(request, 'cliente/formulario/index.html', variables)


def estado_cuenta(request):
    id_cuenta = request.session['id_cuenta']
    titulo_pantalla = "DETALLE CUENTA"

    try:
        cuenta_cliente = Cuenta.objects.get(id_cuenta=id_cuenta) 
        transacciones = Transaccion.objects.all().select_related('id_cuenta').filter(id_cuenta=id_cuenta)
    except ObjectDoesNotExist:
        print("NO HAY")

    variables = {
        "titulo" : titulo_pantalla,
        "cuenta_cliente": cuenta_cliente,
        "transacciones": transacciones
    }
    return render(request, 'cliente/cuenta/index.html',variables)

def lista_proveedores(request):
    titulo_pantalla = "PROVEEDORES"
    id_usuario = request.session['user']

    try:
        usuario = Usuario.objects.select_related('id_empresa').get(id_usuario=id_usuario)
        proveedores = Proveedor.objects.select_related('id_cuenta').filter(id_empresa=usuario.id_empresa.id_empresa)
    except ObjectDoesNotExist:
        print("NO HAY")

    variables = {
        "titulo" : titulo_pantalla,
        "proveedores": proveedores
    }
    return render(request, 'cliente/proveedor/index.html',variables)

def agregar_proveedor(request):
    id_usuario = request.session['user']
    usuario = ''

    try:
        usuario = Usuario.objects.select_related('id_empresa').get(id_usuario=id_usuario)
    except ObjectDoesNotExist:
        print("NO HAY")


    form = proveedor()
    form.fields['cuenta'].queryset = Cuenta.objects.all().exclude(id_usuario=id_usuario).filter(estado='ACTIVA').exclude(id_usuario__id_empresa__id_empresa=usuario.id_empresa.id_empresa).exclude(id_usuario__id_empresa__id_empresa=None)

    titulo_pantalla = "AGREGAR PROVEEDOR"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_proveedor'
    mensaje = ''

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form,
        "mensaje": mensaje
    }

    if (request.method == "POST"):
        form = proveedor(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos.get("nombre")
            monto = datos.get("monto")
            tipo_pago = datos.get("tipo_pago")
            cuenta = datos.get("cuenta")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Proveedor(nombre, monto, tipo_pago, id_empresa, id_cuenta) VALUES('" + nombre + "', '" + str(monto) + "', '" + tipo_pago + "', '" + str(usuario.id_empresa.id_empresa) + "', '" + str(cuenta.id_cuenta) + "');"
            c.execute(consulta)
            db.commit()
            c.close()

            mensaje = "SE LOGRO AGREGAR EL PROVEEDOR"

            form = proveedor()
            form.fields['cuenta'].queryset = Cuenta.objects.all().exclude(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().exclude(id_usuario=id_usuario).filter(estado='ACTIVA')
            mensaje_error = "ERROR NO SE PUDO HACER LA CONSULTA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form,
                "mensaje": mensaje
            }
    return render(request, 'cliente/formulario/index.html', variables)