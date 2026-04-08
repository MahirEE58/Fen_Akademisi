import streamlit as st
import random

def oyun():
    st.header("🧪 Periyodik Sistem ve Madde Bilmecesi")
    
    # Genişletilmiş Soru Havuzu
    sorular = [
        # Periyodik Tablo
        {"soru": "Atom numarası 1 olan ametal nedir?", "cevap": "H"},
        {"soru": "7A grubunun özel adı nedir?", "cevap": "HALOJENLER"},
        {"soru": "8A grubunun özel adı nedir?", "cevap": "SOYGAZLAR"},
        {"soru": "Periyodik tablodaki yatay sıralara ne denir?", "cevap": "PERİYOT"},
        {"soru": "Periyodik tablodaki dikey sütunlara ne denir?", "cevap": "GRUP"},
        {"soru": "1A grubunun özel adı nedir?", "cevap": "ALKALİ METALLER"},
        
        # Asitler ve Bazlar
        {"soru": "Sulu çözeltilerinde H+ iyonu veren madde türü?", "cevap": "ASİT"},
        {"soru": "Sulu çözeltilerinde OH- iyonu veren madde türü?", "cevap": "BAZ"},
        {"soru": "Turnusol kağıdını maviye çeviren madde türü?", "cevap": "BAZ"},
        {"soru": "Turnusol kağıdını kırmızıya çeviren madde türü?", "cevap": "ASİT"},
        {"soru": "pH değeri 7'den küçük olan maddelere ne denir?", "cevap": "ASİT"},
        {"soru": "pH değeri 7'den büyük olan maddelere ne denir?", "cevap": "BAZ"},
        {"soru": "Asitler ve bazların tepkimeye girerek tuz ve su oluşturmasına ne denir?", "cevap": "NÖTRALLEŞME"},
        
        # Fiziksel ve Kimyasal Değişimler
        {"soru": "Sütten yoğurt yapılması nasıl bir değişimdir?", "cevap": "KİMYASAL"},
        {"soru": "Demirin paslanması nasıl bir değişimdir?", "cevap": "KİMYASAL"},
        {"soru": "Buzun erimesi nasıl bir değişimdir?", "cevap": "FİZİKSEL"},
        {"soru": "Kağıdın yanması nasıl bir değişimdir?", "cevap": "KİMYASAL"},
        {"soru": "Gökkuşağı oluşumu nasıl bir değişimdir?", "cevap": "FİZİKSEL"},
        
        # Maddenin Isı ile Etkileşimi
        {"soru": "Bir gram maddenin sıcaklığını 1 derece artırmak için gereken ısı?", "cevap": "ÖZ ISI"},
        {"soru": "Sıvı haldeki bir maddenin ısı alarak gaz haline geçmesine ne denir?", "cevap": "BUHARLAŞMA"},
        {"soru": "Katı bir maddenin ısı alarak doğrudan gaz haline geçmesine ne denir?", "cevap": "SÜBLİMLEŞME"}
    ]

    # Rastgele bir soru seçelim
    if 'aktif_soru_madde' not in st.session_state:
        st.session_state.aktif_soru_madde = random.choice(sorular)

    s = st.session_state.aktif_soru_madde
    
    st.write("---")
    st.subheader("Soru:")
    st.write(s["soru"])
    
    cevap = st.text_input("Cevabını buraya yaz (Büyük/küçük harf duyarlı değil):").upper().strip()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Kontrol Et"):
            if cevap == s["cevap"]:
                st.success(f"Tebrikler! Doğru cevap: {s['cevap']}")
                # Soruyu bildiği için yeni bir soru hazırlayalım (bir sonraki render için)
                st.session_state.aktif_soru_madde = random.choice(sorular)
                return True
            else:
                st.error("Hatalı cevap, tekrar dene veya ipucu düşün!")
                return False
                
    with col2:
        if st.button("Yeni Soru Getir"):
            st.session_state.aktif_soru_madde = random.choice(sorular)
            st.rerun()

    return False