#Libraries

import argparse

#Public

class ArgparseHandler:
    '''
    Classe responsável por gerenciar os argumentos no CLI.
    '''

    #Constructor

    def __init__(self):

        self._parser = argparse.ArgumentParser()

        self._define_all_arguments()

    #Implementation

    def _define_all_arguments(self):

        self._parser.add_argument(
            '-i', 
            '--Initial', 
            help = 'Define the initial interation cicle value',
            required = False
        )

    def get_arguments_dict(self):

        return self._parser.parse_args().__dict__