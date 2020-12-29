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

    class Meta:
        managed = False
        db_table = 'cheque'


class Chequera(models.Model):
    id_chequera = models.AutoField(primary_key=True)
    acabada = models.CharField(max_length=20)
    id_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='id_cuenta')

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

    class Meta:
        managed = False
        db_table = 'cuenta'


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


class Planilla(models.Model):
    id_planilla = models.AutoField(primary_key=True)
    monto = models.FloatField()
    monto_anterior = models.FloatField()
    monto_despues = models.FloatField()
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'planilla'


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    monto = models.FloatField()
    monto_anterior = models.FloatField()
    monto_despues = models.FloatField()
    tipo_prestamo = models.CharField(max_length=50)
    id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='id_cuenta')

    class Meta:
        managed = False
        db_table = 'prestamo'


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

    class Meta:
        managed = False
        db_table = 'usuario'
