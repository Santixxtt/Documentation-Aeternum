
.. Aeternum documentation master file

====================================
Bienvenido a Aeternum 📚
====================================

.. image:: _static/aeternum_logo.png
   :alt: Logo Aeternum
   :align: center
   :width: 200px

|

**Aeternum** es una plataforma moderna de biblioteca virtual que revoluciona la forma en que accedes a los libros. 
Combina lo mejor de dos mundos: préstamos físicos tradicionales y acceso digital instantáneo.

----

✨ Características Principales
================================

.. raw:: html

   <div class="feature-grid">
     <div class="feature-card">
       <div class="feature-icon">🔐</div>
       <h3>Autenticación Segura</h3>
       <p>Sistema robusto con JWT, recuperación de contraseña y protección contra ataques de fuerza bruta.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon">📖</div>
       <h3>Préstamos Duales</h3>
       <p>Solicita libros físicos o accede a versiones digitales instantáneamente desde cualquier dispositivo.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon">💝</div>
       <h3>Lista de Deseos</h3>
       <p>Guarda tus libros favoritos y recibe notificaciones cuando estén disponibles.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon">⭐</div>
       <h3>Reviews & Ratings</h3>
       <p>Califica y comenta libros. Ayuda a otros usuarios a descubrir grandes lecturas.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon">📥</div>
       <h3>Descargas</h3>
       <p>Descarga libros para leer sin conexión cuando lo necesites.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon">👨‍💼</div>
       <h3>Panel Admin</h3>
       <p>Gestión completa de libros, usuarios y préstamos para bibliotecarios.</p>
     </div>
   </div>

----

🚀 Inicio Rápido
=================

¿Nuevo en Aeternum? Empieza aquí:

1. Lee la :doc:`introduccion` para conocer el proyecto
2. Sigue la guía de :doc:`instalacion` para configurar el entorno
3. Explora la :doc:`arquitectura` del sistema
4. Consulta la documentación de la :doc:`api` para integrar

----

📖 Contenido de la Documentación
==================================

.. toctree::
   :maxdepth: 2
   :caption: 🎯 Comenzando

   introduccion
   instalacion
   arquitectura

.. toctree::
   :maxdepth: 2
   :caption: 🔐 Autenticación

   auth_routes
   password_reset

.. toctree::
   :maxdepth: 2
   :caption: 👤 Módulo de Usuarios

   usuario
   perfil
   wishlist

.. toctree::
   :maxdepth: 2
   :caption: 📚 Gestión de Libros

   catalogo
   prestamos
   reviews

.. toctree::
   :maxdepth: 2
   :caption: 👨‍💼 Administración

   administracion
   gestion_prestamos

.. toctree::
   :maxdepth: 2
   :caption: 🔧 Técnico

   backend
   frontend
   api
   seguridad

----

🛠️ Stack Tecnológico
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