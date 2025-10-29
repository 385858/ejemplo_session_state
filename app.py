import streamlit as st
st.title("Ejemplo para usar session.state")

if "count" not in st.session_state:
  st.session_state["count"] = 0

if "name" not in st.session_state:
  st.session_state['name'] = ''

if nombre == st.text_input("Escribe tu nombre"):
st.write(nombre)

if st.button("Click me"):
  st.session_state['count'] += 1

st.write(st.session_state)
