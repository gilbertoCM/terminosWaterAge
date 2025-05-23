## The Python codes were developed by Cardoso-Mohedano JG (gilbertoCM). [ORCID](https://orcid.org/0000-0002-2918-972X). 

-  The data and results were used in the publication:

# Assessing Contamination Risk Zones with Water Age Modeling in Terminos Lagoon, Southeastern Coastal Mexico (**Submitted**)

Authors:	 	 	

**Authors:**  
José-Gilberto Cardoso-Mohedano<sup>a, *</sup>, Eduardo Gómez-de la Peña<sup>b,c</sup>, Marisol Meneses-Fernández<sup>d</sup>, Joan-Albert Sánchez-Cabeza<sup>e</sup>, Ana-Carolina Ruiz-Fernández<sup>e</sup>, María Eugenia Allende-Arandía<sup>f</sup>, Mario-Alejandro Gómez-Ponce<sup>a</sup>, Carlos Alberto Herrera-Becerril<sup>b</sup>, Jorge Feliciano Ontiveros-Cuadras<sup>g</sup>

**Affiliations:**

<sup>a</sup> Estación El Carmen, Instituto de Ciencias del Mar y Limnología, Universidad Nacional Autónoma de México, Carretera Carmen-Puerto Real km. 9.5, 24157 Ciudad del Carmen, Campeche, México.  
<sup>b</sup> Posgrado en Ciencias de la Tierra, Universidad Nacional Autónoma de México, Av. Universidad 3000, Ciudad Universitaria, Coyoacán, C.P. 04510, Ciudad de México, México.  
<sup>c</sup> School of Environment, The University of Auckland, Tāmaki Makaurau / Auckland, Aotearoa / New Zealand.  
<sup>d</sup> Posgrado en Ciencias del Mar y Limnología, Universidad Nacional Autónoma de México, Av. Universidad 3000, Ciudad Universitaria, Coyoacán, C.P. 04510, Ciudad de México, México.  
<sup>e</sup> Unidad Académica Mazatlán, Instituto de Ciencias del Mar y Limnología, Universidad Nacional Autónoma de México, 82040 Mazatlán, Sinaloa, México.  
<sup>f</sup> Laboratorio de Ingeniería y Procesos Costeros, Instituto de Ingeniería, Universidad Nacional Autónoma de México, Yucatán, 97835, México.  
<sup>g</sup> Unidad Procesos Oceánicos y Costeros, Instituto de Ciencias del Mar y Limnología, Universidad Nacional Autónoma de México, Av. Universidad 3000, Ciudad Universitaria, Coyoacán, C.P. 04510, Ciudad de México, México.

**Corresponding author:**  
*José-Gilberto Cardoso-Mohedano*  
Tel: +52-938-1120285 ext: 201  
Email: [gcardoso@cmarl.unam.mx](mailto:gcardoso@cmarl.unam.mx)

- For more details on the methodology used please refer to:[doi:](https://doi.org/XXXXX)

- Please use the following link to cite the code and results: [![DOI](Zenodo- falta)](https://doi.org/XXXXX)

_________________________________________________________________________________________

For further details, please refer to the article or contact Gilberto Cardoso[^1] [^2].

[^1]: https://www.icmyl.unam.mx/el_carmen/quienes_somos/personal_academico/jose-gilberto-cardoso-mohedano
[^2]: https://blinq.me/YKZ9U8mqdr8n?bs=db

_________________________________________________________________________________________


# Repository content

## Terminos lagoon Water Age (Delt3d-WAQ)

- scripts/TerminosAgeTimeSeries.ipynb calcualtes  "water age" (days) calculate the results simulations in the Termios Lagoon studied areas:  i) Carmen Inlet, ii) Puerto Real Inlet, iii) Carmen Island, iv) Palizada Estuary, v) Candelaria Estuary, vi) Chumpan Estuary, and vii) Lagoon Center 

##  Interannual flow variability of the Candelaria and Palizada rivers

 - scripts\candelaria_palizada_rivers_analys.ipynb calculated the interannual flow variability of the Candelaria and Palizada rivers. using data bank of surface waters (CONAGUA 2014)


## Terminos Lagoon hidrodimaics model performance using Delft3D-Flow

- scripts/salinity_temperature_model_data_plot.ipynb ploted the modeled and observed temperature and salinity time series at the Ciudad del
Carmen Observatory. Southern Gulf of Mexico (Sanchez-Cabeza et al., 2019).

- salinity_temperature_model_performance_analysis evalutes  the Model performance indices comparing 30-minute results with the temperature climatological diurnal cycle calculated by averaging 30-minute records from 2016 to 2018 at Carmen City Coastal Observatory (Sanchez-Cabeza, J.A. et al., 2019). 

- temperature and salinity results from a 3D hydrodynamic model were implemented at the Ecological Modelling Laboratory, Ciudad del Carmen, ICML, UNAM, using Delft3D 4.01.00[^2].

# Data Contend

- data\salinity_temperature_climatological_year_terminos_lagoon.csv contains: 
    -  field data 
        - Date_GMT_00 (for each year)
        - Conductivity_microsiemens_cm
        - Temp_C
    - Interanual calculation
        - Conductivity_microsiemens_cm_average
        - Temp_C_av

These measurements were taken every 30 minutes using Onset U24-001 Conductivity Data Logger sensors (HOBO) at the Ciudad del Carmen Observatory 1, located at the Carmen Coastal Observatory (18°37'54.04"N, 91°49'55.15"W), in Marina Port of the Ciudad del Carmen, Campeche[^1].


- the AGE\ contains the cvs files with water age model simulations for each studied area, the water age has day for units  

**Note:** 2016 is used as the reference year.


- ESCALA_CANDELARIA_1995_2020.csv and escala_rio_palizada.csv are the gauging station mesurment from the National Water Commission of Mexico [^5].

    - date: day/mothn/year
    - water_level_msnm: meters above sea level in meteres 
    - flow_m3_s: River flow in metres by secod 


## Salinity Calculation

The salinity was calculated using a Python implementation of the Thermodynamic Equation of Seawater 2010[^2], assuming a constant sea level pressure of 0.

# Rerences

[^1]: Sanchez-Cabeza, J.A. et al. A low-cost long-term model of coastal observatories of global change. Journal of Operational Oceanography 12, (2019). https://doi.org/c4dp
[^2]: https://teos-10.github.io/GSW-Python/#gsw-python
[^3]: https://www.icmyl.unam.mx/el_carmen/quienes_somos/personal_academico/jose-gilberto-cardoso-mohedano
[^4]: https://blinq.me/YKZ9U8mqdr8n?bs=db
[^5]CONAGUA, 2014. National data bank of surface waters [WWW Document]. URL http://www.conagua.gob.mx/CONAGUA07/Contenido/Documentos/Portada BANDAS.htm (accessed 10.1.18).



