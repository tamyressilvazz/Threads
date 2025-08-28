import threading
import time

def conta_de_ate(inicio, fim):
    for i in range(inicio, fim):
        print(i)
        time.sleep(2.5)

    
th1 = threading.Thread(target=conta_de_ate, args=(1,1))
th2 = threading.Thread(target=conta_de_ate, args=(1,5))
th3 = threading.Thread(target=conta_de_ate, args=(2,1))
th4 = threading.Thread(target=conta_de_ate, args=(2,5))

th1.start()
th2.start()

#th3.join()
th4.start()
