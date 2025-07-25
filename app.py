import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data_bahan_kimia.csv")

df = load_data()

# Mapping simbol GHS berdasarkan tingkat bahaya
ikon_map = {
    "Tinggi": "assets/piktogram/toxic.png",
    "Sedang": "assets/piktogram/warning.png",
    "Rendah": "assets/piktogram/health_hazard.png"
}

# Judul aplikasi
st.title("🧪 Pengenalan dan Klasifikasi Bahan Kimia")
st.markdown("""
Aplikasi edukasi ini memperkenalkan berbagai bahan kimia berbahaya, rumus kimianya, serta klasifikasi bahayanya.  
Gunakan sebagai panduan pembelajaran mandiri atau alat bantu pengajaran di laboratorium dan kelas kimia.
""")

# Filter
tingkat_opsi = ["Semua"] + sorted(df["Tingkat Bahaya"].unique())
pilih = st.selectbox("🔍 Filter berdasarkan tingkat bahaya:", tingkat_opsi)
if pilih != "Semua":
    df = df[df["Tingkat Bahaya"] == pilih]

# Tampilkan data dengan ikon
for _, row in df.iterrows():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(row["Nama Bahan Kimia"])
        st.markdown(f"""
        **Rumus Kimia:** `{row['Rumus Kimia']}`  
        **Tingkat Bahaya:** `{row['Tingkat Bahaya']}`  
        **Penanganan:** {row['Penanganan']}
        """)
    with col2:
        st.image(ikon_map.get(row["Tingkat Bahaya"], "assets/piktogram/warning.png"), width=60)

st.markdown("---")
st.markdown("📚 Sumber ikon: [OSHA.gov](https://www.osha.gov/hazcom/pictograms) & [Wikipedia Commons](https://commons.wikimedia.org/wiki/GHS_pictograms)")

