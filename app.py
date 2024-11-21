import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Biomoléculas",  # Título que aparece en la pestaña del navegador
    page_icon="🧬",  # Ícono que aparece en la pestaña
    layout="wide"  # Diseño ancho de la página
)








# Menú lateral
with st.sidebar:
    st.title("Menú de Navegación")
    page = st.selectbox(
        "Selecciona una sección:",
        ["Inicio", "ADN", "ARN", "Carbohidratos", "Proteínas", "Grasas"]
    )

def show_home():
    # Título del dashboard
    st.title("Las Moléculas Orgánicas Clave para el Desarrollo Humano")
    st.markdown(
        "Explora las propiedades y funciones de ADN, ARN, proteínas, carbohidratos y grasas, y su importancia para el cuerpo humano.")

    # Introducción
    st.markdown("### Introducción")
    st.write("""
    Las moléculas orgánicas más importantes para el desarrollo humano son: 
    - **ADN y ARN**: Contienen las instrucciones genéticas para el desarrollo y funcionamiento celular.
    - **Proteínas**: Construyen estructuras y aceleran reacciones químicas.
    - **Carbohidratos y grasas**: Proveen energía y son bloques de construcción esenciales.
    - **Bioelementos (CHON)**: Representan el 99% de la composición química del cuerpo humano.
    """)

    # Sección 1: Visualización de proporciones CHON
    st.markdown("### Composición Elemental del Cuerpo Humano")
    elements = {'Elemento': ['Carbono', 'Hidrógeno', 'Oxígeno', 'Nitrógeno'], 'Porcentaje': [18.5, 9.5, 65, 3.2]}
    df_elements = pd.DataFrame(elements)
    fig = px.pie(df_elements, values='Porcentaje', names='Elemento', title="Composición de CHON")
    st.plotly_chart(fig)

    # Sección 2: Macronutrientes
    st.markdown("### Macronutrientes: Carbohidratos, Grasas y Proteínas")
    macros = {'Macronutriente': ['Carbohidratos', 'Grasas', 'Proteínas'], 'Porcentaje': [50, 30, 20]}
    df_macros = pd.DataFrame(macros)
    fig_macros = px.bar(df_macros, x='Macronutriente', y='Porcentaje',
                        title="Distribución Recomendada de Macronutrientes", color='Macronutriente')
    st.plotly_chart(fig_macros)

    # Sección 3: Funciones del ADN, ARN y Proteínas
    st.markdown("### Funciones Biológicas Clave")
    selected_molecule = st.selectbox("Selecciona una molécula para explorar",
                                     ['ADN', 'ARN', 'Proteínas', 'Carbohidratos', 'Grasas'])
    if selected_molecule == 'ADN':
        st.write(
            "**ADN** contiene las instrucciones genéticas para el desarrollo, funcionamiento y reproducción de todos los organismos vivos.")



    elif selected_molecule == 'ARN':
        st.write(
            "**ARN** transfiere las instrucciones genéticas del ADN a las máquinas celulares para producir proteínas.")
    elif selected_molecule == 'Proteínas':
        st.write("**Proteínas** construyen tejidos, catalizan reacciones químicas y regulan funciones corporales.")
    elif selected_molecule == 'Carbohidratos':
        st.write("**Carbohidratos** proporcionan energía rápida para el cuerpo.")
    elif selected_molecule == 'Grasas':
        st.write("**Grasas** almacenan energía y forman membranas celulares.")

    # Sección 4: Comparativa de alimentos
    st.markdown("### Comparativa Nutricional")
    food_data = {
        'Alimento': ['Pan', 'Carne', 'Aguacate'],
        'Carbohidratos (%)': [50, 0, 10],
        'Grasas (%)': [5, 20, 15],
        'Proteínas (%)': [8, 25, 2]
    }
    df_food = pd.DataFrame(food_data)
    fig_food = px.bar(df_food, x='Alimento', y=['Carbohidratos (%)', 'Grasas (%)', 'Proteínas (%)'],
                      title="Composición Nutricional de Alimentos")
    st.plotly_chart(fig_food)






def show_adn():
    st.title("Página: ADN")
    st.write("Aquí encontrarás información sobre la estructura y función del ADN.")
    # Puedes agregar más contenido aquí, como modelos 3D, gráficos o tablas.



    # Enlace al visor limpio de NGL Viewer
    iframe_url ="https://3dmol.csb.pitt.edu/viewer.html?pdb=1BNA&select=all&style=cartoon" # Cambia '1BNA' si usas otro modelo
    st.components.v1.html(f"""
        <iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>
    """, height=600)



    st.subheader("Funciones Principales")
    st.write("""
           - **Almacén de información genética**: Codifica las instrucciones para la síntesis de proteínas.
           - **Transmisión hereditaria**: Se replica para ser transmitido a las células hijas durante la división celular.
           - **Control de actividades celulares**: A través de la regulación de genes.
           """)

    # Sección 1: Composición química (Tabla)
    st.subheader("Composición Química")
    st.write("""
        El ADN está compuesto por los siguientes elementos básicos:
        """)
    # Crear tabla
    data_composicion = {
        "Componente": ["Grupo fosfato", "Azúcar desoxirribosa", "Base nitrogenada"],
        "Descripción": [
            "Une los nucleótidos en una cadena.",
            "Azúcar de cinco carbonos que forma el esqueleto del ADN.",
            "Adenina, guanina, citosina y timina."
        ]
    }
    df_composicion = pd.DataFrame(data_composicion)
    st.table(df_composicion)

    # Sección 2: Gráfica - Porcentaje de bases en el ADN humano
    st.subheader("Distribución de Bases Nitrogenadas")
    st.write("""
        En el ADN humano, las bases nitrogenadas están distribuidas de la siguiente manera:
        """)
    # Datos de bases
    bases = ["Adenina (A)", "Timina (T)", "Guanina (G)", "Citosina (C)"]
    porcentajes = [30, 30, 20, 20]

    # Crear gráfica
    fig, ax = plt.subplots()
    ax.pie(porcentajes, labels=bases, autopct='%1.1f%%', startangle=90,
           colors=["#FF9999", "#66B2FF", "#99FF99", "#FFCC99"])
    ax.axis("equal")  # Para mantener la proporción
    st.pyplot(fig)

    # Sección 3: Imagen de la estructura del ADN
    st.subheader("Estructura de la Doble Hélice")
    st.image(
        "https://images.my.labster.com/v2/NAP/4963af1e-a76c-4f7f-b2ff-90f7b8d0a349/NAP_DNAStructure.es_ES.x1024.png",
        caption="Representación química del ADN ",
        use_container_width=True
    )
    st.subheader("Datos Curiosos")
    st.write("""
               - Si desenrolláramos todo el ADN de una célula, mediría aproximadamente **2 metros de longitud**.
               - Solo alrededor del **1.5% del ADN humano** codifica proteínas; el resto tiene funciones regulatorias o no se comprende completamente.
               """)





    if st.button("Volver al inicio"):
        st.session_state.page = "main"


def show_arn():

        st.title("ARN: Modelos y Visualización Interactiva")
        st.write("""
        El ARN (ácido ribonucleico) es fundamental para la transferencia de información genética y para la síntesis de proteínas en todas las formas de vida. 
        Aquí exploramos diferentes tipos de ARN con datos relevantes y su estructura tridimensional.
        """)

        # Selector de modelo de ARN
        modelo = st.selectbox(
            "Selecciona el modelo de ARN para visualizar:",
            [
                "ARN ribosomal (rARN)",
                "ARN mensajero (mARN)",
                "ARN pequeño nuclear (snARN)"
            ]
        )

        # Información y visualización según el modelo seleccionado
        if modelo == "ARN ribosomal (rARN)":
            st.subheader("Información: ARN Ribosomal (rARN)")
            st.write("""
            - **Función**: Componente principal de los ribosomas, encargado de la síntesis de proteínas.
            - **Distribución**: Representa el 80% del ARN total en una célula.
            """)

            # Visor interactivo para rARN
            st.write("### Visualización del rARN desde RCSB PDB")
            iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=1JJ2&select=all&style=cartoon"
            st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                                  height=600)

            # Tabla de datos del rARN
            data = {"Subunidad": ["28S", "18S", "5.8S", "5S"], "Tamaño (nucleótidos)": [4718, 1869, 160, 120]}
            st.table(pd.DataFrame(data))

            # Imagen representativa del ribosoma
            st.write("### Estructura del ribosoma que contiene rARN.")
            st.image(
                "https://www.lifeder.com/wp-content/uploads/2018/06/ribosomas-funciones-lifeder.jpg",
                caption="Estructura del ribosoma que contiene rARN.",
                use_container_width=True
            )



        elif modelo == "ARN mensajero (mARN)":
            st.subheader("Información: ARN Mensajero (mARN)")
            st.write("""
            - **Función**: Transporta información genética del ADN al ribosoma para la síntesis de proteínas.
            - **Diferencia clave**: Contiene uracilo en lugar de timina.
            """)

            # Visor interactivo para mARN
            st.write("### Visualización del mARN desde RCSB PDB")
            iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=1S03&select=all&style=cartoon"
            st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                                  height=600)

            # Gráfica de vida media del mARN
            st.write("### Vida Media del mARN en Organismos")
            vida_media = {"Organismo": ["Procariotas", "Eucariotas"], "Vida Media (s)": [5, 600]}
            fig, ax = plt.subplots()
            ax.bar(vida_media["Organismo"], vida_media["Vida Media (s)"], color=["#FFA07A", "#20B2AA"])
            ax.set_ylabel("Vida Media (segundos)")
            st.pyplot(fig)

            # Imagen representativa del mARN
            st.write("### Estructura del mARN")
            st.image(
                "https://biologia.laguia2000.com/wp-content/uploads/2014/02/ARN-mensajero.gif",
                caption="Ejemplo de estructura de ARN mensajero.",
                use_container_width=True
            )






        elif modelo == "ARN pequeño nuclear (snARN)":
            st.subheader("Información: ARN Pequeño Nuclear (snARN)")
            st.write("""
            - **Función**: Participa en el empalme del ARN mensajero como parte del spliceosoma.
            - **Tipos comunes**: U1, U2, U4, U5, U6.
            """)
            # Tabla con tipos de snARN
            data = {"Tipo": ["U1", "U2", "U4", "U5", "U6"],
                    "Función": ["Reconocimiento sitio 5'", "Reconocimiento punto de ramificación", "Asociación con U6",
                                "Unión de exones", "Catálisis de empalme"]}
            st.table(pd.DataFrame(data))

            # Visor interactivo para snARN
            st.write("### Visualización del snARN desde RCSB PDB")
            iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=3HAX&select=all&style=cartoon"
            st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                                  height=600)

            # Imagen representativa del spliceosoma

            # Visor interactivo para snARN
            st.write("### Visualización del Spliceosoma desde RCSB PDB")
            iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=6ZYM&select=all&style=cartoon"
            st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                                  height=600)

        # Botón para regresar al inicio
        if st.button("Volver al inicio"):
            st.session_state.page = "main"


def show_carbohidratos():
    st.title("Carbohidratos: Estructura y Función")
    st.write("""
            Los carbohidratos son biomoléculas esenciales que proveen energía rápida al cuerpo humano. 
            Se componen de carbono, hidrógeno y oxígeno, y pueden clasificarse en monosacáridos, disacáridos y polisacáridos.
            """)

    # Información General
    st.header("Información General")
    st.write("""
            - **Función Principal**: Proporcionar energía rápida y ser una fuente importante de fibra dietética.
            - **Clasificación**:
                1. **Monosacáridos**: Glucosa, fructosa.
                2. **Disacáridos**: Sacarosa, lactosa.
                3. **Polisacáridos**: Almidón, glucógeno.
            """)

    # Modelo 3D de Carbohidratos
    st.header("Modelos 3D de Carbohidratos")
    st.write("Selecciona un carbohidrato para visualizar su estructura molecular en 3D:")

    modelo = st.selectbox(
        "Selecciona una molécula para visualizar:",
        ["Glucosa", "Sacarosa", "Almidón"]
    )

    if modelo == "Glucosa":
        st.markdown("""
                <iframe src="https://3dmol.csb.pitt.edu/viewer.html?pdb=1G6U&select=all&style=cartoon" 
                        width="700" height="500" style="border:none;"></iframe>
                """, unsafe_allow_html=True)
        st.write("""
                - **Glucosa**: Es un monosacárido que actúa como la principal fuente de energía para las células.
                - **Fórmula Molecular**: C₆H₁₂O₆.
                """)

    elif modelo == "Sacarosa":
        st.markdown("""
                <iframe src="https://3dmol.csb.pitt.edu/viewer.html?pdb=1SAC&select=all&style=cartoon" 
                        width="700" height="500" style="border:none;"></iframe>
                """, unsafe_allow_html=True)
        st.write("""
                - **Sacarosa**: Es un disacárido formado por la unión de una molécula de glucosa y una de fructosa.
                - **Fórmula Molecular**: C₁₂H₂₂O₁₁.
                """)

    elif modelo == "Almidón":
        st.markdown("""
                <iframe src="https://3dmol.csb.pitt.edu/viewer.html?pdb=1STM&select=all&style=cartoon" 
                        width="700" height="500" style="border:none;"></iframe>
                """, unsafe_allow_html=True)
        st.write("""
                - **Almidón**: Es un polisacárido compuesto por largas cadenas de glucosa. 
                Se encuentra en alimentos como el arroz y las papas.
                """)

    # Tabla de ejemplos y contenido energético
    st.header("Ejemplos de Carbohidratos en Alimentos")
    data = {
        "Alimento": ["Arroz", "Pan", "Frutas"],
        "Tipo de Carbohidrato": ["Polisacárido", "Polisacárido", "Monosacáridos y Disacáridos"],
        "Contenido Energético (kcal/100g)": [130, 265, 60]
    }
    st.table(data)

    # Gráfico de Consumo Recomendado
    st.subheader("Distribución Recomendada de Macronutrientes")
    labels = ['Carbohidratos', 'Proteínas', 'Grasas']
    sizes = [55, 25, 20]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    st.pyplot(plt)

    # Botón para regresar al inicio
    if st.button("Volver al inicio"):
        st.session_state.page = "main"


def show_proteinas():
    st.title("Proteínas: Funciones y Visualización Interactiva")
    st.write("""
        Las proteínas son macromoléculas fundamentales para el desarrollo y funcionamiento del cuerpo humano. 
        Están compuestas por aminoácidos unidos por enlaces peptídicos y cumplen una variedad de funciones estructurales, catalíticas y regulatorias.
        """)

    # Selector para tipo de proteína
    tipo_proteina = st.selectbox(
        "Selecciona el tipo de proteína para explorar:",
        ["Enzimas", "Proteínas estructurales", "Proteínas de transporte", "Proteínas de señalización"]
    )

    # Contenido dinámico por tipo de proteína
    if tipo_proteina == "Enzimas":
        st.subheader("Información: Enzimas")
        st.write("""
            - **Función**: Catalizan reacciones químicas esenciales en los organismos.
            - **Ejemplos comunes**: Amilasa, catalasa, tripsina.
            - **Importancia**: Sin enzimas, muchas reacciones biológicas serían demasiado lentas para sustentar la vida.
            """)
        # Tabla con ejemplos de enzimas
        data = {"Enzima": ["Amilasa", "Lipasa", "Pepsina"],
                "Función": ["Digestion de carbohidratos", "Digestión de grasas", "Digestión de proteínas"]}
        st.table(pd.DataFrame(data))

        # Visor interactivo para una enzima (fosfofructoquinasa)
        st.write("### Visualización de fosfofructoquinasa desde RCSB PDB")
        iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=1GZX&select=all&style=cartoon"
        st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                              height=600)

    elif tipo_proteina == "Proteínas estructurales":
        st.subheader("Información: Proteínas Estructurales")
        st.write("""
            - **Función**: Proporcionan soporte y estructura a las células y tejidos.
            - **Ejemplos comunes**: Colágeno, queratina, elastina.
            """)
        # Tabla con características de proteínas estructurales
        data = {"Proteína": ["Colágeno", "Queratina", "Elastina"],
                "Función": ["Estructura en tejidos conectivos", "Fortaleza en cabello y uñas",
                            "Elasticidad en la piel"]}
        st.table(pd.DataFrame(data))

        # Visor interactivo para una enzima (fosfofructoquinasa)
        st.write("### Visualización del Colágeno desde RCSB PDB")
        iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=1GZX&select=all&style=cartoon"
        st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                              height=600)





    elif tipo_proteina == "Proteínas de transporte":
        st.subheader("Información: Proteínas de Transporte")
        st.write("""
            - **Función**: Transportan moléculas esenciales dentro del cuerpo.
            - **Ejemplos comunes**: Hemoglobina, mioglobina.
            """)
        # Gráfico de comparación entre hemoglobina y mioglobina
        st.write("### Comparación entre Hemoglobina y Mioglobina")
        transporte_data = {"Proteína": ["Hemoglobina", "Mioglobina"], "Afinidad por el oxígeno (%)": [95, 90]}
        fig, ax = plt.subplots()
        ax.bar(transporte_data["Proteína"], transporte_data["Afinidad por el oxígeno (%)"],
               color=["#FF4500", "#1E90FF"])
        ax.set_ylabel("Afinidad por el oxígeno (%)")
        st.pyplot(fig)

        # Visor interactivo para hemoglobina
        st.write("### Visualización de la Hemoglobina  desde RCSB PDB")
        iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=1A3N&select=all&style=cartoon"
        st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                              height=600)

    elif tipo_proteina == "Proteínas de señalización":
        st.subheader("Información: Proteínas de Señalización")
        st.write("""
            - **Función**: Transmiten señales químicas entre diferentes partes del cuerpo.
            - **Ejemplos comunes**: Insulina, factores de crecimiento.
            """)
        # Tabla con ejemplos de proteínas de señalización
        data = {"Proteína": ["Insulina", "Factor de crecimiento epidérmico (EGF)"],
                "Función": ["Regulación de glucosa en sangre", "Estimulación de crecimiento celular"]}
        st.table(pd.DataFrame(data))

        # Visor interactivo para insulina
        st.write("### Visualización de la Insulina  desde RCSB PDB")
        iframe_url = "https://3dmol.csb.pitt.edu/viewer.html?pdb=2HIU&select=all&style=cartoon"
        st.components.v1.html(f"""<iframe src="{iframe_url}" width="800" height="600" frameborder="0"></iframe>""",
                              height=600)

    # Botón para regresar al inicio
    if st.button("Volver al inicio"):
        st.session_state.page = "main"


def show_grasas():
    st.title("Grasas: Tipos, Funciones y Modelos 3D")
    st.write("""
            Las grasas, también conocidas como lípidos, son biomoléculas esenciales que desempeñan múltiples funciones en el cuerpo humano, 
            incluyendo el almacenamiento de energía, la protección de órganos y la regulación de procesos metabólicos.
            """)

    # Selector para explorar tipos de grasas
    tipo_grasa = st.selectbox(
        "Selecciona un tipo de grasa para explorar:",
        ["Grasas saturadas", "Grasas insaturadas", "Grasas trans", "Modelos 3D de lípidos"]
    )

    # Contenido dinámico según el tipo de grasa
    if tipo_grasa == "Grasas saturadas":
        st.subheader("Información: Grasas Saturadas")
        st.write("""
                - **Características**: Son sólidas a temperatura ambiente y se encuentran principalmente en productos animales y algunos aceites tropicales.
                - **Fuentes**: Mantequilla, carne roja, aceite de coco.
                - **Impacto en la salud**: Su consumo excesivo puede aumentar el riesgo de enfermedades cardiovasculares.
                """)
        data = {"Fuente": ["Mantequilla", "Queso", "Carne roja"], "Contenido de grasa saturada (%)": [51, 33, 37]}
        st.table(pd.DataFrame(data))
        st.image("https://www.goredforwomen.org/-/media/AHA/H4GM/Article-Images/saturated-fat.jpg?sc_lang=es",
                 caption="Grasas saturadas",
                 use_container_width=True)

    elif tipo_grasa == "Grasas insaturadas":
        st.subheader("Información: Grasas Insaturadas")
        st.write("""
                - **Características**: Son líquidas a temperatura ambiente y se consideran grasas saludables.
                - **Fuentes**: Aceite de oliva, aguacate, pescado.
                - **Impacto en la salud**: Ayudan a reducir el colesterol malo y promueven la salud del corazón.
                """)
        data = {"Fuente": ["Aceite de oliva", "Aguacate", "Salmón"], "Contenido de grasa insaturada (%)": [73, 15, 27]}
        st.table(pd.DataFrame(data))
        st.image("https://fivestarsfitness.com/wp-content/uploads/diferencia-entre-grasas-saturadas-e-insaturadas.jpg",
                 caption="Grasas insaturadas",
                 use_container_width=True)

    elif tipo_grasa == "Grasas trans":
        st.subheader("Información: Grasas Trans")
        st.write("""
                - **Características**: Son grasas insaturadas que han sido procesadas para solidificarlas, aumentando su estabilidad en alimentos.
                - **Fuentes**: Margarina, alimentos procesados, pasteles.
                - **Impacto en la salud**: Aumentan el colesterol malo y reducen el colesterol bueno, incrementando el riesgo de enfermedades cardiovasculares.
                """)
        data = {"Producto": ["Margarina", "Galletas", "Pastel"], "Contenido de grasa trans (%)": [15, 10, 12]}
        st.table(pd.DataFrame(data))
        st.image("https://www.drazemba.com/web/wp-content/uploads/grasas-trans-1-scaled.jpg", caption="Grasas Trans",
                 use_container_width=True)


    elif tipo_grasa == "Modelos 3D de lípidos":
        st.title("Modelos 3D de Lípidos")
        st.write(

            """
                Explora las estructuras moleculares de algunos lípidos importantes en el cuerpo humano.
                """)

        modelo = st.selectbox(
            "Selecciona una molécula para visualizar:",
            ["Triglicérido", "Fosfolípido", "Colesterol"]
        )

        if modelo == "Triglicérido":
            st.markdown("""
                    <iframe src="https://3dmol.csb.pitt.edu/viewer.html?pdb=1CRN&select=all&style=cartoon" 
                            width="700" height="500" style="border:none;"></iframe>
                    """, unsafe_allow_html=True)
            st.write(

                """
                        - **Triglicérido**: Compuesto por una molécula de glicerol unida a tres ácidos grasos. 
                        Son la principal forma de almacenamiento de energía en el cuerpo.
                        """)

        elif modelo == "Fosfolípido":
            st.markdown(

                """
                        <iframe src="https://3dmol.csb.pitt.edu/viewer.html?pdb=2M3G&select=all&style=cartoon" 
                                width="700" height="500" style="border:none;"></iframe>
                        """, unsafe_allow_html=True)
            st.write("""
                    - **Fosfolípido**: Componente clave de las membranas celulares. 
                    Poseen una cabeza hidrofílica y dos colas hidrofóbicas.
                    """)

        elif modelo == "Colesterol":
            st.markdown(

                """
                        <iframe src="https://3dmol.csb.pitt.edu/viewer.html?pdb=1COH&select=all&style=cartoon" 
                                width="700" height="500" style="border:none;"></iframe>
                        """, unsafe_allow_html=True)
            st.write("""
                    - **Colesterol**: Lípido estructural importante en las membranas celulares. 
                    También es precursor de hormonas esteroides y vitamina D.
                    """)

        # Botón para regresar al menú principal
        if st.button("Volver al inicio"):
            st.session_state.page = "main"


# Renderizar la página según la selección
if page == "Inicio":
    show_home()
elif page == "ADN":
    show_adn()
elif page == "ARN":
    show_arn()
elif page == "Carbohidratos":
    show_carbohidratos()
elif page == "Proteínas":
    show_proteinas()
elif page == "Grasas":
    show_grasas()






