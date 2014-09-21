from pylab import plotfile, show, gca
import matplotlib.cbook as cbook

fname = cbook.get_sample_data('msft.csv',asfileobj=False)

plotfile(fname,(0,5,6))
plotfile(fname,('date','volume','adj_close'))

show()
