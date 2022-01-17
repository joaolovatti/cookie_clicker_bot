#Libraries

import keyboard

#Public

class ExitHandler:
    '''
    Gerencia a inativação do funcionamento do BOT.
    '''

    #Implementation

    def check(self):
        '''
        Avalia se deve inativar o BOT.
        '''

        return keyboard.is_pressed('q')