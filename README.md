# Progra-III-2024
Clases y ejemplos de programación computacional III

## Que hacer al clonar el repo
Crear el entorno virtual

`
python -m venv venv
`

Activar el entorno virtual

`
venv\Scripts\activate
`

## Que hacer al clonar, hacer pull o sincronizar

` 
pip install -r backend/requirements.txt
`

`
cd backend
`

`
python manage.py migrate
`

`
cd ../frontend
`

`
npm install
`

`
cd ..
`
## Iniciar servidores
### Backend
Abrir una nueva terminal

`
venv\Scripts\activate
`

`
cd backend
`

`
python manage.py runserver
`
## Frontend
Abrir una nueva terminal

`
cd frontend
`

`
npm run serve
`