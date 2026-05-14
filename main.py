# Importaciones de cada integrante
   # Integrante A
   from distancia import calcular_distancia
    #integrante b
from eta import calcular_eta                  # Integrante C


# Programa principal
def main():
    print("=== SISTEMA DE LOGÍSTICA Y TRANSPORTE ===")

    # Datos de entrada
    x1 = float(input("Ingrese x1: "))
    y1 = float(input("Ingrese y1: "))
    x2 = float(input("Ingrese x2: "))
    y2 = float(input("Ingrese y2: "))

    rendimiento = float(input("Ingrese rendimiento (km/l): "))
    velocidad = float(input("Ingrese velocidad (km/h): "))

    # Integrante A: cálculo de distancia
   distacia = calcular_distancia(x1,y1,x2,y2)

    # Integrante B: cálculo de combustible


    # Integrante C: cálculo del tiempo estimado (ETA)
    eta = calcular_eta(distancia, velocidad)

    # Resultados
    print("\n--- RESULTADOS ---")
    print(f"Distancia: {distancia:.2f} km")
    print(f"Combustible estimado: {combustible:.2f} litros")
    print(f"Tiempo estimado de llegada: {eta:.2f} horas")


if __name__ == "__main__":
    main()