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

# %%


def makePretryGraphs():

    plt.rcParams["xtick.labelsize"] = 18
    plt.rcParams["ytick.labelsize"] = 18
    sns.set_style("ticks")
    sns.despine(top=False, right=False)


# %% read my data base

sal_temp_terminos_semar_model = "salinity_terminos_marina_delft3d.csv"

terminos_sal_temp_rawdata = pd.read_csv(
    sal_temp_terminos_semar_model, sep=",", header=0, decimal=".", encoding="utf-8"
)

for col in terminos_sal_temp_rawdata.columns:
    print(col)
terminos_sal_temp = terminos_sal_temp_rawdata[
    [
        "Time_model",
        "salinity_psu_model",
        "temperature_C_model",
        "Conductivity_microsiemens_cm_average",
        "Temp_C_average",
    ]
]


# %% Set date time

terminos_sal_temp["Time_model"] = pd.to_datetime(
    terminos_sal_temp["Time_model"], format="%d/%m/%Y %H:%M"
)

terminos_sal_temp = terminos_sal_temp.set_index(terminos_sal_temp["Time_model"])


terminos_sal_temp = terminos_sal_temp.set_index(terminos_sal_temp["Time_model"])


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# %% Calculate salinity from hobo conductivity

terminos_sal_temp["falsePreasure"] = 0

terminos_sal_temp["salinity_psu"] = gsw.conversions.SP_from_C(
    terminos_sal_temp["Conductivity_microsiemens_cm_average"] / 1000,
    terminos_sal_temp["Temp_C_average"],
    terminos_sal_temp["falsePreasure"],
)


# %%

plt.figure(figsize=(20, 12))

plt.plot_date(
    terminos_sal_temp["Time_model"],
    terminos_sal_temp["Temp_C_average"],
    "*",
    color="#440154",
)

plt.xlim(min(terminos_sal_temp["Time_model"]), max(terminos_sal_temp["Time_model"]))

plt.xticks(size=28)

plt.yticks(size=28)

plt.ylabel("Temperature (\u00b0C)", size=34)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b"))

plt.rc("pdf", fonttype=42)


plt.xlim(min(terminos_sal_temp["Time_model"]), max(terminos_sal_temp["Time_model"]))


plt.plot_date(
    terminos_sal_temp["Time_model"],
    terminos_sal_temp["temperature_C_model"],
    ".",
    color="#5ec962",
)

plt.savefig("temperatureModelDataSMAR.pdf")


# %%


plt.figure(figsize=(20, 12))

plt.plot_date(
    terminos_sal_temp["Time_model"],
    terminos_sal_temp["salinity_psu"],
    "*",
    color="#440154",
)

plt.xlim(min(terminos_sal_temp["Time_model"]), max(terminos_sal_temp["Time_model"]))

plt.xticks(size=28)

plt.yticks(size=28)

plt.ylabel("Salinity (psu)", size=34)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b"))

plt.rc("pdf", fonttype=42)


plt.xlim(min(terminos_sal_temp["Time_model"]), max(terminos_sal_temp["Time_model"]))


plt.plot_date(
    terminos_sal_temp["Time_model"],
    terminos_sal_temp["salinity_psu_model"],
    ".",
    color="#5ec962",
)

plt.savefig("salinityModelDataSMAR.pdf")


# %%


def bias(predictions, targets):
    difference = predictions - targets
    bias_val = difference.mean()
    print("Bias results =")
    return bias_val


def mse(predictions, targets):  # Mean Square Error (MSE): Bennett et al. 2013
    differences_squared = (predictions - targets) ** 2
    mse_val = differences_squared.mean()
    print("Mean Square Error result =")
    return mse_val


def rmse(predictions, targets):  # Root Mean Square Error (RMSE): Bennett et al. 2013
    differences_squared = (predictions - targets) ** 2
    rmse_val = np.sqrt(differences_squared.mean())
    print("Root Mean Square Error result =")
    return rmse_val


def mae(predictions, targets):  # Mean Absolute Error (MAE)
    absoluteDifference = np.absolute(predictions - targets)
    mae_val = absoluteDifference.mean()
    print("Mean Absolute Error result =")
    return mae_val


def ame(predictions, targets):  # Absolute Maximun Error (AME)
    difference = predictions - targets
    ame_val = max(np.abs(difference))
    print("Absolute Maximum Error result =")
    return ame_val


def modelSkill(model, observations):
    differences = model - observations
    differencesSquared = abs(differences) ** 2
    sumDifferencesSquared = sum(differencesSquared)
    meanObservations = np.mean(observations)
    modelMinusMeanObservations = np.absolute(list(np.asarray(model) - meanObservations))
    observationsMinusMeanObservations = np.absolute(
        list(np.asarray(observations) - meanObservations)
    )
    denominator = sum(
        np.square(modelMinusMeanObservations + observationsMinusMeanObservations)
    )
    skill = 1 - sumDifferencesSquared / denominator
    print("Skill result = ")
    return skill


def willmottAgreement(predictions, targets):
    """
        index of agreement Willmott (1981, 1982) 
        input:
        s: simulated
        o: observed
    output:
        ia: index of agreement
    """
    ia = 1 - (np.sum((targets - predictions) ** 2)) / (
        np.sum(
            (
                np.abs(predictions - np.mean(targets))
                + np.abs(targets - np.mean(targets))
            )
            ** 2
        )
    )
    print("Willmott agreement = ")
    return ia


def runMyStat(predictions, targets):
    print(bias(predictions, targets))
    print(mse(predictions, targets))
    print(rmse(predictions, targets))
    print(mae(predictions, targets))
    print(ame(predictions, targets))
    print(modelSkill(predictions, targets))
    print(willmottAgreement(predictions, targets))


# %%
runMyStat(terminos_sal_temp["salinity_psu"], terminos_sal_temp["salinity_psu_model"])

runMyStat(terminos_sal_temp["temperature_C_model"], terminos_sal_temp["Temp_C_average"])
