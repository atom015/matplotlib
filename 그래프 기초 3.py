import matplotlib.pyplot as pl

x = list(range(1001))
y = [i**2 for i in x]

#점으로 표시한다,s=점크기,외각선 제거:edgecolor='none'
#컬러맵:cmap=pl.cm.Blues
pl.scatter(x,y,c=y,s=15,edgecolor='none',cmap=pl.cm.Blues)

pl.axis([0,1100,0,1100000]) #x범위,y범위
pl.show()
