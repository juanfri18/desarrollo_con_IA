coordenadas = (40.4168, -3.7038) 



def separar_coordenadas(coord):
    latitud, longitud = coord
    return (latitud,), (longitud,)

lat, lon = separar_coordenadas(coordenadas)
print(lat, lon)
