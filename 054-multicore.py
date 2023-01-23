from multiprocessing import Process,Queue

# defino una función que cuesta de calcular
def calculaCosas(nombre):
    print("soy el proceso "+nombre )
    i = 1.000000054
    for j in range(0,100000000):
        i = i*1.000000543
    print("ya he finalizado")

# punto de entrada de ejecución de la aplicación
if __name__ == "__main__":
    print("comienza la ejecución")
    # creo una cola de procesos
    coladeproceso = Queue()
    # creo una lista de procesos
    procesos = []
    # atrapo el número de núcleos que tengo
    numerodenucleos = 64
    # creo una piscina de procesos
    for i in range(0,numerodenucleos):
        procesos.append(Process(target = calculaCosas,args=("hola",)))

    for i in range(0,numerodenucleos):
        procesos[i].start()

    for i in range(0,numerodenucleos):
        procesos[i].join()
        
    
    

