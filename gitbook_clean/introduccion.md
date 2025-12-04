============================
# Introducción a Aeternum

![Imagen](.gitbook/assets/aeternum_logo.png)

|

# ¿Qué es Aeternum?

**Aeternum** es una plataforma moderna de biblioteca virtual que revoluciona la forma en que accedes y disfrutas de los libros. Combina lo mejor de dos mundos: la experiencia tradicional de los **préstamos físicos** con la inmediatez y comodidad de los **préstamos digitales**.

---

#  Características Principales

Aeternum ofrece un ecosistema completo para gestionar tu experiencia de lectura:

## 1. Sistema Dual de Préstamos

 **Préstamos Digitales**

- Acceso inmediato sin esperas
- Lectura en línea desde cualquier dispositivo
- Marcadores y progreso sincronizado
- Modo nocturno y ajustes de lectura
- Sin límite de copias digitales

 **Préstamos Físicos**

- Solicitud online, recogida en biblioteca
- Sistema de reservas inteligente
- Notificaciones de recordatorio
- Gestión completa del ciclo de préstamo
- Renovaciones automáticas

## 2. Gestión Inteligente

 **Lista de Deseos**

Guarda libros para leer más tarde y recibe notificaciones cuando estén disponibles.

 **Sistema de Reviews**

- Califica libros del 1 al 5
- Deja comentarios y reseñas
- Lee opiniones de otros usuarios
- Descubre nuevas lecturas

 **Estadísticas Personales**

- Tracking de libros leídos
- Racha de lectura continua
- Tiempo invertido en lectura
- Géneros favoritos

## 3. Experiencia de Usuario

 **Interface Moderna**

- Diseño intuitivo y responsive
- Búsqueda avanzada con filtros
- Catálogo visual atractivo
- Navegación fluida

 **Notificaciones Inteligentes**

- Recordatorios de devolución
- Alertas de disponibilidad
- Confirmaciones por correo
- Updates de estado en tiempo real

 **Seguridad Robusta**

- Autenticación JWT
- Encriptación de contraseñas (bcrypt)
- Protección contra fuerza bruta
- Cumplimiento GDPR

---

#  Arquitectura del Sistema

Aeternum está construido con tecnologías modernas y escalables:

## Stack Tecnológico

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :class: tech-stack-table

   * - Capa
     - Tecnología
   * - **Frontend**
     - React 18 + Vite + TailwindCSS + React Router
   * - **Backend**
     - FastAPI (Python 3.11+) + Uvicorn
   * - **Base de Datos**
     - MySQL 8.0 / Railway Cloud Database
   * - **Cache & Sessions**
     - Redis (bloqueos, rate limiting, sesiones)
   * - **Autenticación**
     - JWT (JSON Web Tokens) + bcrypt
   * - **Email Service**
     - SMTP con templates HTML personalizados
   * - **API Externa**
     - Open Library API (metadata de libros)
   * - **Storage**
     - AWS S3 / Cloudinary (portadas y PDFs)

## Diagrama de Arquitectura

```text

                     USUARIOS                         

                    
                    

              FRONTEND (React + Vite)                 
  • React Router  • TailwindCSS  • Axios              

                     HTTP/REST API
                    

            BACKEND (FastAPI + Redis)                 
  • Autenticación JWT                                 
  • Lógica de negocio                                 
  • Rate Limiting                                     
  • Email Service                                     

                                           
                                           
              
  MySQL              Redis         Open Library 
 Database            Cache             API      
              
```

---

#  Roles de Usuario

Aeternum maneja dos tipos de usuarios con diferentes permisos:

## Usuario Regular

## Bibliotecario

---

#  Flujos Principales

## 1. Flujo de Registro y Login

```text
Usuario nuevo
   
   → Registrarse (/auth/register)
         • Proporciona datos personales
         • Acepta política de privacidad
         • Crea contraseña segura
         ↓
   → Cuenta creada
         ↓
   → Iniciar sesión (/auth/login)
          • Ingresa correo y contraseña
          • Recibe token JWT
          ↓
      Dashboard personalizado
```

## 2. Flujo de Préstamo Digital

```text
Usuario autenticado
   
   → Explora catálogo
         ↓
   → Selecciona libro
         ↓
   → Clic en "Leer ahora"
         • Verifica disponibilidad
         • Registra préstamo
         ↓
   → Redirige a lector online
          • Lee el libro
          • Guarda progreso automático
          • 12 días de acceso
```

## 3. Flujo de Préstamo Físico

```text
Usuario autenticado
   
   → Selecciona libro
         ↓
   → Clic en "Préstamo físico"
         ↓
   → Selecciona fecha de recogida
         • Mínimo: Mañana
         • Máximo: 7 días adelante
         ↓
   → Confirma solicitud
         • Estado: "Pendiente"
         • Correo de confirmación
         ↓
   → Recoge libro en biblioteca
         • Bibliotecario cambia a "Activo"
         • 12 días para leer
         ↓
   → Devuelve libro
          • Bibliotecario marca como "Devuelto"
          • Préstamo completado
```

---

#  Casos de Uso

## Para Estudiantes

- Acceso a libros académicos 24/7
- Descargas para estudiar offline
- Referencias bibliográficas completas
- Historial organizado de lecturas

## Para Lectores Casuales

- Descubre nuevos libros mediante reviews
- Lista de deseos para planificar lecturas
- Recordatorios para no perder fechas
- Estadísticas de progreso motivacionales

## Para Bibliotecas

- Digitalización de catálogo
- Gestión automatizada de préstamos
- Reducción de trabajo manual
- Reportes detallados de uso
- Mejor experiencia para usuarios

---

#  Beneficios Clave

---

#  Roadmap Futuro

Funcionalidades planeadas para próximas versiones:

**v2.0 - En Desarrollo**

-  Audiolibros
-  App móvil nativa (iOS/Android)
- 🤖 Recomendaciones con IA
-  Chat entre usuarios (club de lectura)
-  Sistema de logros y gamificación

**v3.0 - Planificado**

-  Soporte multiidioma
-  Temas personalizables
-  Integración con más APIs de libros
-  Compartir en redes sociales
-  Modo sin conexión (PWA)

---

# 🤝 Contribuir

¿Quieres mejorar Aeternum?

1. Fork el repositorio en GitHub
2. Crea una branch para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Commitea tus cambios: `git commit -m 'Agrega nueva funcionalidad'`
4. Push a la branch: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

Consulta la guía de contribución en el repositorio para más detalles.

---

#  Soporte

¿Necesitas ayuda?

-  Email: soporte@aeternum.com
-  Discord: `Servidor de Aeternum `_
-  Reportar bug: `GitHub Issues `_
-  Documentación: Estás aquí 

---

.. note::
   
   **Desarrollador:** Santiago Tuta  
   **Versión actual:** 1.0.0  
   **Última actualización:** Enero 2025  
   **Licencia:** MIT