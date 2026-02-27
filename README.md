AI-Driven Optical Screening of Fe-Based Nanoparticles
Overview

This repository presents a physics-informed machine learning workflow for screening Fe, Fe₂O₃, and Fe₃O₄ nanoparticles embedded in 
hydrogel contact lenses based on visible-band optical transparency.

Using COMSOL-simulated transmission data, a regression model was trained to approximate:

T = f(material, radius, wavelength)

The framework enables:

* Multi-material comparison

* Visible-band transparency evaluation (450–650 nm)

* Constraint-based inverse screening 

* Sensitivity analysis

**Key Findings**

* Fe₃O₄ provides highest visible transparency. 

* Fe₂O₃ performs well at small radii. 

* Metallic Fe shows strong absorption and is unsuitable. 

* Radii ≤ 20 nm are required for maintaining avg transmission ≥ 0.90.

**Methodology**

* COMSOL optical simulation 

* Data restructuring (wide → long format)

* Random Forest regression modeling 

* Visible-band transparency metric definition 

* Constraint-based inverse screening 

* Feature importance analysis

**Limitations**

* Optical transparency does not imply full biocompatibility. 

* No ROS, cytotoxicity, or concentration modeling. 

* Valid only within simulated radius and wavelength ranges. 

* Assumes ideal nanoparticle dispersion.