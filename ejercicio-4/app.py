from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistroForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'
csrf = CSRFProtect(app)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        correo = form.correo.data
        contraseña = form.contraseña.data
        flash(f'Usuario {nombre} registrado correctamente.', 'success')
        return redirect(url_for('registro'))
    return render_template('registro.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
