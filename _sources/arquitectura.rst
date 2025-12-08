Arquitectura del Sistema
========================

Aeternum utiliza una arquitectura por capas:

- **Presentación:** React (Vite)
- **Lógica de negocio:** Python (FastAPI)
- **Persistencia:** MySQL, Base de Datos en la Nube Railway
- **Almacenamiento temporal:** Redis guardado en Railway


Flujo:

Usuario → React → FastAPI → Railway → Respuesta
