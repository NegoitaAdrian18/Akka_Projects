"""
DE UTILIZAT
"""
import json
import os
import time
from os import getpid
import psutil
from datetime import datetime
import subprocess
import asyncio
import pandas as pd
import numpy as np


class Proces:

    def __init__(self):
        self.process_name = str(input("Introdu numele procesului: "))
        self.time_interval = int(input("Insert the time interval: "))

    async def run_proces(self):
        subprocess.Popen(["python", self.process_name],
                         shell=True
                         )

        await asyncio.sleep(1)

    async def collect_info(self):
        collected_info = list()
        for i in range(self.time_interval):
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_usage = psutil.Process(os.getpid())
            memory = mem_usage.memory_info().rss
            process = psutil.Process(getpid()).num_handles()
            collected_info.append({
                "cpu_usage": cpu_usage,
                "mem_usage": memory,
                "process": process
            })
            print(f"cpu_usage is: {cpu_usage}")
            print(f"mem_usage is: {mem_usage.memory_info().rss}")

        with open("data_collection.json", "w") as file:
            pd.DataFrame(collected_info).to_csv('data_collection.csv')
            print(pd.DataFrame(collected_info))
        await asyncio.sleep(2)



    async def funct(self):
        task1 = asyncio.create_task(self.run_proces())
        task2 = asyncio.create_task(self.collect_info())

        await task1
        await task2



asyncio.run(Proces().funct())
