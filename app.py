from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    services = [
        {"name": "Consultoria en IT", "description": "Las soluciones tecnologicas para tu empresa"},
        {"name": "Desarrollo Web", "description": "Desarrollo de sitios web y otros"},
        {"name": "Marketing Digital", "description": "Marketing digital"}
    ]
    return render_template('index.html', services=services)

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        ##Con esto vemos lo recibido de la pagina contactos
        print(f"Mensaje recibido de {name} ({email}, Tel: {phone}): {message}")
        
        flash('Nos comunicaremos contigo, esto lleva tiempo', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
