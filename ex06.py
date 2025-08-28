import threading
import time 


lock = threading.Lock()
def adiciona_list(lista_num: list):
    complemento = []
    for i in lista_num:
        with lock: 
            complemento.append(i) 
            print(i)
    

t1 = threading.Thread(target=adiciona_list, args=([1, 2, 3, 4],))
t2 = threading.Thread(target=adiciona_list, args=([5, 6, 7, 8],))


t1.start()
t2.start()

t1.join()
t2.join()
