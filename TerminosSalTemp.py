# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:30:06 2022

@author: Cardoso-Mohedano JG
"""

# %% 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import gsw as gsw
import matplotlib.dates as mdates

# %% read my data base

file_name = "TerminosSalTempSEMAR_duplicatedRemoved.csv"

csv_file =  file_name

terminos_sal_temp_SEMAR = pd.read_csv(csv_file, sep=",", header=0, 
                                      decimal=".", encoding = 'utf-8')

# %% 

terminos_sal_temp_SEMAR["Date_GMT_00"] =  pd.to_datetime(terminos_sal_temp_SEMAR["Date_GMT_00"], 
                                                        format= '%d/%m/%Y %H:%M')

terminos_sal_temp_SEMAR = terminos_sal_temp_SEMAR.set_index(terminos_sal_temp_SEMAR["Date_GMT_00"])

terminos_sal_temp_SEMAR["FalsePreasure"] = 0
                                  
terminos_sal_temp_SEMAR["Salinity_psu"] = gsw.conversions.SP_from_C(terminos_sal_temp_SEMAR["Conductivity_microsiemens_cm"]/1000, 
                                                                    terminos_sal_temp_SEMAR["Temp_C"], 
                                                                    terminos_sal_temp_SEMAR["FalsePreasure"])

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']


# %% 

def makePretryGraphs():

    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    sns.set_style("ticks")
    sns.despine(top=False, right=False)
    

# %% 

start_date = "2016-10-26 19:00:00"

end_date = "2017-08-04 00:00:00"

mask = (terminos_sal_temp_SEMAR["Date_GMT_00"] > start_date) & (terminos_sal_temp_SEMAR["Date_GMT_00"] <= end_date)

terminos_sal_temp_SEMAR_2017 = terminos_sal_temp_SEMAR.loc[mask]
    

# %% 

terminos_sal_temp_SEMAR_2017['Salinity_psu_daily'] = terminos_sal_temp_SEMAR_2017["Salinity_psu"].resample('D').mean()

sns.relplot( x = 'Date_GMT_00',
             y = 'Salinity_psu',
             data = terminos_sal_temp_SEMAR_2017,
             color = "#5ec962", 
             dashes=False, 
             height=10, aspect=1.5)
  
sns.lineplot( x = 'Date_GMT_00',
             y = 'Salinity_psu_daily',
             data = terminos_sal_temp_SEMAR_2017,
             color = "#440154",
             linewidth=2.5)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.ylabel("Salinity (psu)",fontsize=20)
plt.xlabel("Date",fontsize=25)

makePretryGraphs()

plt.show()


# %% 

terminos_sal_temp_SEMAR_2017['Temp_C_daily'] = terminos_sal_temp_SEMAR_2017["Temp_C"].resample('D').mean()


sns.relplot( x = 'Date_GMT_00',
             y = 'Temp_C',
             data = terminos_sal_temp_SEMAR_2017,
             color = "#5ec962", 
             dashes=False, 
             height=10, aspect=1.5)

  
sns.lineplot( x = 'Date_GMT_00',
             y = 'Temp_C_daily',
             data = terminos_sal_temp_SEMAR_2017,
             color = "#440154",
             linewidth=2.5)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.ylabel("Temperature (°C)",fontsize=20)
plt.xlabel("Date",fontsize=25)

makePretryGraphs()

plt.show()


# %% 


ax = sns.boxplot(x="Month",  y="Salinity_psu", 
            data = terminos_sal_temp_SEMAR,
            order = months, 
            linewidth=1,
            palette="viridis"
            )

plt.ylabel("Salinity (psu)",fontsize=20)
plt.xlabel("",fontsize=25)


makePretryGraphs()

plt.show()



#plt.savefig('Salinity.pdf', dpi=600)
 
# %% 


ax = sns.boxplot(x="Month",  y="Temp_C", 
            data = terminos_sal_temp_SEMAR,
            order = months, 
            linewidth=1,
            palette="viridis"
            )

plt.ylabel("Temperature (°C)",fontsize=20)
plt.xlabel("",fontsize=25)


makePretryGraphs()


#plt.savefig('Temperature.pdf', dpi=600)
 

