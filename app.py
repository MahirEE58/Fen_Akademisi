import streamlit as st
import os

# Sayfa Ayarları (Sekme adı ve ikon)
st.set_page_config(page_title="8. Sınıf Fen Bilimleri Akademisi", layout="wide", page_icon="🧬")

# Bordo-Beyaz Profesyonel Tema (CSS)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stSidebar { background-color: #800000; }
    [data-testid="stSidebarNav"] { background-color: #800000; }
    h1, h2, h3 { color: #800000; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    div.stButton > button { 
        background-color: #800000; 
        color: white; 
        border-radius: 10px; 
        width: 100%; 
        font-weight: bold;
        border: 2px solid #800000;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: white;
        color: #800000;
    }
    .stMetric { color: #800000; background-color: #f8f9fa; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Puan Hafızası (Session State)
if 'puan' not in st.session_state:
    st.session_state.puan = 0

# Oyun Modüllerini İçe Aktarma (Hata almamak için kontrol ekledik)
try:
    from oyunlar import mevsimler, dna_genetik, basinc, madde, madde_tablo, enerji
except ImportError as e:
    st.error(f"Hata: Oyun dosyaları bulunamadı! Lütfen 'oyunlar' klasörünün ve içindeki dosyaların adını kontrol et. Hata: {e}")

# Yan Menü (Sidebar) Yapılandırması
st.sidebar.title("🧬 Fen Bilimleri Portalı")
menu = [
    "🏠 Ana Sayfa", 
    "🌍 Mevsimler & İklim", 
    "🧬 DNA & Genetik", 
    "⚖️ Basınç Dünyası", 
    "🧪 Madde Bilmecesi", 
    "📍 Periyodik Tablo Oyunu",
    "☀️ Enerji Dönüşümleri"
]
choice = st.sidebar.selectbox("Bir Ünite Seç", menu)

st.sidebar.divider()
st.sidebar.metric("Toplam Başarı Puanın 🏆", st.session_state.puan)
st.sidebar.write("---")
st.sidebar.info("Hedef: LGS'de Tam İsabet! 🎯")

# Sayfa İçerikleri ve Yönlendirmeler
if choice == "🏠 Ana Sayfa":
    st.title("🏆 8. Sınıf Oyunlaştırılmış Fen Akademisi")
    st.write("Fen Bilimleri dersini eğlenceli hale getiren interaktif platforma hoş geldin!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ Üniteleri Seç: Yan menüden çalışmak istediğin konuya git.")
        st.success("✅ Oyunları Oyna: Her doğru cevapta puan kazan.")
    with col2:
        st.success("✅ Bilgini Taze Tut: Her girişte farklı sorularla karşılaş.")
    
    st.image("https://images.unsplash.com/photo-1507413245164-6160d8298b31?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Bilimin ışığında başarıya!")

elif choice == "🌍 Mevsimler & İklim":
    if mevsimler.oyun(): st.session_state.puan += 20

elif choice == "🧬 DNA & Genetik":
    if dna_genetik.oyun(): st.session_state.puan += 20

elif choice == "⚖️ Basınç Dünyası":
    if basinc.oyun(): st.session_state.puan += 20

elif choice == "🧪 Madde Bilmecesi":
    # Bu kısımda senin güncellediğimiz çok sorulu madde.py çalışacak
    if madde.oyun(): st.session_state.puan += 20

elif choice == "📍 Periyodik Tablo Oyunu":
    # Yeni eklediğimiz tablo yerleştirme oyunu
    if madde_tablo.tablo_oyunu():
        st.session_state.puan += 25

elif choice == "☀️ Enerji Dönüşümleri":
    if enerji.oyun(): st.session_state.puan += 20

# Alt Bilgi
st.write("---")
st.caption("Fen Bilimleri Akademisi | LGS Hazırlık Sistemi")