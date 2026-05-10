# Game Catalog API

REST API para gestionar un catálogo de videojuegos, construida con FastAPI, SQLAlchemy 2.0, Alembic y PostgreSQL.

## Tecnologías

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- Alembic
- PostgreSQL
- Pydantic v2

## Estructura del proyecto

```
app/
├── core/
│   ├── config.py       # Variables de entorno
│   └── database.py     # Conexión a la base de datos
├── games/
│   ├── models.py
│   ├── schemas.py
│   ├── repository.py
│   ├── services.py
│   └── router.py
├── genres/
│   ├── models.py
│   ├── schemas.py
│   ├── repository.py
│   ├── services.py
│   └── router.py
└── main.py
```

## Endpoints

### Géneros
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/genres` | Listar todos los géneros |
| POST | `/genres` | Crear un género |

### Juegos
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/games` | Listar todos los juegos |
| GET | `/games?genre_id={id}` | Filtrar juegos por género |
| GET | `/games/{id}` | Obtener un juego por ID |
| POST | `/games` | Crear un juego |
| PUT | `/games/{id}` | Actualizar un juego |
| DELETE | `/games/{id}` | Eliminar un juego |

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd API-VIDEOJUEGOS
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

Primero asegúrate de tener PostgreSQL instalado y corriendo. Luego crea el usuario y la base de datos:

```bash
sudo -u postgres psql
```

Dentro de la consola de PostgreSQL:

```sql
CREATE USER dev_user WITH PASSWORD 'tu_password';
CREATE DATABASE game_catalog;
GRANT ALL PRIVILEGES ON DATABASE game_catalog TO dev_user;
\q
```

### 5. Configurar variables de entorno

Copia el archivo de ejemplo y edítalo con tus datos:

```bash
cp .env.example .env
```

Edita `.env`:

```env
APP_NAME="Game Catalog API"
DEBUG=True
DATABASE_URL="postgresql://dev_user:tu_password@localhost:5432/game_catalog"
```

### 6. Correr las migraciones

```bash
alembic upgrade head
```

### 7. Levantar el servidor

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`.  
Documentación automática en `http://localhost:8000/docs`.