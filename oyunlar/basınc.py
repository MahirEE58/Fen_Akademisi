import streamlit as st
import random

def oyun():
    st.header("⚖️ Basınç Hesaplama Atölyesi")
    tip = random.choice(["Katı", "Sıvı"])
    if tip == "Katı":
        f, g = random.randint(10, 100), random.randint(2, 10)
        st.write(f"Ağırlık: {f}N, Yüzey Alanı: {g}S. Katı Basıncı kaçtır?")
        dogru = f / g
    else:
        h, d = random.randint(1, 10), random.randint(1, 5)
        st.write(f"Derinlik: {h}m, Sıvı Yoğunluğu: {d}d. Sıvı Basıncı kaçtır? (g=1)")
        dogru = h * d
        
    tahmin = st.number_input("Tahminin:", step=1.0)
    if st.button("Hesapla"):
        if tahmin == dogru:
            st.success("Mükemmel hesaplama!"); return True
        else: st.error(f"Hata! Doğru cevap {dogru} olmalıydı."); return False