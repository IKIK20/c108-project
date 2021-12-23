import pandas as pd
df= pd.read_csv("data.csv")
import plotly_express as px
import plotly.figure_factory as ff

fig=ff.create_distplot([df["Avg Rating"].tolist()],["Rating"], show_hist= True )

fig.show()