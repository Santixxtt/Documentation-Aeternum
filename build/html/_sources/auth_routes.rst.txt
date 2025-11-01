Autenticación de Usuarios
==========================

Este módulo maneja todo lo relacionado con el registro y login de usuarios en Aeternum.

Iniciar Sesión
--------------

**Endpoint:** ``POST /auth/login``

Permite a los usuarios iniciar sesión en el sistema usando su correo y contraseña.

**¿Qué hace?**

1. Verifica que el correo esté registrado
2. Comprueba que la contraseña sea correcta
3. Si todo está bien, te da un token para acceder al sistema
4. Si fallas 3 veces seguidas, bloquea tu cuenta por 15 minutos (por seguridad)

**Lo que necesitas enviar:**

- ``correo``: Tu correo electrónico registrado  
- ``clave``: Tu contraseña

**Lo que recibes si todo sale bien:**

- Un token de acceso (para usarlo en otras peticiones)  
- Tu rol en el sistema (por defecto "usuario")

.. image:: _static/login.png
   :alt: Ejemplo de pantalla de login
   :align: center
   :width: 400px


**Posibles errores:**

- Si el correo no existe: "El correo no está registrado"

  .. image:: _static/correo_no_existe_login.png
     :alt: Error: correo no registrado
     :align: center
     :width: 400px

- Si la contraseña está mal: "Clave incorrecta. Intentos restantes: X"

  .. image:: _static/clave_incorrecta_login.png
     :alt: Error: clave incorrecta
     :align: center
     :width: 400px

- Si intentaste muchas veces: "Cuenta bloqueada. Intenta más tarde"

  .. image:: _static/cuenta_bloqueda_login.png
     :alt: Error: cuenta bloqueada
     :align: center
     :width: 400px


**Ejemplo de uso:**

.. code-block:: json

   {
     "correo": "usuario@ejemplo.com",
     "clave": "miContraseña123"
   }

**Respuesta exitosa:**

.. code-block:: json

   {
     "access_token": "eyJhbGciOiJI...",
     "token_type": "bearer",
     "rol": "usuario"
   }

---

Registrar Nueva Cuenta
-----------------------

**Endpoint:** ``POST /auth/register``

Crea una nueva cuenta de usuario en Aeternum.

**¿Qué hace?**

1. Verifica que el correo no esté usado por otra persona  
2. Verifica que el número de identificación sea único  
3. Encripta tu contraseña (nadie puede verla, ni nosotros)  
4. Guarda tu aceptación de la política de privacidad  
5. Crea tu cuenta

.. image:: _static/registro.png
     :alt: Error: cuenta bloqueada
     :align: center
     :width: 400px

**Lo que necesitas enviar:**

- ``nombre``: Tu nombre  
- ``apellido``: Tu apellido  
- ``tipo_identificacion``: Tipo de documento (CC, TI, CE)  
- ``num_identificacion``: Número de tu documento  
- ``correo``: Tu correo electrónico (debe ser único)  
- ``clave``: Una contraseña segura  
- ``rol``: Rol que tendrás (normalmente "usuario")  
- ``consent``: ``true`` (debes aceptar la política de privacidad)

**Lo que recibes:**

- Un mensaje confirmando que tu cuenta fue creada  
- El ID de tu nueva cuenta

**Posibles errores:**

-  Si no aceptas la política: "Debes aceptar la Política de Privacidad"  

.. image:: _static/numero_identificacion_registrado.jpeg
     :alt: Error: cuenta bloqueada
     :align: center
     :width: 400px

-  Si el correo ya existe: "El correo ya está registrado" 

.. image:: _static/correo_registrado.jpeg
     :alt: Error: cuenta bloqueada
     :align: center
     :width: 400px

-  Si el documento ya existe: "El número de identificación ya está registrado"

.. image:: _static/numero_identificacion_registrado.jpeg
     :alt: Error: cuenta bloqueada
     :align: center
     :width: 400px

**Ejemplo de uso:**

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

**Respuesta exitosa:**

.. code-block:: json

   {
     "message": "¡Cuenta creada con éxito!",
     "user_id": 42
   }

---

Notas de Seguridad
------------------

 **Protección de contraseñas:** Todas las contraseñas se encriptan. Nadie puede verlas.

 **Protección contra ataques:** Si alguien intenta adivinar tu contraseña 3 veces, bloqueamos la cuenta por 15 minutos.

 **Registro de consentimiento:** Guardamos cuándo aceptaste la política de privacidad, desde qué IP y con qué navegador (para cumplir con las leyes de protección de datos).
