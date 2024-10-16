import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as parse

# Configuración de conexión a MySQL
db_config = {
    'user': 'root',
    'password': 'password',  # Cambia a tu contraseña de MySQL
    'host': '127.0.0.1',
    'database': 'crud_python',
}

# Conexión a la base de datos MySQL
def connect_db():
    return mysql.connector.connect(**db_config)

# Crear un servidor HTTP básico
class MyServer(BaseHTTPRequestHandler):
    
    # Maneja las peticiones GET
    def do_GET(self):
        if self.path == '/':
            self.render_html('index.html')
        elif self.path == '/register':
            self.render_html('register.html')
        elif self.path == '/login':
            self.render_html('login.html')
        elif self.path.startswith('/users'):
            query = parse.urlparse(self.path).query
            params = parse.parse_qs(query)
            filtro_nombre = params.get('nombre', [None])[0]
            self.list_users(filtro_nombre)
        else:
            self.send_response(404)
            self.end_headers()

    # Maneja las peticiones POST (para registro e inicio de sesión)
    def do_POST(self):
        if self.path == '/register_user':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse.parse_qs(post_data)
            usuario = data['usuario'][0]
            clave = data['clave'][0]
            nombre = data['nombre'][0]
            direccion = data['direccion'][0]
            telefono = data['telefono'][0]
            self.register_user(usuario, clave, nombre, direccion, telefono)
        elif self.path == '/login_user':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse.parse_qs(post_data)
            usuario = data['usuario'][0]
            clave = data['clave'][0]
            self.login_user(usuario, clave)

    # Función para renderizar HTML
    def render_html(self, filename):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(f"templates/{filename}", 'r') as file:
            html_content = file.read()
            self.wfile.write(bytes(html_content, "utf-8"))

    # Función para registrar un usuario en la base de datos
    def register_user(self, usuario, clave, nombre, direccion, telefono):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (usuario, clave, nombre, direccion, telefono) VALUES (%s, %s, %s, %s, %s)", 
                       (usuario, clave, nombre, direccion, telefono))
        conn.commit()
        cursor.close()
        conn.close()
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    # Función para manejar el inicio de sesión
    def login_user(self, usuario, clave):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE usuario = %s AND clave = %s", (usuario, clave))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            self.send_response(302)
            self.send_header('Location', '/users')
        else:
            self.send_response(302)
            self.send_header('Location', '/login')
        self.end_headers()

    # Función para listar todos los usuarios o filtrar por nombre
    def list_users(self, filtro_nombre=None):
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        
        if filtro_nombre:
            cursor.execute("SELECT * FROM users WHERE nombre LIKE %s", (f"%{filtro_nombre}%",))
        else:
            cursor.execute("SELECT * FROM users")
        
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        html = "<html><body><h1>Lista de usuarios</h1>"
        html += '''
        <form action="/users" method="get">
            <input type="text" name="nombre" placeholder="Filtrar por nombre">
            <input type="submit" value="Filtrar">
        </form>
        <ul>
        '''
        for user in users:
            html += f"<li>{user['nombre']} - {user['direccion']} - {user['telefono']}</li>"
        html += "</ul><a href='/'>Volver</a></body></html>"

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html, "utf-8"))

# Inicia el servidor en el puerto 8080
if __name__ == "__main__":
    webServer = HTTPServer(("localhost", 8080), MyServer)
    print("Servidor corriendo en http://localhost:8080")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Servidor detenido.")
