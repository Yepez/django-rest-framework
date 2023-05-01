# django-rest-framework

## 1. Clonar el repositorio
Primero, clona el repositorio en tu máquina local mediante el siguiente comando en tu terminal:

```
git clone https://github.com/tu_usuario/tu_proyecto.git
```

Recuerda reemplazar tu_usuario y tu_proyecto con los nombres de usuario y de proyecto correspondientes.

## 2. Crear archivo .env
Crea un archivo .env en el directorio raíz del proyecto y agrega las siguientes variables de entorno, reemplazando los valores según corresponda:

```
SECRET_KEY=tu_clave_secreta
DEBUG=True
```

## 3. Iniciar contenedor de Docker
Asegúrate de tener instalado Docker en tu máquina local y ejecuta el siguiente comando en tu terminal desde el directorio raíz del proyecto para iniciar el contenedor de Docker:

```
docker-compose up -d
```

## 4. Realizar migraciones
Una vez iniciado el contenedor, ejecuta los siguientes comandos en tu terminal para realizar las migraciones de la base de datos:
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## 5. Acceder a la aplicación
Una vez completados los pasos anteriores, accede a la aplicación mediante tu navegador web en la siguiente dirección:

```
http://localhost:8000
```

## 6. Endpoints disponibles
El proyecto cuenta con los siguientes endpoints disponibles:

- **/api/usuario/**: endpoint para crear usuarios.
- **/api/usuario/todos**: endpoint para listar usuarios.
- **/api/usuario/edad**: endpoint para listar usuarios en orden de menor a mayor de acuerdo a su edad.
- **/api/usuario/apellido_paterno**: endpoint para listar usuarios en orden alfabético de acuerdo a su apellido paterno.
- **/api/usuario/<int:pk>/**: endpoint para actualizar usuarios.
- **/api/usuario/<int:pk>/delete/**: endpoint para eliminar usuarios.
- **/api/empleados/**: endpoint para crear y listar empleados.
- **/api/productos/**: endpoint para crear, listar y buscar productos.
- **/api/ventas/**: endpoint para crear, listar y buscar ventas.
- **/api/inventarios/**: endpoint para crear, listar y buscar inventario.
- Además, el endpoint **/api-auth/** permite el inicio de sesión y autenticación de usuarios.

## 7. Detener contenedor de Docker
Para detener el contenedor de Docker, ejecuta el siguiente comando en tu terminal desde el directorio raíz del proyecto:
```
docker-compose down
```
