import matplotlib.pyplot as pl

y = [5,3,7,10,9,5,3.5,8]
x = range(len(y))

#bar차트,width=가로길이,color=색깔
pl.bar(x,y,width=0.7,color="red")
pl.show()
