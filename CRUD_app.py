from dash import Dash,dash_table,html,dcc
import pandas as pd 
import dash
df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
app=Dash(__name__)
app.layout=html.Div([
    html.H2("Table APP"),
    html.Br(),
    dash_table.DataTable(id="our_table",data=df.to_dict('records'),columns=[{"name":i , "id":i} for i in df.columns],
    editable=True,row_deletable=True,sort_action="native",filter_action="native"),
    html.Button("Add Row",id="add_row_button"),
    html.Button("Export to CSV",id="export_csv_button"),
    dcc.Store(id="Store",data=0)
])
@app.callback(dash.dependencies.Output("our_table","data"),
[dash.dependencies.Input("add_row_button","n_clicks")],
[dash.dependencies.State("our_table","data"),dash.dependencies.State("our_table","columns")])
def add_row(n_clicks,rows,cols):
    if n_clicks > 0:
        rows.append({c["id"]:" " for c in cols} )
    return rows

@app.callback(dash.dependencies.Output("Store","data"),
[dash.dependencies.Input("export_csv_button","n_clicks")],
[dash.dependencies.State("our_table","data"),dash.dependencies.State("Store","data")])
def export_csv(n_clicks,data,s):
    df=pd.DataFrame(data)
    df.to_csv("dash/exported_data.csv")
    

if __name__ == '__main__':
    app.run_server(debug=True)