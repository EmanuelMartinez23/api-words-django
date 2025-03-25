#  API REST Words - Django Rest Framework

## 📌 Descripción  
Esta API permite gestionar palabras, temas e idiomas. Puedes crear, leer, actualizar y eliminar palabras y temas, 
así como obtener listas de palabras filtradas por idioma y tema.

## 🛠️ Tecnologías  
- Django REST Framework (DRF)  
- PostgreSQL  
- Token Authentication (JWT)

--- 
## 📦 Instalación de dependencias
Para instalar las dependencias del proyecto, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```
## ⚙️ Configuración de Variables de Entorno  
Este proyecto utiliza variables de entorno para configurar credenciales y opciones sensibles.  

###  Pasos para configurar:  
1. **Crea un archivo `.env` en la raíz del proyecto.**  
2. **Usa el archivo `.env.example` como referencia para definir la estructura.**  
3. **Completa los valores necesarios antes de ejecutar la aplicación.** 

--- 
## 📂 Recursos y Endpoints  

### 🌍 Idiomas  
| Método | Endpoint          | Descripción               |
|--------|-------------------|---------------------------|
| GET    | `/languages/`     | Obtener todos los idiomas |
| GET    | `/languages/{id}` | Obtener un idioma         |
| POST   | `/languages/`     | Crear un idioma           |
| DELETE | `/languages/{id}` | Borrar un idioma          |
| PUT    | `/languages/{id}` | Actualizar un idioma      |

### 📂 Temas 
| Método | Endpoint       | Descripción             |
|--------|----------------|-------------------------|
| GET    | `/themes/`     | Obtener todos los temas |
| GET    | `/themes/{id}` | Obtener un tema         |
| POST   | `/themes/`     | Crear un tema           |
| DELETE | `/themes/{íd}` | Borrar un tema          |

### 📝 Palabras  
| Método | Endpoint      | Descripción                |
|--------|---------------|----------------------------|
| GET    | `/words/`     | Obtener todas las palabras |
| GET    | `/words/{id}` | Obtener una palabra        |
| POST   | `/words/`     | Crear una palabra          |
| DELETE | `/words/{id}` | Borrar una palabra         |
| PUT    | `/words/{id}` | Actualizar una palabra     |

## 🔗 Relaciones  
Ejemplos:

`GET /themes/{theme_id}/words/` → Devuelve todas las palabras de un tema.

`GET /languages/{lang_id}/words/` → Devuelve todas las palabras de un idioma.

`GET /themes/{theme_id}/languages/{lang_id}/words/` → Devuelve todas las palabras por tema y idioma.

---
## 🔐 Autenticación  
La API usa **Token Authentication** con **JWT** (JSON Web Tokens). Para obtener un token, debes enviar una solicitud `POST` al endpoint `api/token/` con tus credenciales. Luego, puedes usar el token recibido para autenticar tus solicitudes agregándolo en el encabezado `Authorization` con el prefijo `Bearer`.


---

## 📖 Documentación de la API  

La API está completamente documentada con **Swagger**. Puedes acceder a la documentación interactiva en el siguiente endpoint:  

🔗 **Swagger UI:** [`/schema/swagger/`](http://127.0.0.1:8000/schema/swagger/)  

También puedes obtener la documentación en formato OpenAPI JSON en:  

🔗 **Esquema OpenAPI:** [`/schema/`](http://127.0.0.1:8000/schema/)  

Esto te permitirá explorar los endpoints, probar solicitudes y ver respuestas en tiempo real.
