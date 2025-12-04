---
description: Plataforma moderna de biblioteca virtual que combina préstamos físicos y digitales
layout: landing
---

# 📚 Documentación de Aeternum

Bienvenido a la documentación completa de **Aeternum**, una plataforma moderna de biblioteca virtual que revoluciona el acceso a los libros.

---

## ⚡ Inicio Rápido

| 📖 Guías de Usuario | 🔧 Documentación Técnica | 🔌 API Reference |
|---------------------|-------------------------|------------------|
| Aprende a usar la plataforma | Arquitectura y desarrollo | Referencia completa de endpoints |
| [Ver guías →](usuario.md) | [Ver documentación →](arquitectura.md) | [Ver API →](api.md) |

---

## 🎯 ¿Qué puedes hacer con Aeternum?

### Sistema Dual de Préstamos

- **📖 Préstamos Digitales** - Acceso inmediato, lectura online desde cualquier dispositivo
- **📦 Préstamos Físicos** - Solicita online, recoge en biblioteca

### Gestión Completa

- **💝 Lista de Deseos** - Guarda libros para leer más tarde
- **⭐ Reviews y Ratings** - Califica y comenta libros
- **📊 Estadísticas** - Tracking de tu progreso de lectura

### Para Bibliotecarios

- **⚙️ Panel de Administración** - Gestión completa del sistema
- **📚 Catálogo** - Administra libros, usuarios y préstamos
- **📈 Reportes** - Métricas y estadísticas del sistema

---

## 📚 Contenido de la Documentación

### Comenzando

* [Introducción](introduccion.md) - Conoce el proyecto y sus características
* [Instalación](instalacion.md) - Configura tu entorno de desarrollo
* [Arquitectura del Sistema](arquitectura.md) - Stack tecnológico y estructura

### Autenticación

* [Sistema de Autenticación](auth_routes.md) - Login, registro y JWT
* [Recuperación de Contraseña](password_reset.md) - Sistema de recuperación

### Módulo de Usuarios

* [Módulo de Usuario](usuario.md) - Dashboard y funcionalidades
* [Gestión de Perfil](perfil.md) - Editar información personal
* [Lista de Deseos](wishlist.md) - Gestión de libros favoritos

### Gestión de Libros

* [Catálogo de Libros](catalogo.md) - Exploración y búsqueda
* [Sistema de Préstamos](prestamos.md) - Préstamos físicos y digitales
* [Reviews y Calificaciones](reviews.md) - Sistema de reseñas

### Administración

* [Panel de Administración](administracion.md) - Para bibliotecarios
* [Gestión de Préstamos](gestion_prestamos.md) - Control de préstamos

### Referencia Técnica

* [Backend (FastAPI)](backend.md) - API REST con Python
* [Frontend (React + Vite)](frontend.md) - Aplicación web
* [API Reference](api.md) - Documentación completa de endpoints
* [Seguridad](seguridad.md) - Autenticación y protección

---

## 🚀 Stack Tecnológico
```
Frontend:  React 18 + Vite + TailwindCSS
Backend:   FastAPI (Python 3.11+)
Database:  MySQL 8.0 / Railway
Cache:     Redis
Auth:      JWT + bcrypt
```

---

## 📖 Características Principales

{% hint style="info" %}
**Sistema Dual de Préstamos**

Aeternum combina lo mejor de dos mundos: préstamos físicos tradicionales y acceso digital instantáneo, ofreciendo máxima flexibilidad a los usuarios.
{% endhint %}

{% hint style="success" %}
**Seguridad Robusta**

Autenticación JWT, encriptación bcrypt, protección contra fuerza bruta y cumplimiento GDPR garantizan la seguridad de tus datos.
{% endhint %}

{% hint style="warning" %}
**En Desarrollo**

Esta documentación está en constante actualización. Si encuentras algún error o tienes sugerencias, no dudes en reportarlo.
{% endhint %}

---

## 🎓 Guías Rápidas

### Para Usuarios

1. [Crea tu cuenta](auth_routes.md#registrar-nueva-cuenta)
2. [Explora el catálogo](catalogo.md)
3. [Solicita un préstamo](prestamos.md)
4. [Califica libros](reviews.md)

### Para Desarrolladores

1. [Clona el repositorio](instalacion.md)
2. [Configura el entorno](instalacion.md#configuracion)
3. [Ejecuta el proyecto](backend.md)
4. [Prueba la API](api.md)

### Para Bibliotecarios

1. [Accede al panel admin](administracion.md)
2. [Gestiona el catálogo](administracion.md#gestion-de-libros)
3. [Administra préstamos](gestion_prestamos.md)
4. [Genera reportes](administracion.md#reportes-y-estadisticas)

---

## 📞 Soporte y Contacto

¿Necesitas ayuda?

* 📧 **Email:** soporte@aeternum.com
* 🐛 **Reportar bug:** [GitHub Issues](https://github.com/Santixxtt/Aeternum/issues)
* 📖 **Documentación:** Estás aquí 😊

---

## 🤝 Contribuir

¿Quieres mejorar Aeternum?

1. Fork el repositorio
2. Crea una branch: `git checkout -b feature/nueva-funcionalidad`
3. Commit tus cambios: `git commit -m 'Agrega nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

<div align="center">

**Desarrollado por:** Santiago Tuta  
**Versión:** 1.0.0  
**Licencia:** MIT

---

⭐ Si te gusta este proyecto, dale una estrella en [GitHub](https://github.com/Santixxtt/Aeternum)

</div>