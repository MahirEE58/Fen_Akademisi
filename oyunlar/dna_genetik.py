import streamlit as st
import random

def oyun():
    st.header("🧬 DNA Zinciri Oluşturma")
    st.info("Üst zincirdeki bazların altına uygun eşlerini (A-T, G-C) yerleştir!")

    bazlar = ["Adenin (A)", "Timin (T)", "Guanin (G)", "Sitozin (C)"]
    esler = {"A": "Timin (T)", "T": "Adenin (A)", "G": "Sitozin (C)", "C": "Guanin (G)"}
    
    if 'dna_hedef' not in st.session_state:
        st.session_state.dna_hedef = [random.choice(["A", "T", "G", "C"]) for _ in range(4)]
    
    # Görsel Tasarım
    cols = st.columns(4)
    user_choices = []

    for i in range(4):
        with cols[i]:
            # Üst Zincir (Sabit)
            target = st.session_state.dna_hedef[i]
            st.button(target, key=f"target_{i}", disabled=True)
            st.write("  |  ")
            # Alt Zincir (Kullanıcı Seçimi)
            choice = st.selectbox(f"Eşini Seç", ["?"] + bazlar, key=f"select_{i}")
            user_choices.append(choice)

    if st.button("Zinciri Kontrol Et"):
        dogru_mu = True
        for i in range(4):
            if user_choices[i] != esler[st.session_state.dna_hedef[i]]:
                dogru_mu = False
        
        if dogru_mu:
            st.balloons()
            st.success("Harika! Hidrojen bağları başarıyla kuruldu.")
            if st.button("Yeni Zincir"):
                del st.session_state.dna_hedef
                st.rerun()
            return True
        else:
            st.error("Bir hata var! Eşleşmeleri kontrol et (A-T / G-C).")
    return False
