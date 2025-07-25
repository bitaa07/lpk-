import pandas as pd

# Buat daftar bahan kimia campuran (umum & berbahaya)
chemicals_data = [
    # Format: (Name, Formula, Hazard Level, Handling, Usage)
    ("Acetic Acid", "CH3COOH", "Medium", "Use gloves and work in a ventilated area", "Food additive, lab reagent"),
    ("Sulfuric Acid", "H2SO4", "High", "Wear goggles, gloves; avoid skin contact", "Batteries, fertilizer production"),
    ("Sodium Chloride", "NaCl", "Low", "Store in dry area", "Food seasoning, de-icing roads"),
    ("Benzene", "C6H6", "High", "Avoid inhalation; use fume hood", "Industrial solvent, precursor to plastics"),
    ("Methanol", "CH3OH", "High", "Highly flammable; keep away from flames", "Fuel, antifreeze"),
    ("Ethanol", "C2H5OH", "Medium", "Use in ventilated area", "Disinfectant, solvent"),
    ("Formaldehyde", "CH2O", "High", "Toxic vapor; wear mask", "Preservative, disinfectant"),
    ("Ammonia", "NH3", "High", "Avoid inhalation; use gas mask", "Fertilizer, cleaning agents"),
    ("Hydrochloric Acid", "HCl", "High", "Wear goggles; avoid inhalation", "Cleaning agent, pH control"),
    ("Sodium Hydroxide", "NaOH", "High", "Corrosive; wear protective clothing", "Soap making, drain cleaner"),
    ("Hydrogen Peroxide", "H2O2", "Medium", "Store in dark bottles", "Bleaching, disinfectant"),
    ("Chloroform", "CHCl3", "High", "Avoid skin contact and inhalation", "Solvent, anesthetic (historical)"),
    ("Toluene", "C7H8", "High", "Use fume hood", "Paint thinner, industrial solvent"),
    ("Acetone", "C3H6O", "Medium", "Flammable; use in well-ventilated space", "Nail polish remover, solvent"),
    ("Nitric Acid", "HNO3", "High", "Highly corrosive; use goggles and gloves", "Explosives, fertilizers"),
    ("Carbon Tetrachloride", "CCl4", "High", "Avoid inhalation; toxic", "Industrial degreasing"),
    ("Phenol", "C6H5OH", "High", "Use gloves and goggles", "Resins, antiseptics"),
    ("Aniline", "C6H5NH2", "High", "Avoid inhalation; use fume hood", "Dye manufacturing"),
    ("Hexane", "C6H14", "High", "Flammable; use in fume hood", "Solvent in labs"),
    ("Boric Acid", "H3BO3", "Low", "Avoid ingestion", "Insecticide, antiseptic"),
    ("Citric Acid", "C6H8O7", "Low", "Generally safe", "Food additive, pH adjuster"),
    ("Calcium Carbonate", "CaCO3", "Low", "Non-toxic, store dry", "Antacid, construction"),
    ("Potassium Nitrate", "KNO3", "Medium", "Oxidizer; keep away from combustibles", "Fertilizer, fireworks"),
    ("Diethyl Ether", "C4H10O", "High", "Extremely flammable; avoid sparks", "Solvent, anesthetic"),
    ("Urea", "CH4N2O", "Low", "Store in dry area", "Fertilizer, chemical feedstock"),
    ("Sodium Bicarbonate", "NaHCO3", "Low", "Non-toxic, store dry", "Baking soda, antacid"),
    ("Phosphoric Acid", "H3PO4", "Medium", "Irritant; wear gloves", "Fertilizer, food additive"),
    ("Hydrofluoric Acid", "HF", "High", "Highly toxic; specialized PPE required", "Glass etching, semiconductor"),
    ("Zinc Oxide", "ZnO", "Low", "Minimize dust inhalation", "Sunscreen, rubber additive"),
    ("Calcium Hypochlorite", "Ca(ClO)2", "High", "Corrosive; store away from organics", "Water treatment"),
    ("Titanium Dioxide", "TiO2", "Low", "Avoid inhalation of fine dust", "Paint pigment, sunscreen"),
    ("Magnesium Sulfate", "MgSO4", "Low", "Non-toxic", "Epsom salt, laxative"),
    ("Isopropanol", "C3H8O", "Medium", "Flammable; use with ventilation", "Disinfectant, solvent"),
    ("Lithium Carbonate", "Li2CO3", "Medium", "Avoid ingestion", "Bipolar treatment, ceramics"),
    ("Acetylene", "C2H2", "High", "Explosive gas; use proper regulators", "Welding, lighting"),
    ("Styrene", "C8H8", "High", "Avoid prolonged inhalation", "Plastic manufacturing"),
    ("Ethylene Glycol", "C2H6O2", "High", "Toxic if ingested", "Antifreeze"),
    ("Chromic Acid", "H2CrO4", "High", "Carcinogenic; avoid all contact", "Electroplating"),
    ("Mercury(II) Chloride", "HgCl2", "High", "Very toxic; avoid all exposure", "Reagents, disinfectant"),
    ("Arsenic Trioxide", "As2O3", "High", "Toxic; avoid inhalation and skin contact", "Pesticides, glass"),
    ("Nickel(II) Sulfate", "NiSO4", "High", "Allergen; wear gloves", "Electroplating"),
    ("Caffeine", "C8H10N4O2", "Low", "Generally safe in moderation", "Stimulant in beverages"),
    ("Lactic Acid", "C3H6O3", "Low", "Generally safe", "Food additive, skincare"),
    ("Copper(II) Sulfate", "CuSO4", "High", "Avoid ingestion", "Fungicide, lab reagent"),
    ("Thallium(I) Sulfate", "Tl2SO4", "High", "Extremely toxic", "Rodenticide (banned in many countries)"),
    ("Lead(II) Acetate", "Pb(C2H3O2)2", "High", "Toxic; avoid ingestion", "Historical use in cosmetics"),
    ("Hydrazine", "N2H4", "High", "Toxic, explosive", "Rocket propellant"),
    ("Picric Acid", "C6H3N3O7", "High", "Explosive; handle with care", "Explosives, dyes"),
    ("Barium Nitrate", "Ba(NO3)2", "High", "Toxic if ingested", "Fireworks"),
    ("Dimethyl Sulfoxide", "C2H6OS", "Medium", "Penetrates skin; use gloves", "Solvent, drug carrier"),
    ("Oxalic Acid", "C2H2O4", "Medium", "Irritant; avoid skin contact", "Cleaning agent, bleaching")
]

# Buat DataFrame
df = pd.DataFrame(chemicals_data, columns=["Name", "Chemical Formula", "Hazard Level", "Handling", "Usage"])

# Simpan ke file CSV
csv_path = "/mnt/data/data_bahan_kimia_lengkap.csv"
df.to_csv(csv_path, index=False)

csv_path


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

