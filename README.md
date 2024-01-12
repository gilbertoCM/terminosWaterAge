# Climatological Year of Temperature and Salinity Variation (2016-2018)

This repository contains data and model simulations for the climatological year of temperature and salinity variation throughout 2016-2018.

## Data Field

The data is located in the file 'data\salinity_terminos_marina_delft3d.csv', which contains the following columns:

- Date_GMT_00 (for each year)
- Conductivity_microsiemens_cm
- Temp_C
- Conductivity_microsiemens_cm_average

## Climatological Data

The climatological data includes:

- Temp_C_average
- Conductivity_microsiemens_cm_average

These measurements were taken every 30 minutes using Onset U24-001 Conductivity Data Logger sensors (HOBO) at the Ciudad del Carmen Observatory 1, located at the Carmen Coastal Observatory (18°37'54.04"N, 91°49'55.15"W), in Marina Port of the Ciudad del Carmen, Campeche[^1].

## Salinity Calculation

The salinity was calculated using a Python implementation of the Thermodynamic Equation of Seawater 2010[^2], assuming a constant sea level pressure of 0.

## Model Data

This repository also includes temperature and salinity results from a 3D hydrodynamic model. This model was implemented at the Ecological Modelling Laboratory, Ciudad del Carmen, ICML, UNAM, using Delft3D 4.01.00[^2].

**Note:** 2016 is used as the reference year.

The model data includes:

- Time_model
- Salinity_psu_model
- Temperature_C_model

For further details, please refer to the article *In preparation* or contact Gilberto Cardoso[^4].

[^1]: Sanchez-Cabeza, J.A. et al. A low-cost long-term model of coastal observatories of global change. Journal of Operational Oceanography 12, (2019). https://doi.org/c4dp
[^2]: https://teos-10.github.io/GSW-Python/#gsw-python
[^3]: https://www.icmyl.unam.mx/el_carmen/quienes_somos/personal_academico/jose-gilberto-cardoso-mohedano
[^4]: https://blinq.me/YKZ9U8mqdr8n?bs=db