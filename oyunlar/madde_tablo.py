import streamlit as st
import random

def tablo_oyunu():
    st.header("📍 Periyodik Tablo Yerleştirmece")
    st.write("Rastgele gelen elementi tabloda doğru konuma (Grup ve Periyot) yerleştir!")

    # Element veritabanı: (Periyot, Grup, Sembol)
    elementler = [
        (1, 1, "H"), (1, 18, "He"),
        (2, 1, "Li"), (2, 2, "Be"), (2, 13, "B"), (2, 14, "C"), (2, 15, "N"), (2, 16, "O"), (2, 17, "F"), (2, 18, "Ne"),
        (3, 1, "Na"), (3, 2, "Mg"), (3, 13, "Al"), (3, 14, "Si"), (3, 15, "P"), (3, 16, "S"), (3, 17, "Cl"), (3, 18, "Ar")
    ]

    if 'hedef_element' not in st.session_state:
        st.session_state.hedef_element = random.choice(elementler)

    p_hedef, g_hedef, s_hedef = st.session_state.hedef_element

    st.info(f"Yerleştirilecek Element: **{s_hedef}**")

    # Tablo Görünümü Oluşturma
    periyotlar = [1, 2, 3]
    gruplar = [1, 2, 13, 14, 15, 16, 17, 18]

    # Tablo başlıkları (Gruplar)
    cols = st.columns(len(gruplar))
    for i, g in enumerate(gruplar):
        cols[i].write(f"**{g}A**")

    # Satırları oluşturma
    for p in periyotlar:
        cols = st.columns(len(gruplar))
        for i, g in enumerate(gruplar):
            # Elementin olup olmadığını kontrol et
            mevcut_mu = any(e for e in elementler if e[0] == p and e[1] == g)
            
            if mevcut_mu:
                if cols[i].button("Seç", key=f"btn_{p}_{g}"):
                    if p == p_hedef and g == g_hedef:
                        st.balloons()
                        st.success(f"Harika! {s_hedef} elementi {p}. Periyot {g}A grubundadır.")
                        st.session_state.hedef_element = random.choice(elementler)
                        st.rerun()
                    else:
                        st.error("Yanlış yer! Tekrar dene.")
            else:
                cols[i].write("---") # Boş kutucuklar için

    if st.button("Başka Element Getir"):
        st.session_state.hedef_element = random.choice(elementler)
        st.rerun()

    return False