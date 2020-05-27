import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

sankey = Sankey()
sankey.add(flows=[1, -1],
       labels=['input', 'output'])
sankey.finish()

