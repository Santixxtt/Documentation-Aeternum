============================
Sistema de Préstamos
============================

Aeternum ofrece dos tipos de préstamos: **digitales** (lectura online instantánea) y **físicos** (recogida en biblioteca).

.. note::
   
   Ambos sistemas están integrados para ofrecer la mejor experiencia al usuario.

----

📖 Préstamos Digitales
========================

Los préstamos digitales permiten acceso inmediato a la versión digital de un libro para leerlo en línea.

Registrar Préstamo Digital
----------------------------

**Endpoint:** ``POST /prestamos/digital``

Registra un nuevo préstamo digital cuando un usuario accede a leer un libro online.

**¿Qué hace?**

1. Verifica que el usuario esté autenticado
2. Comprueba disponibilidad de copias digitales
3. Registra el préstamo en el sistema
4. Redirige al lector online
5. Registra estadísticas de lectura

**Datos a enviar:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "book_title": "El Principito",
     "book_author": "Antoine de Saint-Exupéry"
   }

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Préstamo digital registrado exitosamente",
     "prestamo_id": 123,
     "url_lectura": "https://aeternum.com/leer/OL45883W",
     "fecha_inicio": "2025-01-15T14:30:00",
     "fecha_expiracion": "2025-01-27T14:30:00"
   }

.. image:: _static/prestamo_digital.png
   :alt: Préstamo digital
   :align: center
   :width: 600px

**Características:**

- Acceso inmediato sin espera
- Duración: 12 días por defecto
- Sin límite de copias (si ``copias_digitales_disponibles = -1``)
- Registro de tiempo de lectura
- Marcadores automáticos de progreso

**Posibles errores:**

- Sin copias disponibles: "No hay copias digitales disponibles en este momento"
- Límite alcanzado: "Has alcanzado el límite de préstamos simultáneos (3)"
- Libro no disponible digitalmente: "Este libro no está disponible en formato digital"

.. image:: _static/error_prestamo_digital.png
   :alt: Error préstamo digital
   :align: center
   :width: 400px

----

Lector Online
--------------

**URL:** ``/leer/{openlibrary_key}``

Interface de lectura integrada en el navegador.

**Funcionalidades del lector:**

- 📖 Navegación por páginas
- 🔖 Marcadores y notas personales
- 🔍 Búsqueda dentro del libro
- 🌙 Modo nocturno
- 📏 Ajuste de tamaño de fuente
- 💾 Guardado automático de progreso
- ⏱️ Registro de tiempo de lectura

.. image:: _static/lector_online.png
   :alt: Lector online
   :align: center
   :width: 600px

**Controles principales:**

.. code-block:: text

   ← Anterior    [Progreso: 45%]    Siguiente →
   
   [🔖 Marcar]  [🔍 Buscar]  [⚙️ Ajustes]  [🌙 Modo]

.. image:: _static/lector_controles.png
   :alt: Controles del lector
   :align: center
   :width: 500px

----

Historial de Lectura
---------------------

**Endpoint:** ``GET /prestamos/digitales/mi-historial``

Obtiene el historial completo de préstamos digitales del usuario.

**Respuesta:**

.. code-block:: json

   {
     "total_prestamos": 15,
     "prestamos_activos": 2,
     "historial": [
       {
         "prestamo_id": 123,
         "book_title": "El Principito",
         "book_author": "Antoine de Saint-Exupéry",
         "fecha_inicio": "2025-01-15T14:30:00",
         "fecha_expiracion": "2025-01-27T14:30:00",
         "progreso_lectura": 45,
         "tiempo_lectura_minutos": 180,
         "estado": "activo"
       },
       {
         "prestamo_id": 122,
         "book_title": "Cien Años de Soledad",
         "book_author": "Gabriel García Márquez",
         "fecha_inicio": "2025-01-01T10:00:00",
         "fecha_finalizacion": "2025-01-10T22:30:00",
         "progreso_lectura": 100,
         "tiempo_lectura_minutos": 720,
         "estado": "completado"
       }
     ]
   }

.. image:: _static/historial_digital.png
   :alt: Historial de lectura
   :align: center
   :width: 600px

----

📦 Préstamos Físicos
=====================

Los préstamos físicos permiten solicitar un libro para recogerlo en la biblioteca.

Solicitar Préstamo Físico
---------------------------

**Endpoint:** ``POST /prestamos-fisicos/solicitar``

Crea una solicitud de préstamo físico de un libro.

**¿Qué hace?**

1. Verifica disponibilidad de copias físicas
2. Valida que el usuario no tenga préstamos vencidos
3. Comprueba el límite de préstamos simultáneos
4. Crea la solicitud con estado "pendiente"
5. Envía correo de confirmación al usuario
6. Notifica al bibliotecario

**Datos a enviar:**

.. code-block:: json

   {
     "openlibrary_key": "/works/OL45883W",
     "book_title": "El Principito",
     "book_author": "Antoine de Saint-Exupéry",
     "fecha_recogida": "2025-01-20"
   }

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Solicitud de préstamo creada exitosamente",
     "prestamo_id": 456,
     "estado": "pendiente",
     "fecha_recogida": "2025-01-20",
     "fecha_devolucion": "2025-02-01",
     "instrucciones": "Presenta tu identificación en el mostrador de préstamos."
   }

.. image:: _static/prestamo_fisico.png
   :alt: Solicitar préstamo físico
   :align: center
   :width: 600px

**Correo de confirmación enviado:**

.. image:: _static/correo_prestamo_fisico.png
   :alt: Correo de confirmación
   :align: center
   :width: 500px

**Validaciones:**

- Usuario con préstamos vencidos: No puede solicitar nuevos
- Límite de 3 préstamos físicos simultáneos
- Fecha de recogida debe ser futura (mínimo 1 día de anticipación)
- Debe haber copias físicas disponibles

**Posibles errores:**

- Sin copias: "No hay copias físicas disponibles"
- Préstamos vencidos: "Tienes préstamos vencidos. Devuélvelos para continuar"
- Límite alcanzado: "Has alcanzado el límite de 3 préstamos físicos simultáneos"
- Fecha inválida: "La fecha de recogida debe ser al menos 1 día en el futuro"

.. image:: _static/error_prestamo_fisico.png
   :alt: Error préstamo físico
   :align: center
   :width: 400px

----

Ver Mis Préstamos Físicos
---------------------------

**Endpoint:** ``GET /prestamos-fisicos/mis-prestamos``

Lista todos los préstamos físicos del usuario actual.

**Filtros opcionales:**

- ``estado``: pendiente | activo | devuelto | cancelado | retrasado
- ``page``: Número de página
- ``limit``: Resultados por página

**Ejemplo de URL:**

.. code-block:: text

   GET /prestamos-fisicos/mis-prestamos?estado=activo&page=1

**Respuesta:**

.. code-block:: json

   {
     "total_prestamos": 8,
     "prestamos_activos": 2,
     "prestamos_retrasados": 0,
     "prestamos": [
       {
         "prestamo_id": 456,
         "book_title": "El Principito",
         "book_author": "Antoine de Saint-Exupéry",
         "openlibrary_key": "/works/OL45883W",
         "fecha_solicitud": "2025-01-15T14:30:00",
         "fecha_recogida": "2025-01-20",
         "fecha_devolucion": "2025-02-01",
         "estado": "pendiente",
         "dias_restantes": 5,
         "puede_cancelar": true
       },
       {
         "prestamo_id": 455,
         "book_title": "Cien Años de Soledad",
         "book_author": "Gabriel García Márquez",
         "openlibrary_key": "/works/OL123456W",
         "fecha_solicitud": "2025-01-10T09:00:00",
         "fecha_recogida": "2025-01-12",
         "fecha_devolucion": "2025-01-24",
         "fecha_recogida_real": "2025-01-12T10:30:00",
         "estado": "activo",
         "dias_restantes": 8,
         "puede_cancelar": false
       }
     ]
   }

.. image:: _static/mis_prestamos.png
   :alt: Mis préstamos físicos
   :align: center
   :width: 600px

**Estados explicados:**

- **🟡 Pendiente**: Libro reservado, esperando que lo recojas
- **🟢 Activo**: Libro en tu poder, debes devolverlo antes de la fecha
- **🔴 Retrasado**: Pasó la fecha de devolución
- **⚪ Devuelto**: Préstamo completado
- **❌ Cancelado**: Solicitud cancelada

----

Cancelar Préstamo Físico
--------------------------

**Endpoint:** ``PUT /prestamos-fisicos/cancelar/{prestamo_id}``

Permite al usuario cancelar un préstamo físico.

**¿Cuándo se puede cancelar?**

- Solo préstamos en estado **"pendiente"** (antes de recoger el libro)
- No se puede cancelar después de recoger el libro

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Préstamo cancelado exitosamente",
     "prestamo_id": 456,
     "libro_disponible_nuevamente": true
   }

.. image:: _static/cancelar_prestamo.png
   :alt: Cancelar préstamo
   :align: center
   :width: 400px

**Posibles errores:**

- Ya recogido: "No puedes cancelar un préstamo activo. Debes devolverlo en biblioteca"
- No encontrado: "El préstamo no existe"
- Ya procesado: "Este préstamo ya fue devuelto o cancelado"

----

🔔 Notificaciones y Recordatorios
===================================

El sistema envía notificaciones automáticas por correo:

Notificaciones por Correo
---------------------------

**Tipos de notificaciones:**

1. **Confirmación de solicitud** (inmediato)
   
   - Detalles del libro
   - Fecha de recogida
   - Instrucciones

2. **Recordatorio de recogida** (1 día antes)
   
   - Libro reservado te espera
   - Horario de atención
   - Link para cancelar si es necesario

3. **Confirmación de entrega** (cuando el bibliotecario marca como "activo")
   
   - Fecha de devolución
   - Consecuencias del retraso
   - Renovación (si aplica)

4. **Recordatorio de devolución** (2 días antes de vencer)
   
   - Libro próximo a vencer
   - Fecha límite
   - Instrucciones de devolución

5. **Alerta de retraso** (si pasa la fecha)
   
   - Préstamo vencido
   - Posible penalización
   - Urgencia en devolución

.. image:: _static/email_recordatorio.png
   :alt: Email de recordatorio
   :align: center
   :width: 500px

----

📊 Estadísticas de Préstamos
==============================

Dashboard Personal
-------------------

**Endpoint:** ``GET /prestamos/estadisticas``

Obtiene estadísticas personales de préstamos del usuario.

**Respuesta:**

.. code-block:: json

   {
     "total_prestamos": 23,
     "prestamos_completados": 20,
     "prestamos_activos": 3,
     "prestamos_retrasados": 0,
     "libros_favoritos": ["El Principito", "Cien Años de Soledad"],
     "tiempo_lectura_total_horas": 45,
     "racha_actual_dias": 15,
     "insignias": ["Lector frecuente", "Sin retrasos"]
   }

.. image:: _static/estadisticas_usuario.png
   :alt: Estadísticas personales
   :align: center
   :width: 600px

----

⚙️ Políticas de Préstamos
===========================

Límites y Restricciones
-------------------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Política
     - Valor
   * - **Préstamos digitales simultáneos**
     - 3 libros
   * - **Préstamos físicos simultáneos**
     - 3 libros
   * - **Duración préstamo digital**
     - 12 días
   * - **Duración préstamo físico**
     - 12 días (desde recogida)
   * - **Tiempo para recoger**
     - 3 días (luego se cancela automáticamente)
   * - **Renovación**
     - 1 renovación de 12 días más (si no hay reservas)
   * - **Penalización por retraso**
     - 7 días sin poder solicitar nuevos préstamos

Renovación de Préstamos
-------------------------

**Endpoint:** ``PUT /prestamos-fisicos/renovar/{prestamo_id}``

Extiende un préstamo físico por 12 días adicionales.

**Condiciones:**

- Solo 1 renovación permitida
- No puede haber reservas del libro por otros usuarios
- Debe renovarse antes de la fecha de devolución
- No aplicable si hay retrasos previos

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "Préstamo renovado exitosamente",
     "nueva_fecha_devolucion": "2025-02-13"
   }

.. image:: _static/renovar_prestamo.png
   :alt: Renovar préstamo
   :align: center
   :width: 500px

----

🔒 Notas de Seguridad
======================

.. warning::
   
   **Protección de datos:**
   
   - Los préstamos son privados (solo el usuario y bibliotecarios pueden verlos)
   - El historial se mantiene por tiempo indefinido
   - Los datos de lectura (progreso, tiempo) son confidenciales
   - Las notificaciones no revelan información sensible

.. tip::
   
   **Recomendaciones:**
   
   - Configura notificaciones para no olvidar devoluciones
   - Devuelve libros a tiempo para mantener tu historial limpio
   - Usa renovaciones si necesitas más tiempo
   - Cancela reservas si cambias de opinión (libera el libro para otros)