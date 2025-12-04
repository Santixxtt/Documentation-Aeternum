============================
# Módulo de Usuario

Este módulo maneja toda la experiencia del usuario autenticado en Aeternum: desde el dashboard inicial hasta la gestión de su perfil y préstamos.

.. note::
   
   Todas las funcionalidades requieren que el usuario esté **autenticado** con un token JWT válido.

---

#  Dashboard / Inicio

**Endpoint:** `GET /user/me`

## ¿Qué muestra?

1. Saludo personalizado con el nombre del usuario
2. **Libros recomendados** basados en:
   
   - Historial de lectura
   - Lista de deseos
   - Libros populares
   - Géneros favoritos

3. Acceso rápido a:
   
   - Catálogo completo
   - Lista de deseos
   - Mis préstamos
   - Mi perfil

4. Estadísticas personales:
   
   - Libros leídos este mes
   - Racha de lectura
   - Próximos vencimientos

![Imagen](.gitbook/assets/dashboard_user.png)

**Respuesta del endpoint:**

```json
{
  "user": {
    "id": 42,
    "nombre": "Juan",
    "apellido": "Pérez",
    "correo": "juan@ejemplo.com"
  },
  "recommended_books": [
    {
      "openlibrary_key": "/works/OL45883W",
      "title": "El Principito",
      "author": "Antoine de Saint-Exupéry",
      "cover_url": "https://covers.openlibrary.org/...",
      "average_rating": 4.5
    }
  ],
  "stats": {
    "books_read_this_month": 3,
    "current_streak_days": 15,
    "upcoming_due_dates": 2
  }
}
```

---

#  Catálogo de Libros

**URL:** `/catalogo`

Exploración completa del catálogo de libros de Aeternum.

## Funcionalidades

1. **Búsqueda avanzada:**
   
   - Por título
   - Por autor
   - Por ISBN
   - Por palabras clave

2. **Filtros:**
   
   - Género/Categoría
   - Disponibilidad (físico/digital)
   - Calificación mínima
   - Año de publicación

3. **Ordenamiento:**
   
   - Más recientes
   - Mejor calificados
   - Más populares
   - A-Z / Z-A

![Imagen](.gitbook/assets/catalogo_logueado.png)

### Barra de Búsqueda

```text
[ Buscar por título, autor o ISBN...] [Filtros ] [Ordenar ]
```

Ejemplo de búsqueda:

```text
GET /api/books/search?q=principito&genero=ficcion&disponible=true
```

---

#  Modal del Libro

Al hacer clic en cualquier libro, se abre un modal con información detallada y opciones de acción.

## Sin Autenticar

Si el usuario **no ha iniciado sesión**, el modal muestra:

- Información básica del libro
- Mensaje: "Inicia sesión para acceder a todas las funciones"
- Botón: "Iniciar Sesión"

![Imagen](.gitbook/assets/modal_no_logueado.png)

## Con Autenticación

Para usuarios autenticados, el modal incluye:

**Información del libro:**

- Portada
- Título y autor
- Descripción completa
- Género
- Año de publicación
- ISBN
- Calificación promedio ()
- Reviews de usuarios

**Acciones disponibles:**

-  **Préstamo Digital** (si está disponible digitalmente)
-  **Préstamo Físico** (si hay copias físicas)
-  **Agregar a Lista de Deseos**
-  **Descargar** (si está habilitado)
-  **Calificar y Comentar**

![Imagen](.gitbook/assets/modal_logueado.png)

### Estados de Disponibilidad

El modal muestra claramente el estado:

---

#  Préstamo Físico (Desde Modal)

Al hacer clic en **"Préstamo Físico"**, se abre un segundo modal para seleccionar detalles.

## Seleccionar Fecha de Recogida

![Imagen](.gitbook/assets/prestamo_fisico.png)

**Campos del formulario:**

- `Fecha de recogida`: Calendario (mínimo mañana, máximo 7 días)
- `Confirmar`: Botón para enviar solicitud

**Al confirmar:**

1. Se crea el préstamo con estado "pendiente"
2. Se envía correo de confirmación
3. El modal se cierra y muestra mensaje de éxito

![Imagen](.gitbook/assets/correo_prestamo_fisico.png)

---

#  Lista de Deseos

Gestión de libros guardados para leer más tarde.

## Agregar a Lista de Deseos

**Endpoint:** `POST /wishlist/add`

Desde el modal del libro, clic en el icono de corazón 

**Datos enviados:**

```json
{
  "openlibrary_key": "/works/OL45883W",
  "book_title": "El Principito",
  "book_author": "Antoine de Saint-Exupéry"
}
```

**Respuesta:**

```json
{
  "message": "Libro agregado a tu lista de deseos",
  "wishlist_id": 123
}
```

![Imagen](.gitbook/assets/guarda_lista_deseos.png)

## Ver Lista de Deseos

**Endpoint:** `GET /wishlist/list`

**URL:** `/lista-de-deseos`

Acceso desde el menú principal → "Lista de Deseos"

![Imagen](.gitbook/assets/lista_deseos.png)

**Funcionalidades:**

- Ver todos los libros guardados
- Quitar libros (clic en )
- Acceder directamente al libro (clic en el libro)
- Filtrar por disponibilidad

### Quitar de Lista

**Endpoint:** `DELETE /wishlist/delete/{book_id}`

Simplemente haz clic en el icono de eliminar () junto al libro.

**Respuesta:**

```json
{
  "message": "Libro eliminado de tu lista de deseos"
}
```

---

#  Descargas

Algunos libros tienen habilitada la opción de descarga para leer offline.

## ¿Cómo funciona?

1. En el modal del libro, si la descarga está habilitada, aparece el botón **"Descargar PDF"**
2. Al hacer clic:
   
   - Si es un libro con archivo directo → Descarga inmediata
   - Si no → Redirige a la página de lectura digital

3. El sistema registra la descarga para estadísticas

![Imagen](.gitbook/assets/download_button.png)

.. note::
   
   No todos los libros permiten descarga por restricciones de derechos de autor. Solo los marcados por bibliotecarios como "permitir_descarga" tendrán esta opción.

---

#  Mi Perfil

**Endpoint:** `GET /users/me`

**URL:** `/mi-perfil`

Ver y editar información personal de la cuenta.

## Información Mostrada

![Imagen](.gitbook/assets/mi_perfil.png)

**Secciones del perfil:**

1. **Datos personales:**
   
   - Nombre completo
   - Correo electrónico
   - Tipo y número de identificación
   - Fecha de registro

2. **Estadísticas:**
   
   - Libros leídos
   - Calificaciones dadas
   - Comentarios publicados
   - Racha de lectura

3. **Configuración:**
   
   - Notificaciones por correo
   - Privacidad
   - Preferencias de idioma

## Editar Perfil

**Endpoint:** `PUT /users/me`

**Datos editables:**

```json
{
  "nombre": "Juan Carlos",
  "apellido": "Pérez García",
  "correo": "nuevo_correo@ejemplo.com"
}
```

.. note::
   
   No puedes editar tu número de identificación una vez registrado. Para cambios en este dato, contacta a un bibliotecario.

## Eliminar Cuenta

**Endpoint:** `DELETE /users/me`

.. warning::
   
   Esta acción es **permanente** y elimina:
   
   - Tu perfil y datos personales
   - Historial de préstamos (soft delete)
   - Lista de deseos
   - Calificaciones y comentarios
   
   **No puedes recuperar tu cuenta después de eliminarla.**

Al hacer clic en "Eliminar Cuenta":

1. Se muestra confirmación con checkbox: "Entiendo que esta acción es irreversible"
2. Se solicita ingresar contraseña para confirmar
3. Se elimina la cuenta (soft delete)
4. Se envía correo de confirmación de cierre

![Imagen](.gitbook/assets/delete_account_confirm.png)

---

#  Mis Préstamos Físicos

**Endpoint:** `GET /prestamos-fisicos/mis-prestamos`

**URL:** `/mis-prestamos`

Vista completa de todos los préstamos físicos del usuario.

![Imagen](.gitbook/assets/mis_prestamos.png)

## Información Mostrada

Para cada préstamo:

-  Portada y título del libro
-  Fecha de solicitud
-  Fecha de recogida programada
-  Fecha de devolución
-  Estado actual (badge con color)
- ⏱ Días restantes
-  Opción de cancelar (si aplica)

## Estados

## Cancelar Préstamo

Solo para préstamos en estado **"Pendiente"**.

Al hacer clic en "Cancelar":

1. Confirmación: "¿Estás seguro de cancelar este préstamo?"
2. Si confirmas → El préstamo se cancela
3. La copia física queda disponible nuevamente

![Imagen](.gitbook/assets/cancelar_prestamo.png)

---

#  Notificaciones

Los usuarios reciben notificaciones por correo para:

-  Confirmación de registro
-  Confirmación de préstamo físico
- ⏰ Recordatorio de recogida (1 día antes)
- ⏰ Recordatorio de devolución (2 días antes)
-  Alerta de retraso
-  Libro disponible (si estaba en lista de deseos)
-  Respuesta a comentario

.. tip::
   
   Puedes configurar qué notificaciones recibir desde tu perfil en "Configuración de Notificaciones".

---

#  Privacidad y Seguridad

.. note::
   
   **Tu información está protegida:**
   
   - Nadie más puede ver tu historial de préstamos
   - Tu lista de deseos es privada
   - Solo tú y los bibliotecarios pueden ver tus datos personales
   - Tus calificaciones son públicas pero anónimas (solo se muestra tu nombre de usuario)
   - Puedes eliminar tu cuenta en cualquier momento