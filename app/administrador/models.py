# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cheque(models.Model):
    id_cheque = models.AutoField(primary_key=True)
    monto = models.FloatField()
    autorizado = models.CharField(max_length=20)
    disponible = models.CharField(max_length=20)
    id_chequera = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='id_chequera')
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return u'{0}'.format(f'-CORRELATIVO: { str(self.id_cheque) } -MONTO: { str(self.monto) } -AUTORIZADO: { self.autorizado } -DISPONIBLE: { self.disponible }')

    def __unicode__(self):
        return u'{0}'.format(f'-CORRELATIVO: { str(self.id_cheque) } -MONTO: { str(self.monto) } -AUTORIZADO: { self.autorizado } -DISPONIBLE: { self.disponible }')

    class Meta:
        managed = False
        db_table = 'cheque'


class Chequera(models.Model):
    id_chequera = models.AutoField(primary_key=True)
    acabada = models.CharField(max_length=20)
    id_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='id_cuenta')

    def __str__(self):
        return u'{0}'.format('CODIGO DE CHEQUERA: ' + str(self.id_cuenta) + ' ESTADO: ' + self.acabada)

    def __unicode__(self):
        return u'{0}'.format('CODIGO DE CHEQUERA: ' + str(self.id_cuenta) + ' ESTADO: ' + self.acabada)

    class Meta:
        managed = False
        db_table = 'chequera'


class Cliente(models.Model):
    cui = models.BigIntegerField(primary_key=True)
    nit = models.BigIntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    monto = models.FloatField()
    tipo_cuenta = models.CharField(max_length=50)
    tipo_moneda = models.CharField(max_length=50)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    estado = models.CharField(max_length=20)

    def __str__(self):
        return u'{0}'.format(self.id_cuenta)

    def __unicode__(self):
        return u'{0}'.format(self.id_cuenta)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Detalletarjeta(models.Model):
    id_detalletarjeta = models.AutoField(db_column='id_detalleTarjeta', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=200)
    monto = models.FloatField()
    tipo_moneda = models.CharField(max_length=50)
    id_tarjeta = models.ForeignKey('Tarjeta', models.DO_NOTHING, db_column='id_tarjeta')

    class Meta:
        managed = False
        db_table = 'detalletarjeta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    nombre_representante = models.CharField(max_length=150)
    tipo_empresa = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'empresa'


class Pagoplanilla(models.Model):
    id_pagoplanilla = models.AutoField(db_column='id_pagoPlanilla', primary_key=True)  # Field name made lowercase.
    monto = models.FloatField()
    monto_anterior = models.FloatField()
    monto_despues = models.FloatField()
    fecha = models.DateTimeField(blank=True, null=True)
    id_planilla = models.ForeignKey('Planilla', models.DO_NOTHING, db_column='id_planilla')
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'pagoplanilla'


class Pagoprestamo(models.Model):
    id_pagoprestamo = models.AutoField(db_column='id_pagoPrestamo', primary_key=True)  # Field name made lowercase.
    monto = models.FloatField()
    interes = models.FloatField()
    fecha = models.DateTimeField(blank=True, null=True)
    tipo_pago = models.CharField(max_length=30)
    id_prestamo = models.ForeignKey('Prestamo', models.DO_NOTHING, db_column='id_prestamo')
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'pagoprestamo'


class Pagoproveedor(models.Model):
    id_pagoproveedor = models.AutoField(db_column='id_pagoProveedor', primary_key=True)  # Field name made lowercase.
    monto = models.FloatField()
    monto_anterior = models.FloatField()
    monto_despues = models.FloatField()
    fecha = models.DateTimeField(blank=True, null=True)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'pagoproveedor'


class Planilla(models.Model):
    id_planilla = models.AutoField(primary_key=True)
    monto = models.FloatField()
    nombre_empleado = models.CharField(max_length=100)
    tipo_pago = models.CharField(max_length=30)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'planilla'


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    monto = models.FloatField()
    descripcion = models.CharField(max_length=200)
    tipo_prestamo = models.CharField(max_length=30)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    aprobado = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return u'{0}'.format('CODIGO DE PRESTAMO: ' + str(self.id_prestamo))

    def __unicode__(self):
        return u'{0}'.format('CODIGO DE PRESTAMO: ' + str(self.id_prestamo))

    class Meta:
        managed = False
        db_table = 'prestamo'


class Prestamoautomatico(models.Model):
    id_prestamoauto = models.AutoField(db_column='id_prestamoAuto', primary_key=True)  # Field name made lowercase.
    monto = models.FloatField()
    id_prestamo = models.ForeignKey(Prestamo, models.DO_NOTHING, db_column='id_prestamo')
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'prestamoautomatico'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    monto = models.FloatField()
    tipo_pago = models.CharField(max_length=30)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'proveedor'


class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    monto = models.FloatField()
    marca = models.CharField(max_length=30)
    puntos = models.IntegerField(blank=True, null=True)
    cashback = models.IntegerField(blank=True, null=True)
    limitecredito = models.FloatField(db_column='limiteCredito')  # Field name made lowercase.
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'tarjeta'


class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    monto = models.FloatField()
    monto_anterior = models.FloatField()
    monto_despues = models.FloatField()
    tipo_moneda = models.CharField(max_length=50)
    tipo_transaccion = models.CharField(max_length=50)
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaccion'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=25)
    intentos = models.IntegerField()
    cui = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cui', blank=True, null=True)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)

    def __str__(self):
        return u'{0}'.format(self.nombre)

    def __unicode__(self):
        return u'{0}'.format(self.nombre)

    class Meta:
        managed = False
        db_table = 'usuario'




