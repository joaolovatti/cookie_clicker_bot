#Libraries

from logic.click_box import ClickBox

import pyautogui as pyauto

#Public

class GameManager:
    '''
    Controla a interação do BOT com o game.
    '''

    #Constructor

    def __init__(self):

        self._master_cookie = ClickBox(path = 'assets/cookie.png')

        self._wait_to_cursor_image_display()

        self._cursor = ClickBox(path = 'assets/cursor.png')

        self._store_item = ClickBox(coordenate = (
            self._cursor.coordenate[0] - 60,
            self._cursor.coordenate[1] - 120
        ))

        self._clicks_per_cicle = 100

    #Interface

    def click_rotation(self, initial_cicle = 0):
        '''
        Executa a seguinte sequência de cliques:

        1. Um número pré-estabelecido de cliques no cookie.

        2. Clique num item da store.

        3. Scroll para baixo. Clique em todos os itens de compra disponíveis.

        4. Scroll para cima. Clique em todos os itens de compra disponíveis.

        Argumentos:

        → initial_circle: Aumenta o período gasto na etapa "1".
        '''

        self._master_cookie.click(500 + initial_cicle * self._clicks_per_cicle)

        self._store_item.click(1) 

        pyauto.moveTo(
            x = self._cursor.coordenate[0],
            y = self._cursor.coordenate[1]
        )

        pyauto.scroll(-10)

        self._click_all_options()
                
        pyauto.scroll(10)

        self._click_all_options()

    #Implementation

    def _wait_to_cursor_image_display(self):

        self._master_cookie.click(2000)

    def _click_all_options(self):

        options = 13

        for i in range(0, options + 1):

            pyauto.click(
                clicks = 1, 
                x = self._cursor.coordenate[0], 
                y = self._cursor.coordenate[1] + 55 * (options - i) )