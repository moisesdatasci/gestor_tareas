# 📋 Gestor de Tareas - Django

Aplicación web para gestión de tareas personales desarrollada con Django. Permite a los usuarios registrarse, autenticarse y administrar sus tareas de forma privada y segura.

## 🚀 Funcionalidades Principales

### Autenticación de Usuarios
- **Registro de nuevos usuarios**: Sistema completo de creación de cuentas
- **Inicio de sesión**: Autenticación segura con credenciales
- **Cierre de sesión**: Finalización segura de sesión
- **Protección de rutas**: Solo usuarios autenticados pueden acceder a las tareas

### Gestión de Tareas
- **Ver lista de tareas**: Visualización de todas las tareas del usuario en tarjetas responsivas
- **Agregar tareas**: Creación de nuevas tareas con título y descripción
- **Ver detalles**: Vista completa de información de cada tarea
- **Eliminar tareas**: Eliminación con confirmación de seguridad
- **Privacidad**: Cada usuario solo ve y gestiona sus propias tareas

### Características Técnicas
- **Almacenamiento en memoria**: Las tareas se guardan en memoria durante la ejecución
- **Interfaz responsiva**: Diseño adaptable con Bootstrap 5
- **Formularios Django**: Validación y manejo seguro de datos
- **Decoradores de seguridad**: Protección de vistas con `@login_required`

## 📁 Estructura del Proyecto

```
gestor_tareas/
│
├── gestor_tareas/          # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py         # Configuración general
│   ├── urls.py            # URLs principales
│   └── wsgi.py
│
├── tareas/                # Aplicación de gestión de tareas
│   ├── migrations/        # Migraciones de base de datos
│   ├── templates/         # Plantillas HTML
│   │   └── tareas/
│   │       ├── base.html           # Plantilla base
│   │       ├── lista_tareas.html   # Lista de tareas
│   │       ├── detalle_tarea.html  # Detalle de tarea
│   │       ├── agregar_tarea.html  # Formulario nueva tarea
│   │       ├── login.html          # Inicio de sesión
│   │       └── registro.html       # Registro de usuario
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py           # Formularios Django
│   ├── models.py
│   ├── urls.py            # URLs de la aplicación
│   ├── views.py           # Lógica de vistas
│   └── tests.py
│
├── manage.py              # Utilidad de Django
└── db.sqlite3            # Base de datos SQLite
```

## 🛠️ Tecnologías Utilizadas

- **Django 4.x**: Framework web de Python
- **Python 3.8+**: Lenguaje de programación
- **Bootstrap 5**: Framework CSS para diseño responsivo
- **SQLite**: Base de datos para autenticación
- **HTML/CSS**: Estructura y estilos

## ⚙️ Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior instalado
- pip (gestor de paquetes de Python)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/moisesdatasci/gestor-tareas.git
cd gestor-tareas
```

### Paso 2: Crear y Activar Entorno Virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
pip install django
```

O si tienes un archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Paso 4: Realizar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto creará la base de datos SQLite y las tablas necesarias para el sistema de autenticación.

### Paso 5: Crear Superusuario (Opcional)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### Paso 6: Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 📖 Uso de la Aplicación

### Primera Vez

1. **Accede a la aplicación**: Abre tu navegador en `http://127.0.0.1:8000/`
2. **Regístrate**: Haz clic en "Registrarse" y crea tu cuenta
3. **Inicia sesión**: Usa tus credenciales para acceder
4. **Crea tareas**: Haz clic en "Nueva Tarea" o "Agregar Tarea"
5. **Gestiona tus tareas**: Ve detalles, elimina o crea nuevas tareas

### Navegación

- **Navbar**: Acceso rápido a todas las secciones
- **Mis Tareas**: Vista principal con todas tus tareas
- **Agregar Tarea**: Formulario para crear nuevas tareas
- **Ver Detalle**: Información completa de cada tarea
- **Eliminar**: Botón con confirmación de seguridad

## 🔒 Seguridad Implementada

- ✅ Autenticación obligatoria para acceder a tareas
- ✅ Cada usuario solo ve sus propias tareas
- ✅ Protección CSRF en formularios
- ✅ Validación de formularios con Django Forms
- ✅ Confirmación antes de eliminar tareas
- ✅ Mensajes de error y éxito para feedback

## 📝 Notas Importantes

- **Almacenamiento en Memoria**: Las tareas se almacenan en una variable de Python durante la ejecución del servidor. Si reinicias el servidor, las tareas se perderán. Esto es intencional para este proyecto educativo.
- **Base de Datos**: Solo se usa SQLite para gestionar usuarios y sesiones, no para las tareas.
- **Modo Desarrollo**: `DEBUG = True` está activado. Para producción, cambia a `False` y configura `ALLOWED_HOSTS`.

## 🚀 Configuración para Producción

Para desplegar en producción, modifica `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']
SECRET_KEY = 'tu-clave-secreta-segura'  # Usa variables de entorno
```

También considera:
- Usar una base de datos PostgreSQL o MySQL
- Configurar archivos estáticos con `collectstatic`
- Implementar HTTPS
- Usar un servidor WSGI como Gunicorn

## 🧪 Pruebas

Para verificar que todo funciona correctamente:

1. Registra al menos 2 usuarios diferentes
2. Crea tareas con cada usuario
3. Verifica que cada usuario solo ve sus propias tareas
4. Prueba agregar, ver detalle y eliminar tareas
5. Cierra sesión y verifica que no puedes acceder sin autenticarte

## 👨‍💻 Autor

Desarrollado por Moisés como proyecto educativo para aprender Django y desarrollo web.
