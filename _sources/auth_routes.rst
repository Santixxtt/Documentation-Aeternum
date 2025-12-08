============================
Autenticación de Usuarios
============================

Este módulo maneja todo lo relacionado con el registro y login de usuarios en Aeternum.

.. note::

   Aeternum utiliza **JWT (JSON Web Tokens)** para autenticación segura y **bcrypt** para encriptación de contraseñas.

----

Iniciar Sesión
==================

**Endpoint:** ``POST /auth/login``

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/auth/login</code>
     </div>
     <p>Permite a los usuarios iniciar sesión en el sistema usando su correo y contraseña.</p>
   </div>

¿Qué hace?
----------

1. Verifica que el correo esté registrado en el sistema.
2. Comprueba que la contraseña sea correcta (bcrypt).
3. Si todo está bien, genera un **token JWT** para acceder al sistema.
4. Si fallas **3 veces seguidas**, se bloquea la cuenta por **15 minutos** (protección contra fuerza bruta).

.. image:: _static/login.png
   :alt: Pantalla de inicio de sesión
   :align: center
   :width: 500px

Datos a Enviar
--------------

.. code-block:: json

   {
     "correo": "usuario@ejemplo.com",
     "clave": "miContraseña123"
   }

**Campos:**

- ``correo`` (string, requerido): Correo electrónico registrado.
- ``clave`` (string, requerido): Contraseña del usuario.

Respuesta Exitosa
-----------------

.. code-block:: json

   {
     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "token_type": "bearer",
     "rol": "usuario"
   }

**Campos de respuesta:**

- ``access_token``: Token JWT para autenticación (válido por 24 horas).
- ``token_type``: Siempre ``bearer``.
- ``rol``: Rol del usuario (``usuario`` o ``bibliotecario``).

.. tip::

   Guarda el ``access_token`` de forma segura. Debes incluirlo en el header:
   ``Authorization: Bearer {token}`` para todas las peticiones autenticadas.

Posibles Errores
----------------

**Correo no registrado:**

.. code-block:: json

   {
     "detail": "El correo no está registrado"
   }

.. image:: _static/correo_no_existe_login.png
   :alt: Error de correo no registrado
   :align: center
   :width: 450px

**Contraseña incorrecta:**

.. code-block:: json

   {
     "detail": "Clave incorrecta. Intentos restantes: 2"
   }

.. image:: _static/clave_incorrecta_login.png
   :alt: Error: clave incorrecta
   :align: center
   :width: 450px

**Cuenta bloqueada:**

.. code-block:: json

   {
     "detail": "Cuenta bloqueada temporalmente. Intenta en 15 minutos"
   }

.. image:: _static/cuenta_bloqueda_login.png
   :alt: Error: cuenta bloqueada
   :align: center
   :width: 450px

----

Registrar Nueva Cuenta
===========================

**Endpoint:** ``POST /auth/register``

.. raw:: html

   <div class="endpoint-card">
     <div class="endpoint-title">
       <span class="http-method method-post">POST</span>
       <code>/auth/register</code>
     </div>
     <p>Crea una nueva cuenta de usuario en Aeternum.</p>
   </div>

¿Qué hace?
----------

1. Verifica que el **correo** no esté registrado.
2. Valida que el **número de identificación** sea único.
3. Encripta la contraseña con **bcrypt**.
4. Guarda la aceptación de la **política de privacidad**.
5. Crea la cuenta con rol ``usuario`` por defecto.
6. Registra metadata (IP, navegador, fecha) para cumplimiento GDPR.

.. image:: _static/registro.png
   :alt: Formulario de registro
   :align: center
   :width: 500px

Datos a Enviar
--------------

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

**Campos:**

- ``nombre`` (string, requerido): Nombre del usuario.
- ``apellido`` (string, requerido): Apellido del usuario.
- ``tipo_identificacion`` (string, requerido): Tipo de documento  
  - Valores válidos: ``CC``, ``TI``, ``CE``, ``PA``
- ``num_identificacion`` (string, requerido): Número del documento.
- ``correo`` (string, requerido): Correo electrónico único.
- ``clave`` (string, requerido): Contraseña segura  
  - Mínimo 8 caracteres  
  - 1 mayúscula, 1 minúscula y 1 número
- ``rol`` (string, opcional): Rol asignado (default: ``usuario``).
- ``consent`` (boolean, requerido): Debe ser ``true``.

Respuesta Exitosa
-----------------

.. code-block:: json

   {
     "message": "¡Cuenta creada con éxito!",
     "user_id": 42
   }

Después de registrarte, recibirás un correo para verificar la cuenta.

.. image:: _static/correo_verificacion_cuenta.jpg
   :alt: Verificación de correo
   :align: center
   :width: 500px

.. tip::

   Después de registrarte, usa el endpoint de **login** para obtener tu token y comenzar a usar Aeternum.

Posibles Errores
----------------

**Falta consentimiento:**

.. code-block:: json

   {
     "detail": "Debes aceptar la Política de Privacidad para continuar"
   }

.. image:: _static/consent_required.png
   :alt: Consentimiento requerido
   :align: center
   :width: 450px

**Correo ya registrado:**

.. code-block:: json

   {
     "detail": "El correo ya está registrado"
   }

.. image:: _static/correo_registrado.jpeg
   :alt: Correo ya registrado
   :align: center
   :width: 450px

**Documento ya registrado:**

.. code-block:: json

   {
     "detail": "El número de identificación ya está registrado"
   }

.. image:: _static/numero_identificacion_registrado.jpeg
   :alt: Documento ya registrado
   :align: center
   :width: 450px

**Contraseña débil:**

.. code-block:: json

   {
     "detail": "La contraseña debe tener al menos 8 caracteres, una mayúscula y un número"
   }

----

Notas de Seguridad
==================

.. warning::

   **Protecciones implementadas:**

**1. Encriptación de Contraseñas**

- bcrypt cost 12  
- Cada contraseña posee "salt" único  
- Ningún administrador puede ver la contraseña real  

**2. Protección contra Fuerza Bruta**

- Intentos 1 y 2 permitidos  
- Intento 3 → bloqueo de **15 minutos**  
- Redis para rastreo  
- Reset tras login exitoso  

**3. Registro de Consentimiento (GDPR)**

- Fecha y hora de aceptación  
- IP del usuario  
- User-Agent  
- Versión de la política aceptada  

**4. Tokens JWT**

- Expiración: **8 horas**  
- Firmados con clave secreta  
- Incluyen: ``user_id``, ``correo``, ``rol``  
- No contienen información sensible  

**5. Validación de Datos**

- Formato email válido  
- Contraseñas con requisitos mínimos  
- Documentos únicos  
- Sanitización de inputs  

----

Mejores Prácticas
=================

Para Usuarios
-------------

.. tip::

   - Usa contraseñas únicas.  
   - No compartas tu token.  
   - Cierra sesión en dispositivos compartidos.  
   - Actualiza tu contraseña cada 3-6 meses.  

Para Desarrolladores
--------------------

.. code-block:: javascript

   // ✓ CORRECTO: Guardar token de forma segura
   localStorage.setItem('token', response.access_token);

   // ✓ CORRECTO: Usar token en headers
   headers: {
     'Authorization': `Bearer ${token}`
   }

   // ✗ INCORRECTO: Nunca guardes contraseñas
   // localStorage.setItem('password', password);

.. note::

   El token debe incluirse en todas las peticiones a endpoints protegidos usando
   el header ``Authorization`` para realizar pruebas (por ejemplo, en POSTMAN).
