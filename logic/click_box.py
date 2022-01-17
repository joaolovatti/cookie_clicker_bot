#Libraries

import pyautogui as pyauto

#Public

class ClickBox:
    '''
    Classe responsável por representar um box que será clickado pelo BOT.
    '''

    #Constructor
    
    def __init__(self, path = '', coordenate = (0, 0)):
        '''
        → path: Path da imagem do elemento que deseja identificar na imagem.
                Esse valor possui preferência na construção do ClickBox.

        → coordenate: Coordenadas na tela.
        '''
        
        if (path != ''):
        
            self.coordenate = pyauto.locateCenterOnScreen(
                path,
                confidence = 0.8
            )
        
        elif (coordenate != (0, 0)):
            
            self.coordenate = coordenate

    #Interface
        
    def click(self, n):
        '''
        Define a quanidade de cliques no elementos.

        Argumentos:

        → n: Número de cliques.
        '''
        
        pyauto.click(clicks = n,
                     interval = 0.005,
                     x = self.coordenate[0],
                     y = self.coordenate[1]
                    )