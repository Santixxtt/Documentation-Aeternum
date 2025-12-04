# Arquitectura del Sistema

Aeternum utiliza una arquitectura por capas:

- **Presentación:** React (Vite)
- **Lógica de negocio:** FastAPI
- **Persistencia:** MySQL
- **Almacenamiento temporal:** Redis

Flujo:

Usuario → React → FastAPI → MySQL → Respuesta