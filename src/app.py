import pdfkit
from jinja2 import Environment, select_autoescape, FileSystemLoader
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered", page_icon="🎓", page_title="Certificado Torcedor do Bahia")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.image("src/img/ecbahia.png", width=50)
st.title("Certificado Torcedor do Bahia")

st.write("Gere seu certificado de torcedor do Bahia")

left, right = st.columns(2)

right.write("Visualize seu certificado")

right.image("src/img/template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("src/template.html")


left.write("Preencha os dados:")
form = left.form("template_form")
name = form.text_input("Digite seu nome")
submit = form.form_submit_button("Gerar")

if submit:
    html = template.render(
        name=name
    )

    pdf = pdfkit.from_string(html, False, options = {'page-size': 'A5','orientation':'Landscape'})

    right.success("🎉 Certificado gerado com sucesso!")
    right.download_button(
        "⬇️ Baixar PDF",
        data=pdf,
        file_name="certificado.pdf",
        mime="application/octet-stream",
    )

components.html("""
<html><p><a href="https://github.com/ccallazans/certificado-torcedor" target="_blank">Made by Ciro</a></p></html>
""")