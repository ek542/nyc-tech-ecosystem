import streamlit as st

def shared_state_counter():
    increment = st.button('Increment count (shared state across pages)')
    if increment:
        st.session_state.count += 1

    st.write('Count = ', st.session_state.count)
