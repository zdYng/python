import pandas as pd
parameters = pd.read_csv("F:\\learnPython\\sparktest\\csv_data_task01\\parameters_final.csv")
par_av = list(map(lambda x : x+'.AV',list(parameters["Paramters"])))
