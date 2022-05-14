import pandas as pd
import folium
from folium import plugins

latit = 20.522188
longi = -100.814037

tiendas_df = pd.read_json('data.json')
puntos = tiendas_df
tiendas_df = tiendas_df[["Latitud","Longitud","Visita"]]
tiendas_df = tiendas_df.values
map_tiendas = folium.Map(location=[latit,longi], zoom_start=15)
for(index, row) in puntos.iterrows():
  if row.loc['Visita'].capitalize() == 'Ok':
    folium.Marker(location=[row.loc['Latitud'],row.loc['Longitud']],
                popup=row.loc['Calle']+' '+row.loc['Num_Exterior'],
                tooltip=row.loc['Nombre']+' T-'+str(row.loc['Terminales']),
                icon=folium.Icon(color='blue', icon='check', prefix='fa')).add_to(map_tiendas)
  else:
    folium.Marker(location=[row.loc['Latitud'],row.loc['Longitud']],
                popup=row.loc['Calle']+' '+row.loc['Num_Exterior'],
                tooltip=row.loc['Nombre']+' T-'+str(row.loc['Terminales']),
                icon=folium.Icon(color='orange', icon='exclamation', prefix='fa')).add_to(map_tiendas)
map_tiendas.save('index.html')