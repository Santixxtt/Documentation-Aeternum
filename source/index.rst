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
       <div class="feature-icon"></div>
       <h3>Autenticación Segura</h3>
       <p>Sistema robusto con JWT, recuperación de contraseña y protección contra ataques de fuerza bruta.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon"></div>
       <h3>Préstamos Duales</h3>
       <p>Solicita libros físicos o accede a versiones digitales instantáneamente desde cualquier dispositivo.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon"></div>
       <h3>Lista de Deseos</h3>
       <p>Guarda tus libros favoritos y ten un acceso directo a los libros que mas te gusten.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon"></div>
       <h3>Reviews & Ratings</h3>
       <p>Califica y comenta libros. Ayuda a otros usuarios a descubrir grandes lecturas.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon"></div>
       <h3>Descargas</h3>
       <p>Descarga libros para leer sin conexión cuando lo necesites.</p>
     </div>
     
     <div class="feature-card">
       <div class="feature-icon"></div>
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
   perfil
   wishlist

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
       <li style="margin: 0.5rem 0;">📧 Email: soporte@aeternum.com</li>
       <li style="margin: 0.5rem 0;">🐛 Reportar bug: <a href="https://github.com/Santixxtt/Aeternum/issues" style="color: #FF69B4;">GitHub Issues</a></li>
       <li style="margin: 0.5rem 0;"> Documentación completa en esta misma página</li>
     </ul>
   </div>

----

.. note::
   
   **Desarrollador:** Santiago Tuta  
   **Versión actual:** 1.0.0  
   **Última actualización:** Enero 2025  
   **Licencia:** MIT