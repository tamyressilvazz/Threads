import threading
import time 

lock = threading.Lock()

def adiciona_list(lista_num: list, t: float):
    complemento = []
    for i in lista_num:
        with lock: 
            complemento.append(i) 
            print(complemento)
            time.sleep(t)
    

t1 = threading.Thread(target=adiciona_list, args=([1, 2, 3, 4], 1))
t2 = threading.Thread(target=adiciona_list, args=([5, 6, 7, 8], 0.03))


t1.start()
t2.start()
