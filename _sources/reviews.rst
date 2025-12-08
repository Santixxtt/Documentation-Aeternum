=====================================
Sistema de Reviews y Calificaciones
=====================================

El sistema de reviews permite a los usuarios calificar y comentar libros, ayudando a la comunidad a descubrir grandes lecturas.

.. note::
   
   Solo usuarios autenticados pueden dejar calificaciones y comentarios.

----

 Calificaciones
===================

Subir Calificación
-------------------

**Endpoint:** ``POST /reviews/rate``

Permite a un usuario calificar un libro con una puntuación de 1 a 5 estrellas.

**¿Qué hace?**

1. Verifica que el usuario esté autenticado
2. Valida que la calificación esté entre 1 y 5
3. Guarda o actualiza la calificación del usuario
4. Recalcula el promedio general del libro

**Datos a enviar:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "rating": 5
   }

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Calificación guardada exitosamente",
     "rating": 5,
     "average_rating": 4.5,
     "total_ratings": 127
   }

.. image:: _static/rate_book.png
   :alt: Calificar libro
   :align: center
   :width: 500px

**Validaciones:**

- ``rating`` debe ser un número entre 1 y 5
- Solo una calificación por usuario por libro
- Si el usuario ya calificó, se actualiza su calificación anterior

**Posibles errores:**

- Calificación inválida: "La calificación debe estar entre 1 y 5"
- Usuario no autenticado: "Debes iniciar sesión para calificar"

----

Obtener Calificaciones de un Libro
------------------------------------

**Endpoint:** ``GET /reviews/ratings/{openlibrary_key}``

Obtiene estadísticas de calificaciones de un libro específico.

**Respuesta:**

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

**Información devuelta:**

- Promedio de calificaciones
- Total de usuarios que calificaron
- Distribución por estrellas (1-5)

.. image:: _static/ratings_stats.png
   :alt: Estadísticas de calificaciones
   :align: center
   :width: 500px

----

Obtener Calificación del Usuario
----------------------------------

**Endpoint:** ``GET /reviews/user-rating/{openlibrary_key}``

Obtiene la calificación que el usuario actual ha dado a un libro específico.

**Uso típico:**

Se usa para mostrar al usuario su calificación previa cuando ve el detalle de un libro.

**Respuesta si el usuario ya calificó:**

.. code-block:: json

   {
     "user_rating": 4,
     "rated_at": "2025-01-15T10:30:00"
   }

**Respuesta si no ha calificado:**

.. code-block:: json

   {
     "user_rating": null
   }

----

 Comentarios
================

Subir Comentario
-----------------

**Endpoint:** ``POST /reviews/comment``

Permite a un usuario dejar un comentario sobre un libro.

**Datos a enviar:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "comment": "Una lectura increíble que me hizo reflexionar sobre la vida. Totalmente recomendado para amantes de la filosofía."
   }

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Comentario publicado exitosamente",
     "comment_id": 456,
     "created_at": "2025-01-15T14:20:00"
   }

.. image:: _static/post_comment.png
   :alt: Publicar comentario
   :align: center
   :width: 600px


**Posibles errores:**

- Comentario muy corto: "El comentario debe tener al menos 10 caracteres"
- Comentario muy largo: "El comentario no puede superar los 1000 caracteres"

----

Obtener Comentarios de un Libro
---------------------------------

**Endpoint:** ``GET /reviews/comments/{openlibrary_key}``

Obtiene todos los comentarios de un libro ordenados por fecha (más recientes primero).

**Parámetros opcionales:**

- ``page``: Número de página (default: 1)
- ``limit``: Comentarios por página (default: 10, max: 50)

**Ejemplo de URL:**

.. code-block:: text

   GET /reviews/comments/OL45883W?page=1&limit=10

**Respuesta:**

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
       },
       {
         "comment_id": 788,
         "user_name": "María García",
         "comment": "Me cambió la perspectiva sobre muchas cosas.",
         "created_at": "2025-01-14T09:15:00",
         "updated_at": "2025-01-14T10:30:00",
         "is_owner": true
       }
     ]
   }

.. image:: _static/view_comments.png
   :alt: Ver comentarios
   :align: center
   :width: 600px

**Campo ``is_owner``:**

Indica si el comentario pertenece al usuario actual (para mostrar opciones de editar/eliminar).

----

Actualizar Comentario
----------------------

**Endpoint:** ``PUT /reviews/comments/{comment_id}``

Permite editar un comentario existente (solo el autor puede editarlo).

**Datos a enviar:**

.. code-block:: json

   {
     "comment": "Actualicé mi opinión: es aún mejor de lo que pensaba inicialmente."
   }

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Comentario actualizado exitosamente",
     "comment_id": 788,
     "updated_at": "2025-01-16T11:45:00"
   }

.. image:: _static/edit_comment.png
   :alt: Editar comentario
   :align: center
   :width: 500px

**Restricciones:**

- Solo el autor del comentario puede editarlo

**Posibles errores:**

- No autorizado: "No tienes permiso para editar este comentario"

----

Eliminar Comentario
--------------------

**Endpoint:** ``DELETE /reviews/comments/{comment_id}``

Elimina un comentario (solo el autor o un administrador pueden hacerlo).

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Comentario eliminado exitosamente",
     "comment_id": 788
   }

.. image:: _static/edit_comment.png
   :alt: Eliminar comentario
   :align: center
   :width: 400px

**¿Quién puede eliminar?**

- El autor del comentario
- Usuarios con rol "bibliotecario" (proximamente)

**Posibles errores:**

- No autorizado: "No tienes permiso para eliminar este comentario"
- Comentario no encontrado: "El comentario no existe"

----

🎯 Mejores Prácticas
======================

Para Usuarios
--------------

.. tip::
   
   - **Sé constructivo**: Los comentarios ayudan a otros usuarios
   - **Evita spoilers**: Si los incluyes, avisa al inicio
   - **Sé respetuoso**: No ataques a otros usuarios o al autor
   - **Actualiza tu opinión**: Puedes editar si cambias de parecer

----

🔒 Notas de Seguridad
======================

- **Edición limitada**: Los comentarios no pueden editarse indefinidamente
- **Anonimato**: No se muestran correos ni datos sensibles en comentarios