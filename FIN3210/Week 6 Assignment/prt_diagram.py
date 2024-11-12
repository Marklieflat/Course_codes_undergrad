import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


szAvgValue = [
  32.38391638252858,
  36.50634539114002,
  38.80474699309658,
  38.811108559080246,
  44.0373671236599,
  43.767814972729205,
  47.12902025737412,
  44.249068329009226,
  45.8894530314892,
  45.7029861996234,
  49.61384016666555,
  48.48991983747511,
  46.64316515809291,
  49.109781898409004,
  50.61905493623875,
  51.395031735043105,
  50.086481459015786,
  52.235115047110746,
  54.68677423268231,
  52.87250179540762,
  54.4473427966951
]

svAvgValue = [
  22.33789554959651,
  20.31955938089702,
  22.336252799323397,
  22.629322331471958,
  23.157484565676405,
  23.812005613063857,
  23.918587346898267,
  21.362153949168476,
  21.0289239384998,
  20.784027597563846,
  21.048950113574872,
  19.498192253843797,
  20.11356922938916,
  20.130097651932402,
  21.000432513480032,
  20.72192506944247,
  20.899269552681083,
  22.955872011533355,
  21.636720195426676,
  21.2411014356244,
  21.248510231346685
]

yearValue = np.array([i for i in range(1993, 2014)])
szAvgValue = np.array(szAvgValue)
svAvgValue = np.array(svAvgValue)

plt.figure(figsize=(10, 5))
plt.plot(yearValue, szAvgValue, label='SZ')
plt.plot(yearValue, svAvgValue, label='SV')
plt.title('Average Value of nighttime lights between Shenzhen and Silicon Valley')
plt.xlabel('Year')
plt.ylabel('Average Value of nighttime lights')
x_major_locator=MultipleLocator(2)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend()
plt.show()
