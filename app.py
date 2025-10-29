import streamlit as st
st.title("Ejemplo para usar session.state")

if "count" not in st.session_state:
  st.session_state["count"] = 0

st.button("count")
st.write(st.session_state)
