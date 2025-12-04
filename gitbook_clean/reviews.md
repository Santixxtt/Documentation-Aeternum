=====================================
# Sistema de Reviews y Calificaciones

El sistema de reviews permite a los usuarios calificar y comentar libros, ayudando a la comunidad a descubrir grandes lecturas.

.. note::
   
   Solo usuarios autenticados pueden dejar calificaciones y comentarios.

---

#  Calificaciones

## Subir Calificación

**Endpoint:** `POST /reviews/rate`

Permite a un usuario calificar un libro con una puntuación de 1 a 5 estrellas.

**¿Qué hace?**

1. Verifica que el usuario esté autenticado
2. Valida que la calificación esté entre 1 y 5
3. Guarda o actualiza la calificación del usuario
4. Recalcula el promedio general del libro

**Datos a enviar:**

```json
{
  "openlibrary_key": "/works/OL45883W",
  "rating": 5
}
```

**Respuesta exitosa:**

```json
{
  "message": "Calificación guardada exitosamente",
  "rating": 5,
  "average_rating": 4.5,
  "total_ratings": 127
}
```

![Imagen](.gitbook/assets/rate_book.png)

**Validaciones:**

- `rating` debe ser un número entre 1 y 5
- Solo una calificación por usuario por libro
- Si el usuario ya calificó, se actualiza su calificación anterior

**Posibles errores:**

- Calificación inválida: "La calificación debe estar entre 1 y 5"
- Usuario no autenticado: "Debes iniciar sesión para calificar"

---

## Obtener Calificaciones de un Libro

**Endpoint:** `GET /reviews/ratings/{openlibrary_key}`

Obtiene estadísticas de calificaciones de un libro específico.

**Respuesta:**

```json
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
```

**Información devuelta:**

- Promedio de calificaciones
- Total de usuarios que calificaron
- Distribución por estrellas (1-5)

![Imagen](.gitbook/assets/ratings_stats.png)

---

## Obtener Calificación del Usuario

**Endpoint:** `GET /reviews/user-rating/{openlibrary_key}`

Obtiene la calificación que el usuario actual ha dado a un libro específico.

**Uso típico:**

Se usa para mostrar al usuario su calificación previa cuando ve el detalle de un libro.

**Respuesta si el usuario ya calificó:**

```json
{
  "user_rating": 4,
  "rated_at": "2025-01-15T10:30:00"
}
```

**Respuesta si no ha calificado:**

```json
{
  "user_rating": null
}
```

---

#  Comentarios

## Subir Comentario

**Endpoint:** `POST /reviews/comment`

Permite a un usuario dejar un comentario sobre un libro.

**Datos a enviar:**

```json
{
  "openlibrary_key": "/works/OL45883W",
  "comment": "Una lectura increíble que me hizo reflexionar sobre la vida. Totalmente recomendado para amantes de la filosofía."
}
```

**Respuesta exitosa:**

```json
{
  "message": "Comentario publicado exitosamente",
  "comment_id": 456,
  "created_at": "2025-01-15T14:20:00"
}
```

![Imagen](.gitbook/assets/post_comment.png)

**Validaciones:**

- El comentario debe tener entre 10 y 1000 caracteres
- No se permiten comentarios duplicados (mismo usuario, mismo libro, mismo texto)
- Se filtran palabras ofensivas (moderación automática)

**Posibles errores:**

- Comentario muy corto: "El comentario debe tener al menos 10 caracteres"
- Comentario muy largo: "El comentario no puede superar los 1000 caracteres"
- Comentario duplicado: "Ya publicaste este comentario anteriormente"

---

## Obtener Comentarios de un Libro

**Endpoint:** `GET /reviews/comments/{openlibrary_key}`

Obtiene todos los comentarios de un libro ordenados por fecha (más recientes primero).

**Parámetros opcionales:**

- `page`: Número de página (default: 1)
- `limit`: Comentarios por página (default: 10, max: 50)

**Ejemplo de URL:**

```text
GET /reviews/comments/OL45883W?page=1&limit=10
```

**Respuesta:**

```json
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
```

![Imagen](.gitbook/assets/view_comments.png)

**Campo `is_owner`:**

Indica si el comentario pertenece al usuario actual (para mostrar opciones de editar/eliminar).

---

## Actualizar Comentario

**Endpoint:** `PUT /reviews/comments/{comment_id}`

Permite editar un comentario existente (solo el autor puede editarlo).

**Datos a enviar:**

```json
{
  "comment": "Actualicé mi opinión: es aún mejor de lo que pensaba inicialmente."
}
```

**Respuesta exitosa:**

```json
{
  "message": "Comentario actualizado exitosamente",
  "comment_id": 788,
  "updated_at": "2025-01-16T11:45:00"
}
```

![Imagen](.gitbook/assets/edit_comment.png)

**Restricciones:**

- Solo el autor del comentario puede editarlo
- No se puede editar después de 24 horas de publicado (opcional)
- Las mismas validaciones de longitud aplican

**Posibles errores:**

- No autorizado: "No tienes permiso para editar este comentario"
- Tiempo expirado: "No puedes editar comentarios después de 24 horas"

---

## Eliminar Comentario

**Endpoint:** `DELETE /reviews/comments/{comment_id}`

Elimina un comentario (solo el autor o un administrador pueden hacerlo).

**Respuesta exitosa:**

```json
{
  "message": "Comentario eliminado exitosamente",
  "comment_id": 788
}
```

![Imagen](.gitbook/assets/edit_comment.png)

**¿Quién puede eliminar?**

- El autor del comentario
- Usuarios con rol "bibliotecario" (moderación)

**Posibles errores:**

- No autorizado: "No tienes permiso para eliminar este comentario"
- Comentario no encontrado: "El comentario no existe"

---

#  Moderación (Solo Bibliotecarios)

Los bibliotecarios tienen funciones adicionales de moderación:

## Reportar Comentario Inapropiado

**Endpoint:** `POST /reviews/report/{comment_id}`

Los usuarios pueden reportar comentarios ofensivos o inapropiados.

**Datos a enviar:**

```json
{
  "reason": "Contenido ofensivo / spam / acoso / otro",
  "details": "Descripción del problema"
}
```

---

#  Mejores Prácticas

## Para Usuarios

.. tip::
   
   - **Sé constructivo**: Los comentarios ayudan a otros usuarios
   - **Evita spoilers**: Si los incluyes, avisa al inicio
   - **Sé respetuoso**: No ataques a otros usuarios o al autor
   - **Actualiza tu opinión**: Puedes editar si cambias de parecer

## Para Bibliotecarios

.. note::
   
   - Revisa comentarios reportados regularmente
   - Elimina contenido ofensivo o spam rápidamente
   - Contacta a usuarios que violen las reglas repetidamente
   - Fomenta una comunidad positiva y constructiva

---

#  Notas de Seguridad

- **Protección contra spam**: Límite de 5 comentarios por usuario por día
- **Filtro de contenido**: Palabras ofensivas se detectan automáticamente
- **Edición limitada**: Los comentarios no pueden editarse indefinidamente
- **Moderación**: Los bibliotecarios pueden eliminar cualquier comentario
- **Anonimato**: No se muestran correos ni datos sensibles en comentarios