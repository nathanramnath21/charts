import pandas as pd 
import plotly.express as px
df=pd.read_csv("data.csv")
flg=px.scatter(df, x="Population", y="Per capita", color="Country", size="Percentage" ,title='Internet Users', size_max=60)
flg.show()