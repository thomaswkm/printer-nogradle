# Procesador de Fotos Distribuido - ZeroC Ice Application

Una aplicación distribuida que convierte imágenes a color a blanco y negro usando **ZeroC Ice** como middleware de comunicación.

---

## Descripción

Esta aplicación consiste en dos componentes:

- **Servidor (Python)**: Procesa imágenes recibidas y las convierte a escala de grises usando **Pillow (PIL)**.
- **Cliente (Node.js)**: Envía imágenes al servidor y guarda el resultado procesado.

## Flujo de ejecución

1. El cliente lee una imagen local (input.jpg).

1. Envía los bytes de la imagen al servidor mediante Ice.

1. El servidor convierte la imagen a escala de grises y devuelve los bytes resultantes.

1. El cliente guarda la imagen procesada en output_bw.jpg.

---

## Prerrequisitos

### Para el Servidor

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Para el Cliente

- Node.js 14 o superior
- npm (gestor de paquetes de Node.js)

---

## Instalación y Configuración

### 1. Servidor (Python)

```bash
# Navegar al directorio del servidor
cd server

# Crear un entorno virtual de Python
python -m venv venv

# Activar el entorno virtual
# En macOS / Linux:
source venv/bin/activate

# En Windows:
venv\Scripts\activate

# Instalar dependencias de Python
pip install -r requirements.txt

# Generar el código Python a partir del archivo .ice (Slice)
slice2py ColorService.ice

# Iniciar el servidor
python server.py
```

### 2. Cliente

```bash
# Navegar al directorio del cliente
cd client

# Instalar dependencias del package.json
npm i

# Generar el código JavaScript a partir del archivo .ice (Slice)
slice2js ColorService.ice

# Ejecutar el cliente
node client.js

```
