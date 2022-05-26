canal_actual = int(input(""))
canal_llegada = int(input(""))

camino1 = canal_llegada - canal_actual
if camino1 < 0:
    camino1 *= (-1)

canales = 99 + canal_actual
camino2 = canales - canal_llegada
camino3 = canal_llegada - canal_actual + 99

if camino2 < 0:
    camino2*=(-1)

if camino1 < camino2:
    respuesta = camino1

else:
    respuesta = camino2

if respuesta > 49:
    respuesta = camino3

print(respuesta)