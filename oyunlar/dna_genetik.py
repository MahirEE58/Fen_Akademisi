import streamlit as st
import random

def oyun():
    st.header("🧬 DNA Zinciri Tamamlama")
    bazlar = ["A", "T", "G", "C"]
    hedef = [random.choice(bazlar) for _ in range(4)]
    esler = {"A": "T", "T": "A", "G": "C", "C": "G"}
    
    st.write(f"Verilen bazların karşısına gelecek doğru eşleri yaz: **{' - '.join(hedef)}**")
    user = st.text_input("Eşleri araya boşluk bırakarak yaz (Örn: T A C G):").upper().split()
    
    if st.button("Zinciri Onayla"):
        if user == [esler[b] for b in hedef]:
            st.success("Harika! Hidrojen bağları başarıyla kuruldu."); return True
        else: st.error("Hatalı eşleşme yaptın!"); return False