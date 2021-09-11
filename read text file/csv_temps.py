import time
import os
import pandas


while True:
    if os.path.exists("temps_today.csv"):
        with open("temps_today.csv") as file:
            data =  pandas.read_csv("temps_today.csv")
            print(data.mean()["st2"])
    else:
        print(
            "file doesn't exists"
        )
    time.sleep(3)