from flask import Flask, render_template, request, jsonify
from markupsafe import escape
from models import CVModelo

app = Flask(__name__)
modelo = CVModelo()

@app.route('/')
def index():
    datos_cv = modelo.obtener_datos()
    return render_template('index.html', datos=datos_cv)

@app.route('/api/contacto', methods=['POST'])
def contacto():
    nombre = request.form.get('nombre', '').strip()
    correo = request.form.get('correo', '').strip()
    mensaje = request.form.get('mensaje', '').strip()

    if not nombre or not correo or not mensaje:
        return jsonify({"status": "error", "mensaje": "Todos los campos son obligatorios."}), 400

    nombre_seguro = escape(nombre)
    correo_seguro = escape(correo)
    
    print(f"Mensaje recibido de: {nombre_seguro} <{correo_seguro}>")

    return jsonify({
        "status": "success", 
        "mensaje": f"¡Gracias {nombre_seguro}! He recibido tu solicitud. Te contactaré a la brevedad."
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)