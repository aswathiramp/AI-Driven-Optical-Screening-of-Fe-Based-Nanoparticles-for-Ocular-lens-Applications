"""
AI-Driven Optical Screening of Fe-Based Nanoparticles
Materials Physics Project

Author: Aswathi Ram P
Description:
    ML-based screening of Fe, Fe2O3, Fe3O4 nanoparticles
    for visible-band transparency in hydrogel contact lenses.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# =====================================================
# 1. LOAD AND CLEAN DATA
# =====================================================

file_path = r"data/data iron all.csv"

# Skip Excel title row
df = pd.read_csv(file_path, skiprows=1)

# Clean column names
df.columns = df.columns.str.strip()

# Rename columns
df = df.rename(columns={
    "lambda": "wavelength_nm",
    "radius (nm)": "radius_nm"
})

# Convert wide → long format
df_long = df.melt(
    id_vars=["wavelength_nm", "radius_nm"],
    value_vars=["Fe", "Fe2O3", "Fe3O4"],
    var_name="material",
    value_name="transmission"
)

# Convert % to 0–1 if needed
if df_long["transmission"].max() > 1.5:
    df_long["transmission"] /= 100

# Filter radius ≤ 30 nm
df_long = df_long[df_long["radius_nm"] <= 30]

print("Final dataset shape:", df_long.shape)
print("Transmission range:",
      df_long["transmission"].min(),
      "to",
      df_long["transmission"].max())

# =====================================================
# 2. VISUALIZATION (Separate Graph per Material)
# =====================================================

materials = df_long["material"].unique()

for mat in materials:
    plt.figure(figsize=(8, 6))
    subset = df_long[df_long["material"] == mat]
    radii = sorted(subset["radius_nm"].unique())

    for r in radii:
        data_r = subset[subset["radius_nm"] == r]
        data_r = data_r.sort_values("wavelength_nm")

        plt.plot(
            data_r["wavelength_nm"],
            data_r["transmission"],
            label=f"r = {r} nm"
        )

    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Transmission")
    plt.title(f"{mat} — Transmission vs Wavelength (r ≤ 30 nm)")
    plt.legend()
    plt.grid(True)
    plt.show()

# =====================================================
# 3. TRAIN ML MODEL
# =====================================================

X = df_long[["radius_nm", "wavelength_nm", "material"]]
y = df_long["transmission"]

# One-hot encode material
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), ["material"])
    ],
    remainder="passthrough"
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

pipeline = Pipeline(steps=[
    ("preprocess", preprocessor),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

pipeline.fit(X_train, y_train)

r2 = pipeline.score(X_test, y_test)
print("\nModel R²:", r2)

# =====================================================
# 4. VISIBLE BAND METRIC (450–650 nm)
# =====================================================

visible_min = 450
visible_max = 650

results = []

for mat in materials:
    for r in sorted(df_long["radius_nm"].unique()):
        wl_range = np.arange(visible_min, visible_max + 1, 5)

        input_df = pd.DataFrame({
            "radius_nm": r,
            "wavelength_nm": wl_range,
            "material": mat
        })

        T_pred = pipeline.predict(input_df)

        results.append({
            "material": mat,
            "radius_nm": r,
            "avg_visible_T": np.mean(T_pred),
            "min_visible_T": np.min(T_pred)
        })

metrics_df = pd.DataFrame(results)

print("\nVisible-band metrics:")
print(metrics_df)

# =====================================================
# 5. RANK MATERIALS
# =====================================================

ranked = metrics_df.sort_values(
    by="avg_visible_T",
    ascending=False
)

print("\nRanked configurations:")
print(ranked)

# =====================================================
# 6. CONSTRAINT: avg_visible_T ≥ 0.90
# =====================================================

threshold = 0.90

feasible = metrics_df[
    metrics_df["avg_visible_T"] >= threshold
    ]

print(f"\nConfigurations with avg_visible_T ≥ {threshold}:")
print(feasible)

# =====================================================
# 7. FEATURE IMPORTANCE (Sensitivity)
# =====================================================

importances = pipeline.named_steps["model"].feature_importances_
feature_names = pipeline.named_steps["preprocess"].get_feature_names_out()

print("\nFeature Importance:")
for name, imp in zip(feature_names, importances):
    print(f"{name}: {imp:.4f}")

print("\nProject Complete.")

