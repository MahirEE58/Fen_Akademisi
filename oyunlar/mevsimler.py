import streamlit as st
import random

def oyun():
    st.header("🌍 Mevsimler ve Gün Dönümü")
    tarihler = {"21 Haziran": "Yaz", "21 Aralık": "Kış", "21 Mart": "İlkbahar", "23 Eylül": "Sonbahar"}
    tarih = random.choice(list(tarihler.keys()))
    
    st.write(f"Kuzey Yarım Küre'de **{tarih}** tarihinde hangi mevsim başlar?")
    cevap = st.selectbox("Seçimin:", ["Yaz", "Kış", "İlkbahar", "Sonbahar"])
    
    if st.button("Kontrol Et"):
        if cevap == tarihler[tarih]:
            st.success("Tebrikler! Doğru cevap."); return True
        else: st.error("Maalesef yanlış. Konuyu tekrar gözden geçirmelisin."); return False