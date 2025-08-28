import threading

def message_1(m):
    print(m)

def message_2(m):
    print(m)

message_1 = threading.Thread(target=message_1, args=('Olá', 'thread!'))
message_2 = threading.Thread(target=message_2, args=('Olá', 'thread!'))

message_1.start()
message_2.start()

message_1.join()
