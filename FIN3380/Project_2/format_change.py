# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 21:05:00 2022

@author: Mark
"""

import pandas as pd

sas = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_2\wrds_keydev_students.sas7bdat')

sas.to_excel(r'D:\Code Library\FIN3380_summer\Project_2\wrds_keydev_students.xlsx')