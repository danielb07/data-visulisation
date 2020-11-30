import pandas as pd
import plotly.express as px

df = pd.read_csv("owid-covid-data.csv")
scatter = px.scatter(df,x="date",y="total_cases", size="Percentage", color="location",size_max=60)
scatter.show()