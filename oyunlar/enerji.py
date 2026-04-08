import streamlit as st
import random

def oyun():
    st.header("☀️ Besin Zinciri Dizilimi")
    
    zincir_data = ["Ot", "Çekirge", "Kurbağa", "Yılan", "Kartal"]
    
    if 'kullanici_zinciri' not in st.session_state:
        st.session_state.kullanici_zinciri = []
        st.session_state.secenekler = random.sample(zincir_data, len(zincir_data))

    st.subheader("Senin Zincirin:")
    st.write(" ➔ ".join(st.session_state.kullanici_zinciri) if st.session_state.kullanici_zinciri else "Boş (Canlıları aşağıdan seç)")

    # Seçenek butonları
    cols = st.columns(len(st.session_state.secenekler))
    for i, canli in enumerate(st.session_state.secenekler):
        if cols[i].button(canli, key=f"btn_{canli}"):
            st.session_state.kullanici_zinciri.append(canli)
            st.session_state.secenekler.remove(canli)
            st.rerun()

    col_reset, col_check = st.columns(2)
    
    if col_reset.button("🔄 Sıfırla"):
        del st.session_state.kullanici_zinciri
        del st.session_state.secenekler
        st.rerun()

    if col_check.button("✅ Kontrol Et"):
        if st.session_state.kullanici_zinciri == zincir_data:
            st.success("Mükemmel! Üreticiden tüketiciye doğru enerji akışını sağladın.")
            return True
        else:
            st.error("Sıralama yanlış! Güneş enerjisini ilk kim kullanır?")
    return False
