import threading
import time

def texto(mensagem):
    for i in range(2):
        print(f'{mensagem}')
        time.sleep(4)

t1 = threading.Thread(target=texto, args=('Thread 1 trabalhando',))
t2 = threading.Thread(target=texto, args=('Thread 2 trabalhando',))

t1.start()
t2.start()