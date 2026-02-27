AI-Driven Optical Screening of Fe-Based Nanoparticles for Ocular lens Applications

Overview

This project presents a physics-informed machine learning framework for screening iron-based nanoparticles (Fe, Fe₂O₃, Fe₃O₄) embedded in hydrogel contact lens systems based on their optical transmission properties.

Using COMSOL-simulated transmission data, a regression model was trained to approximate the nonlinear optical response:

𝑇
=
𝑓
(
material
,
radius
,
𝜆
)
T=f(material,radius,λ)

The trained model is then used for:

Multi-material comparison

Visible-band transparency evaluation (450–650 nm)

Constraint-based inverse screening

Sensitivity analysis of governing variables

The goal is to identify nanoparticle configurations that preserve visible transparency for potential ocular applications.

Scientific Motivation

For contact lens applications, optical transparency in the visible region (≈450–650 nm) is critical to:

Preserve photopic vision

Prevent color distortion

Minimize photothermal effects

Reduce potential optical-induced oxidative stress

Iron-based nanoparticles are of interest due to:

Magnetic properties (Fe₃O₄)

Semiconductor behavior (Fe₂O₃)

Conductive metallic properties (Fe)

However, their optical absorption behavior strongly depends on:

Material identity

Particle radius

Wavelength

This project aims to quantify and compare their visible-band transparency using a data-driven approach.

Dataset

The dataset consists of COMSOL-simulated transmission values for:

Materials: Fe, Fe₂O₃, Fe₃O₄

Radius: ≤ 30 nm

Wavelength range: full simulated spectrum (filtered to visible band for screening)

The original COMSOL output was provided in wide format and converted to long format for machine learning:

| wavelength_nm | radius_nm | material | transmission |

Transmission values were converted to 0–1 scale when necessary.

Methodology
1️⃣ Data Preprocessing

Removal of Excel header artifacts

Column renaming

Wide → long format transformation

Radius filtering (≤ 30 nm)

Transmission normalization (if in %)

2️⃣ Machine Learning Model

A Random Forest Regressor was trained to model nonlinear optical behavior:

Input features:

Material (one-hot encoded)

Radius

Wavelength

Output:

Transmission

Model performance:

𝑅
2
=
0.99989
R
2
=0.99989

This high R² reflects the smooth and deterministic nature of physics-based optical simulation data.

3️⃣ Visible-Band Transparency Metric

To evaluate suitability for contact lens applications, the following metric was defined:

𝑇
𝑣
𝑖
𝑠
𝑖
𝑏
𝑙
𝑒
𝑎
𝑣
𝑔
=
1
𝑁
∑
𝜆
=
450
650
𝑇
(
𝜆
)
T
visible
avg
	​

=
N
1
	​

λ=450
∑
650
	​

T(λ)

Additionally:

Minimum transmission in visible band was computed.

Configurations were ranked by average visible transmission.

4️⃣ Multi-Material Screening Results
Fe (Metallic Iron)

Rapid transmission drop with increasing radius.

Strong visible absorption.

No configuration satisfies avg T ≥ 0.90.

Conclusion:
Fe is unsuitable for transparency-preserving ocular applications in the tested range.

Fe₂O₃ (Hematite)

High transparency at small radii.

Visible transmission decreases as radius increases.

Meets avg T ≥ 0.90 for:

10 nm

15 nm

Fe₃O₄ (Magnetite)

Highest visible transparency overall.

Maintains avg T ≥ 0.90 up to 20 nm.

Most stable performance across radius variations.

Conclusion:
Fe₃O₄ demonstrates the most favorable optical transparency profile.

5️⃣ Inverse Design

A constraint-based inverse screening approach was implemented:

Requirement:

𝑇
𝑣
𝑖
𝑠
𝑖
𝑏
𝑙
𝑒
𝑎
𝑣
𝑔
≥
0.90
T
visible
avg
	​

≥0.90

Feasible configurations:

Material	Radius (nm)
Fe₂O₃	10, 15
Fe₃O₄	10, 15, 20

Fe does not satisfy the threshold in the studied domain.

This demonstrates a simple inverse design capability within the simulated parameter space.

6️⃣ Sensitivity Analysis

Feature importance analysis indicates:

Material identity dominates transmission variance.

Radius significantly influences scattering-induced loss.

Wavelength contributes secondary variation within visible band.

This aligns with Mie/Rayleigh scattering theory, where extinction cross-section scales with particle size.

Key Findings

Material identity is the dominant factor controlling visible transmission.

Fe₃O₄ provides the best transparency among tested materials.

Smaller radii (<20 nm) are necessary to maintain acceptable optical clarity.

Metallic Fe is unsuitable due to broadband absorption.

Limitations

Optical transparency does not imply full ocular biocompatibility (no ROS, cytotoxicity, or inflammatory modeling included).

Simulations assume ideal, monodisperse nanoparticles without aggregation or concentration effects.

No surface chemistry or coating effects are considered.

Model is valid only within the simulated parameter range (r ≤ 30 nm).

Thermal effects, long-term stability, and in vivo lens conditions are not modeled.