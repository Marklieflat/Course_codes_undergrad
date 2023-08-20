# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:00:42 2022

@author: Mark
"""

from csmarapi.CsmarService import CsmarService
from csmarapi.ReportUtil import ReportUtil

csmar = CsmarService()

csmar.login("120090651@link.cuhk.edu.cn", "15016744246q", '0')

database = csmar.getListDbs()
ReportUtil(database)

# tables = csmar.getListTables('Stock Trading')
# ReportUtil(tables)

# fields = csmar.getListFields()
# ReportUtil(fields)