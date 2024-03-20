# Predicción de Supervivencia en el Titanic

Este repositorio contiene un proyecto de predicción de supervivencia en el Titanic utilizando modelos de aprendizaje automático y una interfaz web desarrollada con Flask.

## Ejecución del Proyecto

Para ejecutar este proyecto, sigue los siguientes pasos:

1. Primero, ejecuta el archivo `api.ipynb`. Aquí se generan los modelos necesarios para realizar las predicciones.

2. A continuación, puedes ejecutar el archivo `app.py`, que contiene el código para la aplicación Flask. Sin embargo, también puedes ejecutar la aplicación desde el archivo `flask.ipynb`.

## Archivos del Proyecto

- `api.ipynb`: Este archivo contiene el código para generar los modelos de aprendizaje automático necesarios para predecir la supervivencia en el Titanic.

- `app.py`: Contiene el código de la aplicación Flask que proporciona una interfaz web para realizar predicciones de supervivencia.

- `flask.ipynb`: Este archivo proporciona una alternativa para ejecutar la aplicación Flask desde un entorno de Jupyter Notebook.

## Dependencias

Este proyecto depende de las siguientes bibliotecas de Python:

- Flask
- Pandas
- NumPy
- Pickle
- Joblib

Puedes instalar estas dependencias utilizando `pip`:

```bash
pip install flask pandas numpy joblib pickle
```

## Uso de la Aplicación

Una vez que la aplicación esté en funcionamiento, puedes acceder a ella desde tu navegador web. Proporciona la edad, sexo y clase del pasajero del Titanic y obtén una predicción sobre su supervivencia.

## Notas Adicionales.
Los modelos de predicción se cargan desde los archivos 'model1.pkl' y 'model1.joblib' que se generan en el archivo api.ipynb
