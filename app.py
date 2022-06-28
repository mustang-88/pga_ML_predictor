from datetime import datetime as dt
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from pga_scraper import fcast, fc
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import dash_auth

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)

# server = app.server

app.config.suppress_callback_exceptions = True
# Keep this out of source code repository - save in a file or a database
# VALID_USERNAME_PASSWORD_PAIRS = [
#   ['[kinray]', '[kinray'],
#  ]

# auth = dash_auth.BasicAuth(
#   app,
#  VALID_USERNAME_PASSWORD_PAIRS
# )


forecast = pd.merge(fc, fcast, on = "PLAYER NAME", how = "outer").fillna(0)

forecast = forecast.groupby(by = "PLAYER NAME").sum()

X = forecast.drop(['loc wins',],axis = 1)
y = forecast['loc wins']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model = linear_model.LinearRegression()
model.fit(X_train,y_train)
model.predict(X_test)
test_predictions = model.predict(X_test)
final_model = LinearRegression()
final_model.fit(X,y)
final_model.score(X,y)
y_hat = final_model.predict(X)
from joblib import dump,load
dump(final_model,"Traveler.joblib")
forecast['pred'] = final_model.predict(X)

forecast.to_csv("forecast.csv")

#@app.callback(
#    dash.dependencies.Output("datatable-interactivity", "data"),
#    [
#        dash.dependencies.Input("my-date-picker-range", "start_date"),
#        dash.dependencies.Input("my-date-picker-range", "end_date"),
#    ],
#)

if __name__ == '__main__':
    app.run_server(debug=True)

# fig.show()
