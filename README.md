# GPT_Neo Sentiment Analysis and Text Generation App
![Imagen inicio](/images/positivo.jpeg)

## Descripción

**GPT_Neo Sentiment Analysis and Text Generation App** es una aplicación interactiva construida con Streamlit y Python, que utiliza un modelo GPT-2.0 para realizar análisis de sentimiento y generar texto a partir de comentarios proporcionados por el usuario.

## Características

- **Análisis de Sentimiento**: Evalúa el sentimiento de los comentarios de los usuarios utilizando un modelo de GPT-2.0.
- **Generación de Texto**: Genera texto basado en el sentimiento del comentario proporcionado.
- **Interfaz Intuitiva**: Fácil de usar y con una interfaz clara para la interacción del usuario.

![Imagen inicio](/images/negativo_negativo.jpeg)


## Instalación

Para ejecutar esta aplicación en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:
   ```sh
   git clone https://github.com/tu_usuario/gpt_neo_app.git
   cd gpt_neo_app
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):
   ```sh
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. **Instala las dependencias**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**:
   ```sh
   streamlit run gptneo_tool.py
   ```

## Uso

1. **Inicia la aplicación**: Ejecuta el comando `streamlit run gptneo_tool.py` en tu terminal.
2. **Interfaz de Usuario**:
    - Introduce un comentario en el cuadro de texto.
    - La aplicación realizará el análisis de sentimiento del comentario.
    - Basado en el análisis de sentimiento, la aplicación generará un texto relevante.
3. **Resultados**: La aplicación mostrará el sentimiento del comentario y el texto generado basado en ese sentimiento.

## Estructura del Proyecto

```
gpt_neo_app/
│
├── gptneo_tool.py                   # Archivo principal de la aplicación Streamlit
├── code_tool.ipynb         # Lista de dependencias necesarias
└── README.md                # Este archivo
```

![Imagen inicio](/images/negativo.jpeg)
