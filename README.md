##  Code and Data for Water Age Analysis in Terminos Lagoon, Southeastern Coastal Mexico 

The Python scripts were developed by José-Gilberto Cardoso-Mohedano ([ORCID](https://orcid.org/0000-0002-2918-972X)).

The data and results presented here are part of the manuscript:

### *Assessing Contamination Risk Zones with Water Age Modeling in Terminos Lagoon, Southeastern Coastal Mexico* (**Submitted**)

**Authors:**  
José-Gilberto Cardoso-Mohedano<sup>a, *</sup>, Eduardo Gómez-de la Peña<sup>b,c</sup>, Marisol Meneses-Fernández<sup>d</sup>, Joan-Albert Sanchez-Cabeza<sup>e</sup>, Ana-Carolina Ruiz-Fernández<sup>e</sup>, María Eugenia Allende-Arandía<sup>f</sup>, Mario-Alejandro Gómez-Ponce<sup>a</sup>, Carlos Alberto Herrera-Becerril<sup>b</sup>, Jorge Feliciano Ontiveros-Cuadras<sup>g</sup>

**Affiliations:**

<sup>a</sup> Estación El Carmen, Instituto de Ciencias del Mar y Limnología, UNAM, Ciudad del Carmen, Campeche, México  
<sup>b</sup> Posgrado en Ciencias de la Tierra, UNAM, Ciudad de México, México  
<sup>c</sup> School of Environment, The University of Auckland, Aotearoa / New Zealand  
<sup>d</sup> Posgrado en Ciencias del Mar y Limnología, UNAM, Ciudad de México, México  
<sup>e</sup> Unidad Académica Mazatlán, Instituto de Ciencias del Mar y Limnología, UNAM, Sinaloa, México  
<sup>f</sup> Laboratorio de Ingeniería y Procesos Costeros, Instituto de Ingeniería, UNAM, Yucatán, México  
<sup>g</sup> Unidad de Procesos Oceánicos y Costeros, Instituto de Ciencias del Mar y Limnología, UNAM, Ciudad de México, México  

**Corresponding author:**  
*José-Gilberto Cardoso-Mohedano*  
Tel: +52-938-1120285 ext. 201  
Email: [gcardoso@cmarl.unam.mx](mailto:gcardoso@cmarl.unam.mx)

For more details on the methodology, please refer to: [DOI submitted](https://doi.org/XXXXX)  
To cite this repository: [![Falta DOI Zenodo](https://doi.org/XXXXX)](https://doi.org/XXXXX)

---

For further inquiries, please contact Gilberto Cardoso [[Profile 1](https://www.icmyl.unam.mx/el_carmen/quienes_somos/personal_academico/jose-gilberto-cardoso-mohedano), [Profile 2](https://blinq.me/YKZ9U8mqdr8n?bs=db)].

---

## Repository Contents

### 1. Water Age Modeling in Terminos Lagoon (Delft3D-WAQ)

- `scripts/TerminosAgeTimeSeries.ipynb`: Calculates water age (in days) from model simulations for the following areas:  
  i) Carmen Inlet  
  ii) Puerto Real Inlet  
  iii) Carmen Island  
  iv) Palizada Estuary  
  v) Candelaria Estuary  
  vi) Chumpan Estuary  
  vii) Lagoon Center  

### 2. Interannual Flow Variability of the Candelaria and Palizada Rivers

- `scripts/candelaria_palizada_rivers_analys.ipynb`: Analyzes flow variability using data from the National Water Commission of Mexico (CONAGUA, 2014).

### 3. Delft3D Hydrodynamic Model Performance

- `scripts/salinity_temperature_model_data_plot.ipynb`: Compares modeled vs. observed salinity and temperature time series at Ciudad del Carmen Observatory [^1].  
- `scripts/salinity_temperature_model_performance_analysis.ipynb`: Evaluates model performance using 30-minute time steps and climatological diurnal cycles from 2016–2018.  
- The 3D hydrodynamic model was implemented using **Delft3D 4.01.00** at the Ecological Modelling Laboratory, ICML, UNAM.

---

## Data Contents

- `data/salinity_temperature_climatological_year_terminos_lagoon.csv` contains:  
  - Field data (30-min interval):  
    - `Date_GMT_00`  
    - `Conductivity_microsiemens_cm`  
    - `Temp_C`  
  - Interannual means:  
    - `Conductivity_microsiemens_cm_average`  
    - `Temp_C_av`  

  > Measurements were collected with Onset U24-001 Conductivity Loggers at Carmen Coastal Observatory (18°37'54.04"N, 91°49'55.15"W).

- `AGE/` folder: Contains CSV files with water age model results (in days) for each zone of study.  
  > Reference year for modeling: **2016**

- `ESCALA_CANDELARIA_1995_2020.csv` and `escala_rio_palizada.csv`:  
  Flow and water level records from CONAGUA.  
  - `date`: dd/mm/yyyy  
  - `water_level_msnm`: Meters above sea level  
  - `flow_m3_s`: River discharge (m³/s)

**We thank Laurel-Castillo J.A. for providing the river database**

---

## Salinity Calculation

Salinity was computed in Python using the [TEOS-10 GSW toolbox](https://teos-10.github.io/GSW-Python/#gsw-python), assuming constant sea level pressure.



---

## References

[^1]: Sánchez-Cabeza, J.A. et al. (2019). *A low-cost long-term model of coastal observatories of global change*. Journal of Operational Oceanography, 12. https://doi.org/c4dp  
[^2]: TEOS-10 GSW-Python Toolbox: https://teos-10.github.io/GSW-Python/#gsw-python  
[^3]: [Author profile - ICML UNAM](https://www.icmyl.unam.mx/el_carmen/quienes_somos/personal_academico/jose-gilberto-cardoso-mohedano)  
[^4]: [Digital profile](https://blinq.me/YKZ9U8mqdr8n?bs=db)  
[^5]: CONAGUA (2014). *National Data Bank of Surface Waters*. [Accessed 2018-10-01]. http://www.conagua.gob.mx/CONAGUA07/Contenido/Documentos/Portada%20BANDAS.htm  


[![Licencia: CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)
