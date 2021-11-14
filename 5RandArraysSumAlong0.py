# Ref.: Data Visualization on the Web with Python & JavaScript by Kyran Dale
# Interactive plotting with Pyplot's Global State
# Creates five 100-element random arrays summed along the 0 axis.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

x = pd.period_range(datetime.now(), periods = 100, freq = 'd')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(100, 5).cumsum(0)

plt.plot(x,y)
plt.show()