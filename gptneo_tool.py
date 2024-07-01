#cargamos librerías
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image #para colocar el logo de la aplicación
import torch
from transformers import pipeline

device = "cpu"  # Utilizamos la CPU en lugar de CUDA

@st.cache_resource
#hacemos un generador que nos permite hacer una inferencia, device 'cpu' para utilizar la CPU
def model_generator():
    generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M", device=device)
    return generator

@st.cache_resource
#utilizaremos un traductor de ingles a español
def model_translator_en_es():
    translator = pipeline("translation", model = "Helsinki-NLP/opus-mt-en-es")
    return translator

@st.cache_resource
#y un traductor de español al ingles
def model_translator_es_en():
    translator = pipeline("translation", model = "Helsinki-NLP/opus-mt-es-en")
    return translator

@st.cache_resource
#le pasamos el decorador singleton, para que no esté cargando a cada rato el modelo
def model_sentiment():
    classifier = pipeline("sentiment-analysis", model = "distilbert-base-uncased-finetuned-sst-2-english")
    return classifier

generator = model_generator()
translator_en_es = model_translator_en_es()
translator_es_en = model_translator_es_en()
sentiment = model_sentiment()

###########################
#### LAYOUT - Sidebar
###########################

logo_gpt = Image.open("./images/Leonardo_Diffusion_Generate_a_captivating_and_professional_log_0.jpg")
with st.sidebar:
    st.image(logo_gpt)
    
#titulo de nuestra aplicación
st.title("GPT Neo - Análisis de Sentimiento")

# Input de texto traducido al español
prompt_es = st.text_area('Texto a Generar')
prompt_en = translator_es_en(prompt_es)


# Generar texto con el prompt en ingles
results = generator(prompt_en[0]['translation_text'], do_sample=True, max_length=256, temperature=1.2)
gen_text_en = results[0]['generated_text']


# Traducir el texto generado a español
gen_text_es = translator_en_es(gen_text_en)
st.write('Texto generado:', gen_text_es[0]['translation_text'])

# Aplicar Sentiment Analysis a el texto generado en ingles
sentiment_en = sentiment(gen_text_en)
st.write(sentiment_en)