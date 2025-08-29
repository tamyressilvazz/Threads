import threading
import queue
import time 

"""
produz números e coloca na fila, outra thread consome e imprime
"""
fila = queue.Queue()
default_p_c = ''

def produz_num(default_p_c, fila):
    for i in range(0,5):
        time.sleep(0.01)
        prod = i
        fila.put(prod)
        print(f'[{default_p_c}] produziu a peça: {prod}')
def consome_num(default_p_c, fila):
    while True:
        #recebe um item (o número produzido)
        cons = fila.get()
        print(f'[{default_p_c}] recebeu a peça: {cons}')
        #Marca como concluído (precisa no while)
        fila.task_done()
    

produtor = threading.Thread(target=produz_num, args=('Produtor', fila))
consumidor = threading.Thread(target=consome_num, args=('Consumidor', fila))

#start na thread do produtor e no consumidor
produtor.start()
consumidor.start()

#espera a thread terminar
#produtor.join()
#consumidor.join()

print('Finalizadas.')