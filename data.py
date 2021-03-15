import pandas as pd

tble_data=pd.read_csv("Web-Design-Challenge/cities_data.csv")

tble_data.to_html("output.html")

