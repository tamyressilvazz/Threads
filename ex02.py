import threading

def quadrado_numero(num):
    quadrado = num**2
    print(quadrado)

th1 = threading.Thread(target=quadrado_numero(2))
th2 = threading.Thread(target=quadrado_numero(10))

th1.start()
th2.start()

th1.join()
