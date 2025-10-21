"""
GPT_2_PESTEL
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# from openai import OpenAI
# from docx import Document
# import os, sys
# from docxtpl import DocxTemplate as DocTemp
# from docxtpl import InlineImage
# from docx.shared import Cm, Inches, Mm, Emu

# # Configuración de la clave de la API de OpenAI
# # falta añadir el panorama internacional
# client = OpenAI(api_key="YOUR_API_KEY_HERE")

# # Función para interactuar con ChatGPT y obtener el análisis del documento
# def analizar_pestel_politico(empresa, rubro, pais):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
#         messages=[
#             {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
#             Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
#             Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
#             adecuado para un contexto académico o empresarial de alto nivel."""},
#             {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis politico de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
#             ],
#         #max_tokens=30048
#     )
#     return response.choices[0].message.content

# def analizar_pestel_economico(empresa, rubro, pais):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
#         messages=[
#             {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
#             Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
#             Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
#             adecuado para un contexto académico o empresarial de alto nivel."""},
#             {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis economico de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
#            ],
#         #max_tokens=30048
#     )
#     return response.choices[0].message.content


# # Función para interactuar con ChatGPT y obtener el análisis del documento
# def analizar_pestel_social(empresa, rubro, pais):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
#         messages=[
#             {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
#             Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
#             Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
#             adecuado para un contexto académico o empresarial de alto nivel."""},
#             {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis social de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
#              ],
#         #max_tokens=30048
#     )
#     return response.choices[0].message.content

# def analizar_pestel_tecnologico(empresa, rubro, pais):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
#         messages=[
#             {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
#             Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
#             Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
#             adecuado para un contexto académico o empresarial de alto nivel."""},
#             {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis tecnologico de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
#              ],
#         #max_tokens=30048
#     )
#     return response.choices[0].message.content



# # Función para interactuar con ChatGPT y obtener el análisis del documento
# def analizar_pestel_ecologico(empresa, rubro, pais):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
#         messages=[
#             {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
#             Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
#             Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
#             adecuado para un contexto académico o empresarial de alto nivel."""},
#             {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis ecologico PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
#             ],
#         #max_tokens=30048
#     )
#     return response.choices[0].message.content

# def analizar_pestel_legal(empresa, rubro, pais):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
#         messages=[
#             {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
#             Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
#             Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
#             adecuado para un contexto académico o empresarial de alto nivel."""},
#             {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis legal de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
#             ],
#         #max_tokens=30048
#     )
#     return response.choices[0].message.content


# def PESTEL(empresa,rubro,pais):

#     texto_politico = analizar_pestel_politico(empresa, rubro, pais)
#     texto_economico = analizar_pestel_economico(empresa, rubro, pais)
#     texto_social = analizar_pestel_social(empresa, rubro, pais)
#     texto_tecnologico = analizar_pestel_tecnologico(empresa, rubro, pais)
#     texto_ecologico = analizar_pestel_ecologico(empresa, rubro, pais)
#     texto_legal = analizar_pestel_legal(empresa, rubro, pais)

#     return texto_politico,texto_economico, texto_social, texto_tecnologico, texto_ecologico, texto_legal



# empresa = "EBIN"
# rubro = "Adminitracion de edficios"
# pais= "Bolivia"
# path_in = r"C:\Users\HP\Desktop\PLANES DE NEGOCIOS\PESTEL_temaplate.docx"
# path_out = r"C:\Users\HP\Desktop\PLANES DE NEGOCIOS\PLANES_DE_NEGOCIO_PROPUESTAS\{}.docx".format(rubro)


# texto_politico,texto_economico, texto_social, texto_tecnologico, texto_ecologico, texto_legal = PESTEL(empresa, rubro, pais)


# doc = DocTemp(path_in)

# context = {
#         "Factores_políticos": texto_politico,
#         "Factores_economicos": texto_economico,
#         "Factores_sociales": texto_social,
#         "Factores_tecnologicos": texto_tecnologico,
#         "Factores_ambientales": texto_ecologico,
#         "Factores_legales":texto_legal,
#         }
# doc.render(context)
# doc.save(path_out)








# In[2]:


# texto_legal


# In[3]:


from openai import OpenAI
from docx import Document
import os, sys
from docxtpl import DocxTemplate as DocTemp
from docxtpl import InlineImage
from docx.shared import Cm, Inches, Mm, Emu

# Configuración de la clave de la API de OpenAI
# falta añadir el panorama internacional
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Función para interactuar con ChatGPT y obtener el análisis del documento
def analizar_pestel_politico(empresa, rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
            Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
            Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
            adecuado para un contexto académico o empresarial de alto nivel."""},
            {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis politico de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def analizar_pestel_economico(empresa, rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
            Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
            Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
            adecuado para un contexto académico o empresarial de alto nivel."""},
            {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis economico de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
           ],
        #max_tokens=30048
    )
    return response.choices[0].message.content


# Función para interactuar con ChatGPT y obtener el análisis del documento
def analizar_pestel_social(empresa, rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
            Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
            Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
            adecuado para un contexto académico o empresarial de alto nivel."""},
            {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis social de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
             ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def analizar_pestel_tecnologico(empresa, rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
            Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
            Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
            adecuado para un contexto académico o empresarial de alto nivel."""},
            {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis tecnologico de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
             ],
        #max_tokens=30048
    )
    return response.choices[0].message.content



# Función para interactuar con ChatGPT y obtener el análisis del documento
def analizar_pestel_ecologico(empresa, rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
            Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
            Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
            adecuado para un contexto académico o empresarial de alto nivel."""},
            {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis ecologico PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def analizar_pestel_legal(empresa, rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": f"""Eres un experto en estrategia empresarial, especializado en el análisis PESTEL. Tu tarea es asistir en la redacción de informes de análisis PESTEL con un enfoque académico y profesional.,
            Debes proporcionar insights detallados sobre factores políticos, económicos, sociales, tecnológicos, ecológicos y legales que afectan a las empresas. ,
            Tu objetivo es ayudar a los usuarios a entender cómo estos factores pueden influir en las estrategias empresariales, utilizando un lenguaje claro, técnico y riguroso,
            adecuado para un contexto académico o empresarial de alto nivel."""},
            {"role": "user", "content": "Hola, ¿podrías ayudarme con el análisis legal de PESTEL de la empresa {} del rubro de {} en el pais {}".format(empresa,rubro,pais)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content


def PESTEL(empresa, rubro, pais,path_in, path_out):

    texto_politico = analizar_pestel_politico(empresa, rubro, pais)
    texto_economico = analizar_pestel_economico(empresa, rubro, pais)
    texto_social = analizar_pestel_social(empresa, rubro, pais)
    texto_tecnologico = analizar_pestel_tecnologico(empresa, rubro, pais)
    texto_ecologico = analizar_pestel_ecologico(empresa, rubro, pais)
    texto_legal = analizar_pestel_legal(empresa, rubro, pais)

    doc = DocTemp(path_in)

    context = {
            "Factores_políticos": texto_politico,
            "Factores_economicos": texto_economico,
            "Factores_sociales": texto_social,
            "Factores_tecnologicos": texto_tecnologico,
            "Factores_ambientales": texto_ecologico,
            "Factores_legales":texto_legal,
            }
    doc.render(context)
    doc.save(path_out)








empresa = "EBIN"
rubro = "Adminitracion de edficios"
pais= "Bolivia"
path_in = r"C:\Users\HP\Desktop\PLANES DE NEGOCIOS\PESTEL\PESTEL_temaplate.docx"
path_out = r"C:\Users\HP\Desktop\PLANES DE NEGOCIOS\PESTEL\PLANES_DE_NEGOCIO_PROPUESTAS\{}.docx".format(rubro)


PESTEL(empresa, rubro, pais,path_in, path_out )








# In[ ]:






if __name__ == "__main__":
    pass
