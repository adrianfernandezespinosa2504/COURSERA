# 🧠 Microsoft AI & ML Engineering - Coursera

## 1. Descripción del proyecto

Este repositorio recoge los ejercicios, prácticas y ejemplos desarrollados durante el curso **Microsoft AI & ML Engineering**, impartido a través de Coursera. https://www.coursera.org/learn/foundations-of-ai-and-machine-learning/home/module/1

El objetivo del trabajo es adquirir conocimientos prácticos sobre el ciclo de desarrollo de soluciones de Inteligencia Artificial y Machine Learning, desde el tratamiento y preparación de los datos hasta el entrenamiento, evaluación y despliegue de modelos.

Se incluyen implementaciones con diferentes bibliotecas y herramientas del ecosistema Python, abordando tanto técnicas tradicionales de Machine Learning como modelos de Deep Learning y procesamiento del lenguaje natural.

## 2. Objetivos

Los principales objetivos de las prácticas son:

- Familiarizarse con las herramientas y bibliotecas de Python para Inteligencia Artificial.
- Aprender a obtener, explorar y analizar conjuntos de datos.
- Aplicar técnicas de limpieza y preprocesamiento de datos.
- Entrenar y evaluar modelos de Machine Learning.
- Desarrollar redes neuronales mediante TensorFlow y Keras.
- Experimentar con modelos de lenguaje utilizando Hugging Face Transformers.
- Implementar servicios de inferencia mediante API REST.
- Aprender a empaquetar y desplegar aplicaciones mediante contenedores Docker.

## 3. Tecnologías utilizadas

| Tecnología                | Aplicación                                         |
| ------------------------- | -------------------------------------------------- |
| Python                    | Lenguaje de programación principal.                |
| NumPy                     | Operaciones y procesamiento de datos numéricos.    |
| Pandas                    | Manipulación y análisis de conjuntos de datos.     |
| Matplotlib                | Visualización de datos y resultados.               |
| Scikit-learn              | Preprocesamiento y algoritmos de Machine Learning. |
| TensorFlow / Keras        | Construcción y entrenamiento de redes neuronales.  |
| Hugging Face Transformers | Utilización de modelos de lenguaje preentrenados.  |
| Docker                    | Contenerización y despliegue de aplicaciones.      |
| BeautifulSoup             | Extracción de información de páginas web.          |

## 4. Contenido del repositorio

Las prácticas se organizan conceptualmente en diferentes áreas:

### 4.1. Obtención y extracción de datos

Ejercicios relacionados con la recopilación de información de fuentes externas mediante técnicas de *web scraping*.

- Extracción de información de páginas web mediante `requests` y `BeautifulSoup`.
- Obtención de tablas y conversión de la información a estructuras de datos mediante Pandas.
- Localización y descarga de documentos desde páginas web.

### 4.2. Limpieza y preprocesamiento de datos

Aplicación de técnicas para preparar los conjuntos de datos antes de utilizarlos en modelos de Machine Learning.

- Identificación y tratamiento de valores ausentes.
- Detección y eliminación de valores atípicos (*outliers*) mediante puntuaciones Z.
- Normalización y estandarización de variables numéricas.
- Codificación de variables categóricas mediante *One-Hot Encoding*.
- Exportación de los datos procesados a ficheros CSV.

### 4.3. Machine Learning

Implementación de algoritmos de aprendizaje automático utilizando Scikit-learn.

- División de conjuntos de datos en entrenamiento y prueba.
- Entrenamiento de modelos de clasificación.
- Regresión logística.
- Utilización del conjunto de datos Iris.
- Serialización de modelos entrenados mediante Joblib.

### 4.4. Deep Learning

Desarrollo de redes neuronales utilizando TensorFlow y Keras.

Se incluyen ejercicios sobre:

- Clasificación de imágenes utilizando el conjunto de datos CIFAR-10.
- Construcción de redes neuronales convolucionales (CNN).
- Clasificación binaria para la predicción de abandono de clientes (*Customer Churn*).
- Evaluación de modelos mediante métricas de precisión.
- Conversión y optimización de modelos para su despliegue mediante TensorFlow Lite.

### 4.5. Modelos de lenguaje y Transformers

Primeros experimentos con modelos de lenguaje preentrenados mediante la biblioteca Hugging Face Transformers.

Se incluyen ejemplos de:

- Generación de texto.
- Resumen automático de textos.
- Respuesta a preguntas.
- Implementación básica de un asistente conversacional.

Se utiliza el modelo `google/flan-t5-small`.

### 4.6. Despliegue de modelos

Prácticas orientadas a poner en funcionamiento modelos previamente entrenados y permitir su utilización desde otras aplicaciones.

- Desarrollo de servicios HTTP mediante Flask.
- Implementación de endpoints REST para realizar predicciones.
- Carga de modelos previamente serializados.
- Intercambio de información mediante peticiones JSON.
- Creación de imágenes Docker para contenerizar los servicios.
- Exposición de servicios de inferencia mediante contenedores.

## 5. Organización del repositorio

La estructura del proyecto se organiza de la siguiente manera:

```text
COURSERA/
│
├── Dockerfile
├── dockerfile_ejemplo.txt
│
├── PRUEBA WIKIPEDIA.py
├── Scraping urls.py
│
├── cleaning_preprocessing.py
├── funciones.py
│
├── churn_ejercicio.py
├── implementing_model_ejercicio.py
├── dploying_model_ejercicio.py
├── transformers_ejemplo.py
│
├── serve_model.py
├── container_test_ejemplo.py
├── setup.py
├── requirements.txt
│
├── customer_churn.csv
├── dataset_practica.csv
├── cleaned_preprocessed_data.csv
├── preprocessed_dummy_data_ejemplo_2.csv
├── scraped_data.csv
│
├── churn_model.h5
├── iris_model.pkl
│
└── curl
```

## 6. Instalación y configuración

### 6.1. Requisitos previos

Para ejecutar las prácticas se necesita:

- Python 3.
- pip (gestor de paquetes de Python).
- Docker (para los ejercicios de contenerización).

Algunas prácticas utilizan bibliotecas adicionales que pueden requerir instalaciones específicas.

### 6.2. Instalación de dependencias

Desde el directorio raíz del repositorio, se pueden instalar las dependencias recogidas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

Las prácticas que utilizan otras bibliotecas, como TensorFlow, Pandas, NumPy, Matplotlib o Transformers, pueden necesitar dependencias adicionales.

## 7. Ejecución de ejemplos

Los ejercicios se ejecutan individualmente mediante Python.

Por ejemplo, para ejecutar el ejercicio de preprocesamiento:

```bash
python cleaning_preprocessing.py
```

Para ejecutar el ejemplo de Transformers:

```bash
python transformers_ejemplo.py
```

Los ficheros que utilizan conjuntos de datos o modelos previamente generados necesitan disponer de dichos recursos en las rutas esperadas por cada script.

## 8. Despliegue mediante Flask y Docker

Una de las prácticas consiste en desplegar un modelo de clasificación utilizando Flask y Docker.

### 8.1. Entrenamiento del modelo

El ejercicio `dploying_model_ejercicio.py` utiliza el conjunto de datos Iris y entrena un modelo de regresión logística mediante Scikit-learn.

El modelo entrenado se almacena mediante Joblib en el fichero `iris_model.pkl`.

```bash
python dploying_model_ejercicio.py
```

### 8.2. Servicio de inferencia

El fichero `serve_model.py` implementa una API REST con Flask que permite realizar predicciones utilizando el modelo previamente entrenado.

El servicio expone un endpoint `POST /predict` que recibe los datos de entrada en formato JSON.

### 8.3. Contenerización

El fichero `Dockerfile` define la imagen necesaria para ejecutar el servicio Flask en un contenedor Docker.

Para construir la imagen:

```bash
docker build -t modelo-iris .
```

Para ejecutar el contenedor:

```bash
docker run -p 80:80 modelo-iris
```

Una vez iniciado el servicio, se pueden enviar peticiones HTTP al endpoint de predicción.

Ejemplo de petición:

```bash
curl -X POST http://127.0.0.1:80/predict \
-H "Content-Type: application/json" \
-d "{\"input\": [5.1, 3.5, 1.4, 0.2]}"
```

## 9. Documentación adicional

El código fuente de cada práctica contiene los ejemplos y procedimientos desarrollados durante el curso.

Los conjuntos de datos y modelos almacenados en el repositorio permiten complementar los ejercicios y realizar pruebas con los ejemplos implementados.
