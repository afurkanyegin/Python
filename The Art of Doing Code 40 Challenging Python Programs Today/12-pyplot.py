from matplotlib import pyplot

x_values=[]
y_values=[]

for a in range(1,61):
      x_values.append(a)
      if a % 3 == 0:
            y_values.append(a*3)
      else:
            y_values.append(a)

pyplot.plot(x_values,y_values)
pyplot.title("Deneme")
pyplot.xlabel("aşağı taraf")
pyplot.ylabel("sol taraf")
pyplot.show()
