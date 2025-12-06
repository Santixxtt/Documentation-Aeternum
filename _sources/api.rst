============================
Documentación API
============================

Referencia completa de todos los endpoints de la API de Aeternum.

.. note::
   
   **Base URL:** ``https://api.aeternum.com``  
   **Versión actual:** ``v1``  
   **Formato:** JSON  
   **Autenticación:** JWT Bearer Token

----

 Autenticación
=================

POST /auth/register
--------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/auth/register</code>
     </div>
     <p>Registra un nuevo usuario en el sistema.</p>
   </div>

**Request Body:**

.. code-block:: json

   {
     "nombre": "Juan",
     "apellido": "Pérez",
     "tipo_identificacion": "CC",
     "num_identificacion": "1234567890",
     "correo": "juan@ejemplo.com",
     "clave": "MiContraseña123!",
     "rol": "usuario",
     "consent": true
   }

**Response 201:**

.. code-block:: json

   {
     "message": "¡Cuenta creada con éxito!",
     "user_id": 42
   }

----

POST /auth/login
-----------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/auth/login</code>
     </div>
     <p>Inicia sesión y obtiene un token JWT.</p>
   </div>

**Request Body:**

.. code-block:: json

   {
     "correo": "juan@ejemplo.com",
     "clave": "MiContraseña123!"
   }

**Response 200:**

.. code-block:: json

   {
     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "token_type": "bearer",
     "rol": "usuario"
   }

----

POST /auth/recuperar-contrasena
---------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/auth/recuperar-contrasena</code>
     </div>
     <p>Envía un correo con enlace de recuperación de contraseña.</p>
   </div>

**Request Body:**

.. code-block:: json

   {
     "correo": "juan@ejemplo.com"
   }

**Response 200:**

.. code-block:: json

   {
     "message": "Si el correo existe, recibirás un enlace de recuperación"
   }

----

POST /auth/restablecer-contrasena
-----------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/auth/restablecer-contrasena</code>
     </div>
     <p>Restablece la contraseña usando el token recibido por correo.</p>
   </div>

**Request Body:**

.. code-block:: json

   {
     "token": "abc123xyz...",
     "nueva_clave": "NuevaContraseña456!"
   }

**Response 200:**

.. code-block:: json

   {
     "message": "Contraseña actualizada correctamente"
   }

----

👤 Usuarios
============

GET /user/me
-------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/user/me</code>
     </div>
     <p>Obtiene el perfil del usuario autenticado.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "id": 42,
     "nombre": "Juan",
     "apellido": "Pérez",
     "correo": "juan@ejemplo.com",
     "tipo_identificacion": "CC",
     "num_identificacion": "1234567890",
     "rol": "usuario",
     "fecha_registro": "2025-01-15T10:30:00",
     "activo": true
   }

----

PUT /users/me
--------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-put">PUT</span>
       <code>/users/me</code>
     </div>
     <p>Actualiza información del perfil del usuario.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "nombre": "Juan Carlos",
     "apellido": "Pérez García",
     "correo": "nuevo_correo@ejemplo.com"
   }

**Response 200:**

.. code-block:: json

   {
     "message": "Perfil actualizado exitosamente",
     "user": {
       "id": 42,
       "nombre": "Juan Carlos",
       "apellido": "Pérez García",
       "correo": "nuevo_correo@ejemplo.com"
     }
   }

----

DELETE /users/me
-----------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-delete">DELETE</span>
       <code>/users/me</code>
     </div>
     <p>Elimina la cuenta del usuario (soft delete).</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "message": "Cuenta eliminada exitosamente"
   }

----

GET /users/reactivar/{user_id}
--------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/users/reactivar/{user_id}</code>
     </div>
     <p>Reactiva una cuenta eliminada. <strong>Solo bibliotecarios.</strong></p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "message": "Cuenta reactivada exitosamente",
     "user_id": 42
   }

----

 Lista de Deseos
===================

GET /wishlist/list
-------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/wishlist/list</code>
     </div>
     <p>Obtiene la lista de deseos del usuario.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "total": 5,
     "wishlist": [
       {
         "id": 1,
         "openlibrary_key": "/works/OL45883W",
         "book_title": "El Principito",
         "book_author": "Antoine de Saint-Exupéry",
         "added_at": "2025-01-15T14:30:00",
         "disponible": true
       }
     ]
   }

----

POST /wishlist/add
-------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/wishlist/add</code>
     </div>
     <p>Agrega un libro a la lista de deseos.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "book_title": "El Principito",
     "book_author": "Antoine de Saint-Exupéry"
   }

**Response 201:**

.. code-block:: json

   {
     "message": "Libro agregado a tu lista de deseos",
     "wishlist_id": 123
   }

----

DELETE /wishlist/delete/{book_id}
----------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-delete">DELETE</span>
       <code>/wishlist/delete/{book_id}</code>
     </div>
     <p>Elimina un libro de la lista de deseos.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "message": "Libro eliminado de tu lista de deseos"
   }

----

GET /wishlist/buscar-libro/{openlibrary_key}
----------------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/wishlist/buscar-libro/{openlibrary_key}</code>
     </div>
     <p>Busca información de un libro por su clave de Open Library.</p>
   </div>

**Response 200:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "title": "El Principito",
     "author": "Antoine de Saint-Exupéry",
     "cover_url": "https://covers.openlibrary.org/...",
     "description": "...",
     "disponible_fisico": true,
     "disponible_digital": true
   }

----

 Reviews y Calificaciones
============================

POST /reviews/rate
-------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/reviews/rate</code>
     </div>
     <p>Califica un libro (1-5 estrellas).</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "rating": 5
   }

**Response 201:**

.. code-block:: json

   {
     "message": "Calificación guardada exitosamente",
     "rating": 5,
     "average_rating": 4.5,
     "total_ratings": 127
   }

----

GET /reviews/ratings/{openlibrary_key}
---------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/reviews/ratings/{openlibrary_key}</code>
     </div>
     <p>Obtiene estadísticas de calificaciones de un libro.</p>
   </div>

**Response 200:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "average_rating": 4.5,
     "total_ratings": 127,
     "ratings_breakdown": {
       "5": 85,
       "4": 30,
       "3": 8,
       "2": 3,
       "1": 1
     }
   }

----

POST /reviews/comment
----------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/reviews/comment</code>
     </div>
     <p>Publica un comentario sobre un libro.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "comment": "Excelente libro, totalmente recomendado para amantes de la filosofía."
   }

**Response 201:**

.. code-block:: json

   {
     "message": "Comentario publicado exitosamente",
     "comment_id": 456,
     "created_at": "2025-01-15T14:20:00"
   }

----

GET /reviews/comments/{openlibrary_key}
-----------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/reviews/comments/{openlibrary_key}</code>
     </div>
     <p>Obtiene todos los comentarios de un libro.</p>
   </div>

**Query Parameters:**

- ``page`` (int, optional): Número de página (default: 1)
- ``limit`` (int, optional): Comentarios por página (default: 10, max: 50)

**Response 200:**

.. code-block:: json

   {
     "total_comments": 45,
     "page": 1,
     "total_pages": 5,
     "comments": [
       {
         "comment_id": 789,
         "user_name": "Juan Pérez",
         "comment": "Excelente libro, muy recomendado.",
         "created_at": "2025-01-15T14:20:00",
         "updated_at": null,
         "is_owner": false
       }
     ]
   }

----

PUT /reviews/comments/{comment_id}
-----------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-put">PUT</span>
       <code>/reviews/comments/{comment_id}</code>
     </div>
     <p>Actualiza un comentario existente.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "comment": "Actualicé mi opinión: es aún mejor de lo que pensaba."
   }

**Response 200:**

.. code-block:: json

   {
     "message": "Comentario actualizado exitosamente",
     "comment_id": 788,
     "updated_at": "2025-01-16T11:45:00"
   }

----

DELETE /reviews/comments/{comment_id}
--------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-delete">DELETE</span>
       <code>/reviews/comments/{comment_id}</code>
     </div>
     <p>Elimina un comentario.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "message": "Comentario eliminado exitosamente",
     "comment_id": 788
   }

----

GET /reviews/user-rating/{openlibrary_key}
--------------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/reviews/user-rating/{openlibrary_key}</code>
     </div>
     <p>Obtiene la calificación del usuario para un libro específico.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "user_rating": 4,
     "rated_at": "2025-01-15T10:30:00"
   }

----

 Préstamos Digitales
========================

POST /prestamos/digital
------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/prestamos/digital</code>
     </div>
     <p>Registra un nuevo préstamo digital.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "book_title": "El Principito",
     "book_author": "Antoine de Saint-Exupéry"
   }

**Response 201:**

.. code-block:: json

   {
     "message": "Préstamo digital registrado exitosamente",
     "prestamo_id": 123,
     "url_lectura": "https://aeternum.com/leer/OL45883W",
     "fecha_inicio": "2025-01-15T14:30:00",
     "fecha_expiracion": "2025-01-27T14:30:00"
   }

----

📦 Préstamos Físicos
=====================

POST /prestamos-fisicos/solicitar
-----------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/prestamos-fisicos/solicitar</code>
     </div>
     <p>Solicita un préstamo físico de un libro.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "book_title": "El Principito",
     "book_author": "Antoine de Saint-Exupéry",
     "fecha_recogida": "2025-01-20"
   }

**Response 201:**

.. code-block:: json

   {
     "message": "Solicitud de préstamo creada exitosamente",
     "prestamo_id": 456,
     "estado": "pendiente",
     "fecha_recogida": "2025-01-20",
     "fecha_devolucion": "2025-02-01"
   }

----

GET /prestamos-fisicos/mis-prestamos
--------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-get">GET</span>
       <code>/prestamos-fisicos/mis-prestamos</code>
     </div>
     <p>Lista todos los préstamos físicos del usuario.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Query Parameters:**

- ``estado`` (string, optional): Filtrar por estado (pendiente, activo, devuelto, cancelado)
- ``page`` (int, optional): Número de página
- ``limit`` (int, optional): Resultados por página

**Response 200:**

.. code-block:: json

   {
     "total_prestamos": 8,
     "prestamos_activos": 2,
     "prestamos": [
       {
         "prestamo_id": 456,
         "book_title": "El Principito",
         "book_author": "Antoine de Saint-Exupéry",
         "fecha_solicitud": "2025-01-15T14:30:00",
         "fecha_recogida": "2025-01-20",
         "fecha_devolucion": "2025-02-01",
         "estado": "pendiente",
         "dias_restantes": 5
       }
     ]
   }

----

PUT /prestamos-fisicos/cancelar/{prestamo_id}
-----------------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-put">PUT</span>
       <code>/prestamos-fisicos/cancelar/{prestamo_id}</code>
     </div>
     <p>Cancela un préstamo físico pendiente.</p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Response 200:**

.. code-block:: json

   {
     "message": "Préstamo cancelado exitosamente",
     "prestamo_id": 456
   }

----

PUT /prestamos-fisicos/estado/{prestamo_id}
---------------------------------------------

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-put">PUT</span>
       <code>/prestamos-fisicos/estado/{prestamo_id}</code>
     </div>
     <p>Actualiza el estado de un préstamo. <strong>Solo bibliotecarios.</strong></p>
   </div>

**Headers:**

.. code-block:: text

   Authorization: Bearer {token}

**Request Body:**

.. code-block:: json

   {
     "nuevo_estado": "activo"
   }

**Valores válidos:** ``pendiente``, ``activo``, ``devuelto``, ``cancelado``

**Response 200:**

.. code-block:: json

   {
     "message": "Estado actualizado exitosamente",
     "prestamo_id": 456,
     "nuevo_estado": "activo"
   }

----

🔒 Códigos de Estado HTTP
===========================

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Código
     - Descripción
   * - **200**
     - ✅ Solicitud exitosa
   * - **201**
     - ✅ Recurso creado exitosamente
   * - **400**
     - ❌ Error en la solicitud (datos inválidos)
   * - **401**
     -  No autenticado (token faltante o inválido)
   * - **403**
     - 🚫 Prohibido (sin permisos suficientes)
   * - **404**
     - 🔍 Recurso no encontrado
   * - **409**
     - ⚠️ Conflicto (recurso ya existe)
   * - **422**
     - 📝 Error de validación
   * - **500**
     - 💥 Error interno del servidor

----

🔑 Autenticación en Requests
==============================

Todas las rutas protegidas requieren el header ``Authorization``:

**Formato:**

.. code-block:: text

   Authorization: Bearer {tu_token_jwt}

**Ejemplo en cURL:**

.. code-block:: bash

   curl -X GET "https://api.aeternum.com/user/me" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

**Ejemplo en JavaScript (Axios):**

.. code-block:: javascript

   const response = await axios.get('https://api.aeternum.com/user/me', {
     headers: {
       'Authorization': `Bearer ${token}`
     }
   });

**Ejemplo en Python (requests):**

.. code-block:: python

   import requests

   headers = {
       'Authorization': f'Bearer {token}'
   }
   response = requests.get('https://api.aeternum.com/user/me', headers=headers)

----

📚 Documentación Interactiva
==============================

Aeternum incluye documentación interactiva de la API usando **Swagger UI**:

- **Swagger UI:** `https://api.aeternum.com/docs <https://api.aeternum.com/docs>`_
- **ReDoc:** `https://api.aeternum.com/redoc <https://api.aeternum.com/redoc>`_

Desde ahí puedes:

- Ver todos los endpoints disponibles
- Probar requests directamente
- Ver ejemplos de request/response
- Descargar el schema OpenAPI

----

⚡ Rate Limiting
=================

La API implementa rate limiting para prevenir abuso:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Endpoint
     - Límite
   * - ``/auth/login``
     - 5 requests / minuto
   * - ``/auth/register``
     - 3 requests / hora
   * - Endpoints generales
     - 100 requests / minuto
   * - Endpoints de búsqueda
     - 30 requests / minuto

**Headers de respuesta:**

.. code-block:: text

   X-RateLimit-Limit: 100
   X-RateLimit-Remaining: 95
   X-RateLimit-Reset: 1642089600

Si excedes el límite, recibirás **HTTP 429 Too Many Requests**.