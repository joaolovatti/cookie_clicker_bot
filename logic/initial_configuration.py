#Libraries

#Public

class InitialConfiguration:
    '''
    Define as configurações iniciais para o funcionamento do BOT.
    '''

    #Constructor

    def __init__(self):

        self.cicle_number = 0

    #Interface

    def set_new_cicle_number(self, value):
        '''
        Define a quantidade inicial de tempo gasta no clique do cookie.
        '''

        if (value):

            self.cicle_number = int(value)

    def next_cicle(self):
        '''
        Autaliza a configuração para o próximo ciclo de cliques.
        '''

        self.cicle_number += 1