# 📚 Documentación de la API Words

## 📌 Descripción  
API para gestionar palabras clasificadas por temas y por idioma.

## 🛠️ Tecnologías  
- Django REST Framework (DRF)  
- PostgreSQL  
- Token Authentication  

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
La API usa **Token Authentication**. Para autenticarse, enviar el token en los headers:  

