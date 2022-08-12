# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:12:29 2022

@author: Cardoso-Mohedano JG
"""
 # %% 

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import gsw as gsw
import matplotlib.dates as mdates
from dateutil.relativedelta import relativedelta

# %% 

def makePretryGraphs():

    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    sns.set_style("ticks")
    sns.despine(top=False, right=False)
    

# %% read my data base

sal_temp_terminos_semar= "TerminosSalTempSEMAR_duplicatedRemoved.csv"

terminos_sal_temp_SEMAR = pd.read_csv(sal_temp_terminos_semar, sep=",", header=0, 
                                      decimal=".", encoding = 'utf-8')

sal_terminos_delft3d= "salinity_terminos_marina_delft3d.csv"

terminos_sal_delft3d= pd.read_csv(sal_terminos_delft3d, sep=",", header=0, 
                                      decimal=".", encoding = 'utf-8')


# %% Set date time 

terminos_sal_temp_SEMAR["Date_GMT_00"] =  pd.to_datetime(terminos_sal_temp_SEMAR["Date_GMT_00"], 
                                                        format= '%d/%m/%Y %H:%M')

terminos_sal_temp_SEMAR = terminos_sal_temp_SEMAR.set_index(terminos_sal_temp_SEMAR["Date_GMT_00"])


terminos_sal_delft3d["Time_2017"] =  pd.to_datetime(terminos_sal_delft3d["Time_2017"], 
                                                        format= '%d/%m/%Y %H:%M')


terminos_sal_delft3d = terminos_sal_delft3d.set_index(terminos_sal_delft3d["Time_2017"])


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']




# %% Calculate salinity from hobo conductivity 


terminos_sal_temp_SEMAR["FalsePreasure"] = 0
                                  
terminos_sal_temp_SEMAR["Salinity_psu"] = gsw.conversions.SP_from_C(terminos_sal_temp_SEMAR["Conductivity_microsiemens_cm"]/1000, 
                                                                    terminos_sal_temp_SEMAR["Temp_C"], 
                                                                    terminos_sal_temp_SEMAR["FalsePreasure"])



# %% 
start_date = "2017-01-01 01:00:00"

end_date = "2017-08-04 00:00:00"

mask = (terminos_sal_temp_SEMAR["Date_GMT_00"] > start_date) & (terminos_sal_temp_SEMAR["Date_GMT_00"] <= end_date)

terminos_sal_temp_SEMAR_2017 = terminos_sal_temp_SEMAR.loc[mask]
 

mask = (terminos_sal_delft3d["Time_2017"] > start_date) & (terminos_sal_delft3d["Time_2017"] <= end_date)
   
terminos_sal_delft3d = terminos_sal_delft3d.loc[mask]


# %% 

sns.relplot( x = 'Date_GMT_00',
             y = 'Salinity_psu',
             data = terminos_sal_temp_SEMAR_2017,
             color = "#5ec962", 
             dashes=False, 
             height=10, aspect=1.5)
  

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.ylabel("Salinity (psu)",fontsize=20)
plt.xlabel("Date",fontsize=25)

makePretryGraphs()

plt.show()


# %% 


sns.relplot( x = 'Time_2017',
             y = 'salinity_psu',
             data = terminos_sal_delft3d,
             color = "#5ec962", 
             dashes=False, 
             height=10, aspect=1.5)
  

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.ylabel("salinity (psu)",fontsize=20)
plt.xlabel("Date",fontsize=25)

makePretryGraphs()

plt.show()


# %% 

  

def bias(predictions, targets):
        difference = (predictions - targets)
        bias_val = difference.mean()
        print ("Bias results =")
        return bias_val               
    
def mse(predictions, targets): #  Mean Square Error (MSE): Bennett et al. 2013
    differences_squared = (predictions - targets) ** 2                       
    mse_val =  differences_squared.mean()
    print ("Mean Square Error result =")             
    return mse_val  

def rmse(predictions, targets): # Root Mean Square Error (RMSE): Bennett et al. 2013
    differences_squared = (predictions - targets) ** 2                       
    rmse_val = np.sqrt( differences_squared.mean())
    print ("Root Mean Square Error result =")               
    return rmse_val


def mae(predictions, targets): # Mean Absolute Error (MAE)
     absoluteDifference = np.absolute(predictions - targets)
     mae_val = absoluteDifference.mean()
     print ("Mean Absolute Error result =")
     return mae_val

 
def ame(predictions, targets): # Absolute Maximun Error (AME)
    difference = (predictions - targets)
    ame_val = max(np.abs(difference))
    print ("Absolute Maximun Error result =")
    return ame_val

          
def modelSkill(model, observations):
    differences = model - observations
    differencesSquared = abs(differences)**2
    sumDifferencesSquared = sum(differencesSquared)
    meanObservations = np.mean(observations)
    modelMinusMeanObservations = np.absolute(list(np.asarray(model) - meanObservations))
    observationsMinusMeanObservations = np.absolute(list(np.asarray(observations) - meanObservations))
    denominator = sum(np.square(modelMinusMeanObservations + observationsMinusMeanObservations))
    skill = 1 - sumDifferencesSquared / denominator
    print ("Skill result")
    return skill 


def willmottAgreement(predictions, targets):
    """
	index of agreement
	
	Willmott (1981, 1982) 
	input:
        s: simulated
        o: observed
    output:
        ia: index of agreement
    """
    ia = 1 -(np.sum((targets-predictions)**2))/(np.sum((np.abs(predictions-np.mean(targets))+np.abs(targets-np.mean(targets)))**2))
    print ("Willmott agreement")
    return ia

def runMyStat(predictions, targets):
    print (bias(predictions, targets))
    print (mse(predictions, targets))
    print (rmse(predictions, targets))
    print (mae(predictions, targets))
    print (ame(predictions, targets))    
    #print (modelSkill(predictions, targets))
    print (willmottAgreement(predictions, targets))
    


 

# %% 

runMyStat(terminos_sal_delft3d['salinity_psu'],terminos_sal_temp_SEMAR_2017['Salinity_psu'] )

