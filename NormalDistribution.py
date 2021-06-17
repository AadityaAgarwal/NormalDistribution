import csv
from os import name
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('StudentsPerformance.csv')
data=list(df["reading score"])


mean=sum(data)/len(data)
median=statistics.median(data)
mode=statistics.mode(data)
sd=statistics.stdev(data)

firstSDStart,firstSDEnd=(mean-sd),(mean+sd)
secondSDStart,secondSDEnd=(mean-(2*sd)),(mean+(2*sd))
thirdSDStart,thirdSDEnd=(mean-(3*sd)),(mean+(3*sd))

listOfFirstSD=[result for result in data if result>firstSDStart and result<firstSDEnd ]
listOfSecondSD=[result for result in data if result>secondSDStart and result<secondSDEnd ]
listOfThirdtSD=[result for result in data if result>thirdSDStart and result<thirdSDEnd ]

length1=len(listOfFirstSD)
length2=len(listOfSecondSD)
length3=len(listOfThirdtSD)

# mean1=statistics.mean(list(firstSDStart))

percentage1=(length1/len(data))*100
percentage2=(length2/len(data))*100
percentage3=(length3/len(data))*100

fig=ff.create_distplot([data],['reading score'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[firstSDStart,firstSDStart],y=[0,0.17],name="SD1",mode="lines"))
fig.add_trace(go.Scatter(x=[secondSDStart,secondSDStart],y=[0,0.17],name="SD1",mode="lines"))
fig.add_trace(go.Scatter(x=[thirdSDStart,thirdSDStart],y=[0,0.17],name="SD1",mode="lines"))
fig.show()

print("Mean of the data",mean," \nStandardDeviation of data",sd)
print(percentage1,"% of data lies within SD1")
print(percentage2,"% of data lies within SD2")
print(percentage3,"% of data lies within SD3")
