#Libraries

from logic.exit_handler import ExitHandler

from logic.game_manager import GameManager

from logic.argparse_handler import ArgparseHandler

from logic.initial_configuration import InitialConfiguration

#Main

game_manager = GameManager()

args_handler = ArgparseHandler()

initial_config = InitialConfiguration()

initial_config.set_new_cicle_number(
    args_handler.get_arguments_dict().get('Initial')
    )

exit_handler = ExitHandler()

while True:
    
    game_manager.click_rotation(initial_config.cicle_number)

    initial_config.next_cicle()

    if exit_handler.check():
        
        break