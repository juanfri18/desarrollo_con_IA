estudiante = {
    "nombre": "Juanfri",
    "edad": 21,
    "nota_media": 7.23,
    "Asignaturas":["ingles","lengua","mates"]
}
estudiante["asignaturas"].append("Entornos de Desarrollo")
estudiante["nota_media"] += 0.5
print(estudiante["nombre"], estudiante["nota_media"])