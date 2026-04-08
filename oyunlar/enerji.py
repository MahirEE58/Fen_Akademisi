import streamlit as st
import random

def oyun():
    st.header("☀️ Enerji Dönüşümleri ve Besin Zinciri")
    
    tab = st.tabs(["🔗 Zincir Sıralama", "📐 Piramit Özellikleri"])
    
    with tab[0]:
        st.subheader("Besin Zincirini Kur")
        # Farklı Ekosistem Zincirleri
        zincirler = [
            {"ad": "Kara Ekosistemi", "liste": ["Ot", "Çekirge", "Kurbağa", "Yılan", "Kartal"]},
            {"ad": "Deniz Ekosistemi", "liste": ["Fitoplankton", "Zooplankton", "Küçük Balık", "Büyük Balık", "Köpek Balığı"]},
            {"ad": "Orman Ekosistemi", "liste": ["Bitki", "Tavşan", "Tilki", "Kurt"]},
            {"ad": "Göl Ekosistemi", "liste": ["Alg", "Salyangoz", "Sazan", "Balıkçıl Kuş"]}
        ]
        
        if 'secili_zincir' not in st.session_state:
            st.session_state.secili_zincir = random.choice(zincirler)
            
        z = st.session_state.secili_zincir
        karisik = list(z["liste"])
        random.shuffle(karisik)
        
        st.write(f"**{z['ad']}** canlılarını üreticiden tüketiciye sırala:")
        st.info(f"Canlılar: {', '.join(karisik)}")
        
        user_input = st.text_input("Sıralamayı virgülle yaz (Örn: Ot, Tavşan, Tilki):")
        user_list = [i.strip().title() for i in user_input.split(",") if i.strip()]
        
        if st.button("Zinciri Onayla"):
            if user_list == z["liste"]:
                st.success("Tebrikler! Enerji akışını doğru takip ettin. +20 Puan!")
                st.session_state.secili_zincir = random.choice(zincirler)
                return True
            else:
                st.error("Sıralama yanlış. Unutma: Enerji her zaman üreticiden tüketiciye akar.")

    with tab[1]:
        st.subheader("Ekoloji Piramidi Kuralları")
        st.write("Aşağıdan yukarıya (Üreticiden Son Tüketiciye) çıkıldığında bu özellikler nasıl değişir?")
        
        ozellikler = [
            {"soru": "Aktarılan Enerji Miktarı", "cevap": "Azalır"},
            {"soru": "Biyokütle (Toplam Canlı Ağırlığı)", "cevap": "Azalır"},
            {"soru": "Biyolojik Birikim (Zehirli Madde)", "cevap": "Artar"},
            {"soru": "Vücut Büyüklüğü (Genellikle)", "cevap": "Artar"},
            {"soru": "Birey Sayısı", "cevap": "Azalır"}
        ]
        
        soru_ozellik = random.choice(ozellikler)
        st.warning(f"Soru: **{soru_ozellik['soru']}** nasıl değişir?")
        secim = st.radio("Seçiminizi yapın:", ["Artar", "Azalır", "Değişmez"])
        
        if st.button("Özelliği Kontrol Et"):
            if secim == soru_ozellik["cevap"]:
                st.success(f"Harika! {soru_ozellik['soru']} gerçekten de {secim.lower()}.")
                return True
            else:
                st.error("Yanlış! Piramidin tepesine doğru gidildikçe bu özellik farklı değişir.")
    
    return False