============================
Panel de Administración
============================

El panel de administración está diseñado para **bibliotecarios** y permite gestionar todo el ecosistema de Aeternum: libros, usuarios, préstamos y más.

.. note::
   
   Solo los usuarios con rol **"bibliotecario"** tienen acceso a estas funcionalidades.

----

🎯 Funcionalidades Principales
================================

Gestión de Usuarios
--------------------

**Endpoint:** ``GET /admin/users``

Lista todos los usuarios registrados en el sistema con sus datos básicos y estado de cuenta.

**¿Qué hace?**

1. Muestra todos los usuarios (activos e inactivos)
2. Permite buscar y filtrar usuarios
3. Ver detalles completos de cada usuario
4. Activar/desactivar cuentas

.. image:: _static/admin_users.png
   :alt: Panel de gestión de usuarios
   :align: center
   :width: 600px

**Información mostrada:**

- Nombre completo
- Correo electrónico
- Tipo y número de identificación
- Estado de la cuenta (activa/inactiva)
- Fecha de registro
- Rol asignado

----

Reactivar Cuenta de Usuario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Endpoint:** ``GET /users/reactivar/{user_id}``

Permite reactivar cuentas de usuarios que fueron eliminadas (soft delete).

**¿Qué hace?**

1. Busca el usuario por ID
2. Verifica que la cuenta esté inactiva
3. Reactiva la cuenta restaurando el acceso
4. Notifica al usuario por correo (opcional)

**Parámetros:**

- ``user_id``: ID del usuario a reactivar

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Cuenta reactivada exitosamente",
     "user_id": 42
   }

.. image:: _static/reactivar_cuenta.png
   :alt: Reactivación de cuenta
   :align: center
   :width: 500px

**Posibles errores:**

- Usuario no encontrado: "Usuario no existe"
- Cuenta ya activa: "La cuenta ya está activa"

----

Gestión de Libros
------------------

**Endpoint:** ``GET /admin/books``

Panel completo para administrar el catálogo de libros.

**¿Qué puedes hacer?**

- Ver todos los libros del catálogo
- Agregar nuevos libros al sistema
- Editar información de libros existentes
- Eliminar libros
- Gestionar disponibilidad (físicos y digitales)
- Habilitar/deshabilitar descargas

.. image:: _static/admin_books.png
   :alt: Gestión de libros
   :align: center
   :width: 600px

Agregar Nuevo Libro
^^^^^^^^^^^^^^^^^^^^

**Endpoint:** ``POST /admin/books/add``

Agrega un nuevo libro al catálogo.

**Datos requeridos:**

.. code-block:: json

   {
     "titulo": "El Principito",
     "autor": "Antoine de Saint-Exupéry",
     "isbn": "978-0-123456-78-9",
     "editorial": "Editorial Ejemplo",
     "año_publicacion": 1943,
     "genero": "Ficción",
     "copias_fisicas_disponibles": 5,
     "copias_digitales_disponibles": -1,
     "permitir_descarga": true,
     "url_portada": "https://...",
     "url_digital": "https://...",
     "descripcion": "Una historia sobre..."
   }

.. note::
   
   - ``copias_digitales_disponibles: -1`` significa **ilimitadas**
   - ``permitir_descarga: true`` habilita la descarga del PDF

Editar Libro
^^^^^^^^^^^^

**Endpoint:** ``PUT /admin/books/{book_id}``

Actualiza la información de un libro existente.

.. image:: _static/admin_edit_book.png
   :alt: Editar libro
   :align: center
   :width: 500px

Eliminar Libro
^^^^^^^^^^^^^^

**Endpoint:** ``DELETE /admin/books/{book_id}``

Elimina un libro del catálogo (soft delete).

.. warning::
   
   Si el libro tiene préstamos activos, no se puede eliminar hasta que sean devueltos.

----

Gestión de Préstamos Físicos
------------------------------

**Endpoint:** ``GET /admin/prestamos-fisicos``

Vista completa de todos los préstamos físicos del sistema.

**Estados de préstamos:**

- 🟡 **Pendiente**: Solicitado pero no recogido
- 🟢 **Activo**: Libro entregado al usuario
- 🔴 **Retrasado**: Pasó la fecha de devolución
- ⚪ **Devuelto**: Préstamo completado
- ❌ **Cancelado**: Préstamo cancelado

.. image:: _static/admin_prestamos.png
   :alt: Gestión de préstamos
   :align: center
   :width: 600px

Cambiar Estado de Préstamo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Endpoint:** ``PUT /prestamos-fisicos/estado/{prestamo_id}``

Actualiza el estado de un préstamo físico.

**Flujo típico:**

1. Usuario solicita libro → **Pendiente**
2. Usuario recoge libro → **Activo** (bibliotecario cambia estado)
3. Usuario devuelve libro → **Devuelto** (bibliotecario cambia estado)

**Datos a enviar:**

.. code-block:: json

   {
     "nuevo_estado": "activo"
   }

**Estados válidos:**

- ``pendiente``
- ``activo``
- ``devuelto``
- ``cancelado``

.. image:: _static/cambiar_estado_prestamo.png
   :alt: Cambiar estado de préstamo
   :align: center
   :width: 500px

----

📊 Reportes y Estadísticas
============================

Dashboard General
------------------

**Endpoint:** ``GET /admin/dashboard``

Vista general con métricas clave del sistema.

**Métricas mostradas:**

- Total de usuarios registrados
- Total de libros en catálogo
- Préstamos activos (físicos y digitales)
- Préstamos retrasados
- Libros más populares
- Usuarios más activos

.. image:: _static/admin_dashboard.png
   :alt: Dashboard administrativo
   :align: center
   :width: 600px

Reporte de Préstamos
---------------------

**Endpoint:** ``GET /admin/reportes/prestamos``

Genera reportes detallados de préstamos filtrados por:

- Fecha (rango)
- Tipo (físico/digital)
- Estado
- Usuario específico
- Libro específico

**Parámetros de filtro:**

.. code-block:: text

   /admin/reportes/prestamos?fecha_inicio=2025-01-01&fecha_fin=2025-01-31&tipo=fisico

.. image:: _static/admin_reportes.png
   :alt: Reportes de préstamos
   :align: center
   :width: 600px

----

 Configuración del Sistema
==============================

**Endpoint:** ``GET /admin/configuracion``

Ajustes generales del sistema:

- **Días de préstamo**: Duración predeterminada (default: 12 días)
- **Límite de préstamos simultáneos**: Máximo por usuario (default: 3)
- **Penalización por retraso**: Tiempo de bloqueo por atraso
- **Notificaciones**: Activar/desactivar recordatorios por correo
- **Mantenimiento**: Poner el sitio en modo mantenimiento

----

🔒 Notas de Seguridad
======================

.. warning::
   
   **Permisos de Administrador:**
   
   - Solo usuarios con rol ``bibliotecario`` pueden acceder
   - Todas las acciones administrativas quedan registradas (logs)
   - Los tokens de administrador tienen menor tiempo de expiración
   - Se requiere re-autenticación para acciones críticas (eliminar libros, usuarios)

.. tip::
   
   **Buenas prácticas:**
   
   - Revisa los logs de actividad regularmente
   - No compartas credenciales de administrador
   - Realiza backups periódicos de la base de datos
   - Verifica préstamos retrasados semanalmente