import streamlit as st
from retangulo import Retangulo
import pandas as pd

st.header("Cálculo com Retângulo")
b = st.text_input("Informe a base")
h = st.text_input("Informe a altura")
if st.button("Calcular"):
    r = Retangulo(float(b), float(h))
    st.write(f"Área = {r.calc_area()}")
    st.write(f"Diagonal = {r.calc_diagonal()}")
    st.write(r)

    df = pd.DataFrame(
        {
            "x": [-4, -2, 0, 2,4],
            "y": [12, 0, -4, 0, 12],
        }
    )

    st.line_chart(df, x="x", y="y")