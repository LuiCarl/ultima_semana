# Importamos las librerías necesarias
import pandas as pd
import numpy as np
import pickle
import joblib
from flask import Flask, request

# Cargamos el modelo
modelp = pickle.load(open('model1.pkl', 'rb'))  # rb = read binary
modelj = joblib.load('model1.joblib')

def prediccion(pasajero):
    # Creamos un array de 0 con la cantidad de columnas del dataset
    nuevo = np.zeros(6)

    # El primer valor del array es la edad
    nuevo[0] = pasajero['edad']
    # El segundo valor del array es el sexo_m y el tercero el sexo_f
    if pasajero['sexo'] == 0:
        nuevo[1] = 1
    else:
        nuevo[2] = 1
    # El cuarto valor del array es la clase_1, el quinto la clase_2 y el sexto la clase_3
    if pasajero['clase'] == 1:
        nuevo[3] = 1
    elif pasajero['clase'] == 2:
        nuevo[4] = 1
    else:
        nuevo[5] = 1

    # Creamos un dataframe con el array
    nuevo = pd.DataFrame(nuevo.reshape(-1, len(nuevo)))

    # Hacemos la predicción
    respuesta = modelj.predict(nuevo)

    if respuesta[0] == 0:
        mensaje = 'No sobrevive'
    else:
        mensaje = 'Sobrevive'

    return mensaje

# Creamos la aplicación
app = Flask(__name__)

# Creamos la ruta de la página principal
@app.route('/', methods = ['GET', 'POST'])
def api_prueba():
    if request.method == 'POST':
        edad = request.form['edad']
        sexo = request.form['sexo']
        clase = request.form['clase']
        pasajero = {
            'edad': int(edad),  # Convertimos la edad a float
            'sexo': int(sexo),    # Convertimos el sexo a int
            'clase': int(clase)   # Convertimos la clase a int
        }
        
        respuesta = prediccion(pasajero)

        # Devolvemos el resultado de la predicción como mensaje
        return f"""
            <h1>Predicción de supervivencia en el Titanic</h1>
            <h2>Resultado de la predicción: {respuesta}</h2>
            <form method="post">
                <label for="edad">Edad:</label>
                <input type="text" id="edad" name="edad"><br><br>
                <label for="sexo">Sexo:</label>
                <input type="text" id="sexo" name="sexo"><br><br>
                <label for="clase">Clase:</label>
                <input type="text" id="clase" name="clase"><br><br>
                <input type="submit" value="Predecir">
            </form>
        """

    return '''
        <h1>Predicción de supervivencia en el Titanic</h1>
        <form method="post">
            <label for="edad">Edad:</label>
            <input type="text" id="edad" name="edad"><br><br>
            <label for="sexo">Sexo:</label>
            <input type="text" id="sexo" name="sexo"><br><br>
            <label for="clase">Clase:</label>
            <input type="text" id="clase" name="clase"><br><br>
            <input type="submit" value="Predecir">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
