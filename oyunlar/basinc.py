import streamlit as st

def oyun():
    st.header("⚖️ Basınç Deney Alanı")
    st.write("Yüzey alanını ve ağırlığı değiştirerek basınç değişimini gözlemle!")

    # Deney Parametreleri
    agirlik = st.slider("Cismin Ağırlığı (N)", 10, 100, 20)
    yuzey = st.radio("Yüzey Alanı (S)", [1, 2, 4], index=0, horizontal=True)

    basinc = agirlik / yuzey
    
    # Görselleştirme (Bordo kutularla temsil)
    st.write(f"### Hesaplanan Basınç: **{basinc} P**")
    
    # Basınca göre büyüyen/küçülen bir gösterge
    st.progress(min(basinc / 100, 1.0))
    
    if basinc > 50:
        st.warning("⚠️ Yüksek Basınç! Zemin zorlanıyor.")
    else:
        st.success("✅ Güvenli Basınç.")
        
    st.info("Unutma: Ağırlık artarsa basınç artar, Yüzey alanı artarsa basınç azalır (Ters orantı).")
