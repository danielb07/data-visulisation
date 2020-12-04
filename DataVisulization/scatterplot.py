import pandas as pd
import plotly.express as px
df = pd.read_csv(r"D:\learn2code\white-hat-jr\python\data-visulisation\DataVisulization\owid-covid-data.csv")
scatter = px.scatter(df,x="date",y="total_cases", color="location",size_max=60)
scatter.show()