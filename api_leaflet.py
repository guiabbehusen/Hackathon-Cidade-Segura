import folium

# Coordenadas de Brasília
latitude = -15.7942
longitude = -47.8822

# Criar o mapa centralizado em Brasília com zoom 13
mapa = folium.Map(location=[latitude, longitude], zoom_start=15)

# Adicionar um marcador com popup em Brasília
folium.Marker(
    location=[latitude, longitude],
    popup='Você está em Brasília!'
).add_to(mapa)

# Salvar o mapa
mapa.save('mapa_brasilia.html')
