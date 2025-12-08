.. Aeternum documentation master file

====================================
Bienvenido a Aeternum
====================================

.. raw:: html

   <div style="text-align: center; padding: 2rem 0 3rem 0;">
     <h2 style="font-size: 1.4rem; color: #b8b8b8; max-width: 800px; margin: 0 auto; line-height: 1.8; font-weight: 400;">
       Una plataforma moderna de biblioteca virtual que revoluciona la forma en que accedes a los libros. 
       Combina lo mejor de dos mundos: préstamos físicos tradicionales y acceso digital instantáneo.
     </h2>
   </div>

----

Características Principales
================================

.. raw:: html

   <div class="feature-grid">
     <div class="feature-card">
       <h3>Autenticación Segura</h3>
       <p>Sistema robusto con JWT, recuperación de contraseña y protección contra ataques de fuerza bruta.</p>
     </div>
     
     <div class="feature-card">
       <h3>Préstamos Duales</h3>
       <p>Solicita libros físicos o accede a versiones digitales instantáneamente desde cualquier dispositivo.</p>
     </div>
     
     <div class="feature-card">
       <h3>Lista de Deseos</h3>
       <p>Guarda tus libros favoritos y ten un acceso directo a los libros que mas te gusten.</p>
     </div>
     
     <div class="feature-card">
       <h3>Reviews & Ratings</h3>
       <p>Califica y comenta libros. Ayuda a otros usuarios a descubrir grandes lecturas.</p>
     </div>
     
     <div class="feature-card">
       <h3>Descargas</h3>
       <p>Descarga libros para leer sin conexión cuando lo necesites.</p>
     </div>
     
     <div class="feature-card">
       <h3>Panel Admin</h3>
       <p>Gestión completa de libros, usuarios y préstamos para bibliotecarios.</p>
     </div>
   </div>

----

Inicio Rápido
=================

¿Nuevo en Aeternum? Empieza aquí:

1. Lee la :doc:`introduccion` para conocer el proyecto
2. Sigue la guía de :doc:`instalacion` para configurar el entorno
3. Explora la :doc:`arquitectura` del sistema
4. Consulta la documentación de la :doc:`api` para integrar

----

Contenido de la Documentación
==================================

.. toctree::
   :maxdepth: 2
   :caption: Comenzando

   introduccion
   instalacion
   arquitectura

.. toctree::
   :maxdepth: 2
   :caption: Autenticación

   auth_routes
   password_reset

.. toctree::
   :maxdepth: 2
   :caption: Módulo de Usuarios

    usuario

.. toctree::
   :maxdepth: 2
   :caption: Gestión de Libros

   catalogo
   prestamos
   reviews

.. toctree::
   :maxdepth: 2
   :caption: Administración

   administracion
   gestion_prestamos

.. toctree::
   :maxdepth: 2
   :caption: Referencia Técnica

   backend
   frontend
   api
   seguridad

----

Modelo de Base de Datos
========================

Modelo Entidad-Relación (MER)
------------------------------

El siguiente diagrama muestra el modelo conceptual de la base de datos de Aeternum, incluyendo todas las entidades y sus relaciones.

.. image:: _static/mer_aeternum.jpg
   :alt: Modelo Entidad-Relación de Aeternum
   :align: center
   :width: 90%

.. tip::
   
   Haz clic en la imagen para verla en tamaño completo y examinar las relaciones entre las entidades.

----

Modelo Relacional (MR)
=======================

Esquema de Base de Datos
-------------------------

Este diagrama representa el esquema relacional implementado en MySQL, con todas las tablas, campos y claves foráneas.

.. image:: _static/mr_aeternum.jpg
   :alt: Modelo Relacional de Aeternum
   :align: center
   :width: 90%

**Tablas principales:**

- **usuarios**: Gestión de cuentas de usuarios y bibliotecarios
- **libros**: Catálogo completo de libros disponibles
- **prestamos_fisicos**: Control de préstamos de copias físicas
- **prestamos_digitales**: Registro de acceso a versiones digitales
- **wishlist**: Listas de deseos personalizadas
- **reviews**: Calificaciones y comentarios de usuarios
- **consentimientos**: Cumplimiento GDPR

----

Casos de Uso
============

Diagramas de Casos de Uso del Sistema
--------------------------------------

Los siguientes diagramas ilustran las principales interacciones entre los actores (usuarios y bibliotecarios) y el sistema Aeternum.

Caso de Uso: Usuario
^^^^^^^^^^^^^^^^^^^^^

.. image:: _static/caso_de_uso_1.jpg
   :alt: Diagrama de Casos de Uso - Usuario
   :align: center
   :width: 85%

Funcionalidades disponibles para usuarios regulares:

- Registro e inicio de sesión
- Búsqueda y exploración del catálogo
- Solicitud de préstamos físicos y digitales
- Gestión de lista de deseos
- Calificación y comentarios de libros
- Administración de perfil personal

Caso de Uso: Bibliotecario
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: _static/caso_de_uso_2.jpg
   :alt: Diagrama de Casos de Uso - Bibliotecario
   :align: center
   :width: 85%

Funcionalidades administrativas:

- Gestión completa del catálogo de libros
- Administración de usuarios
- Control de préstamos físicos
- Generación de reportes
- Moderación de contenido

Caso de Uso: Sistema Completo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: _static/caso_de_uso_3.jpg
   :alt: Diagrama de Casos de Uso - Sistema Completo
   :align: center
   :width: 85%

Vista general de todos los casos de uso del sistema, incluyendo interacciones con APIs externas y servicios de terceros.

----

Stack Tecnológico
======================

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Tecnología
     - Descripción
   * - **Frontend**
     - React 18 + Vite + TailwindCSS
   * - **Backend**
     - FastAPI (Python 3.11+)
   * - **Base de Datos**
     - MySQL / Railway
   * - **Cache**
     - Redis
   * - **Autenticación**
     - JWT (JSON Web Tokens)
   * - **Email**
     - SMTP con templates HTML

----

Agradecimientos
===============

.. raw:: html

   <div style="background: linear-gradient(135deg, rgba(255, 105, 180, 0.1), rgba(186, 142, 217, 0.1)); 
               padding: 2.5rem; 
               border-radius: 12px; 
               border-left: 4px solid #FF69B4; 
               margin: 3rem 0;">
     <h3 style="color: #FF69B4; margin-top: 0; font-size: 1.8rem;">Agradecemos a ...</h3>
     
     <p style="font-size: 1.1em; line-height: 1.8; color: #e8e8e8; margin-bottom: 1.5rem;">
       Este proyecto no habría sido posible sin el apoyo y colaboración de diversas personas y comunidades.
     </p>
     
     <div style="margin: 2rem 0;">
       <h4 style="color: #BA8ED9; margin-bottom: 1rem;">IA</h4>
       <p style="color: #b8b8b8; line-height: 1.6;">
         Gracias a la inteligencia artificial por asistir en gran parte del proyecto, por dar errores mas que soluciones, sacar canas y demás pero se gracias a esta pudimos completar el proyecto.
       </p>
     </div>
     
     <div style="margin: 2rem 0;">
       <h4 style="color: #BA8ED9; margin-bottom: 1rem;">Open Library API</h4>
       <p style="color: #b8b8b8; line-height: 1.6;">
         Por proporcionar acceso gratuito a millones de libros y sus metadatos, haciendo posible 
         un catálogo extenso y actualizado.
       </p>
     </div>
     
     <div style="margin: 2rem 0;">
       <h4 style="color: #BA8ED9; margin-bottom: 1rem;">Mariana Ruiz</h4>
       <p style="color: #b8b8b8; line-height: 1.6;">
         Por el apoyo que dio, creación de código, aportes en diseño y bugs con influencia en funciones de código.
       </p>
     </div>
     
     <div style="margin: 2rem 0;">
       <h4 style="color: #BA8ED9; margin-bottom: 1rem;">Santiago Tuta</h4>
       <p style="color: #b8b8b8; line-height: 1.6;">
         Por apoyar en creación de proyecto, documentación, aportar en diseño y reportees de bugs.
       </p>
     </div>
     
     <div style="text-align: center; margin-top: 2rem; padding-top: 2rem; border-top: 1px solid rgba(255, 105, 180, 0.2);">
       <p style="color: #FF69B4; font-size: 1.2em; font-weight: 600;">
         Construyendo un proyecto con el que estemos conformes mientras aprendemos y nos divertimos.
       </p>
     </div>
   </div>

----

.. raw:: html

   <div style="background: rgba(255, 105, 180, 0.1); 
               padding: 2rem; 
               border-radius: 12px; 
               border-left: 4px solid #FF69B4; 
               margin: 3rem 0;">
     <h3 style="color: #FF69B4; margin-top: 0;">¿Necesitas ayuda?</h3>
     <p style="font-size: 1.1em; line-height: 1.7; margin-bottom: 1rem; color: #e8e8e8;">
       Estamos aquí para ayudarte a sacar el máximo provecho de Aeternum.
     </p>
     <ul style="list-style: none; padding: 0; color: #b8b8b8;">
       <li style="margin: 0.5rem 0;">📧 Email: aeternum538@gmail.com</li>
       <li style="margin: 0.5rem 0;">🐛 Reportar bug: <a href="https://github.com/Santixxtt/Aeternum/issues" style="color: #FF69B4;">GitHub Issues</a></li>
       <li style="margin: 0.5rem 0;">Documentación completa en esta misma página</li>
     </ul>
   </div>

----

.. note::
   
   **Desarrollador:** Mariana Ruiz
   **Desarrollador:** Santiago Tuta 
   **Versión actual:** 1.0.0  
   **Última actualización:** Enero 2025  
   **Licencia:** MIT