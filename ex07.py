import threading
import requests
import time as sleep

link1 = 'https://drive.google.com/uc?export=download&id=13xQP3BrWiZw3Q2Iqe3-mvlX7Q5lFh-dT'
link2 = 'https://drive.google.com/uc?export=download&id=12gyh5rrdk1gunZlDi1AFR4mE6fdG8kZI'
link3 = 'https://drive.google.com/uc?export=download&id=1kBmFOGrMC38_p96OptMMpyeMJmrQ_H2D'
link4 = 'https://drive.google.com/uc?export=download&id=1qHs_eqGr3hNFr7FdaY5VAD07O0kYA9Tj'
link5 = 'https://drive.google.com/uc?export=download&id=1CbHJT38BtLFtR2zOe2ZlDQRP5bxBL2B1'
link6 = 'https://drive.google.com/uc?export=download&id=14p3p4p8D4jvEH2hwvvc_DdpMrKpLOT45'



nome_arq = ''

def get_link(link, nome_arq):
    try: 
        response = requests.get(link)
        response.raise_for_status()

        with open(nome_arq, 'wb') as arq:
            arq.write(response.content)
        print(f'Arquivo {nome_arq} baixado com sucesso!')
    except requests.exceptions.RequestException as e:
        print(e)

t1 = threading.Thread(target=get_link, args=(link1, 'pesquisa.pdf'))
t2 = threading.Thread(target=get_link, args=(link2,'p2.pdf'))
t3 = threading.Thread(target=get_link, args=(link2,'p3.pdf'))

t1.start()
t2.start()
t3.start()