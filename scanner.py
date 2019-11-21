from utils import (
    await_valid_input,
    print_progress_bar,
    clear,
    print_table,
    prompt_credentials,
)
from time import sleep
from password import PASSWORD

CONTINUE_PROMPT = 'Are you sure you want to proceed?'
RETURN_TO_MAIN_MENU_INSTRUCTION = 'Press enter to main menu.'

class Scanner():
    def __init__(self, name, description, results, scan_seconds):
        self.name=name
        self.description=description
        self.results=results
        self.scan_seconds=scan_seconds

    def initiate_scan(self, state):
        if state['is_logged_in'] is True:
            print(self.description)
            await_valid_input(
                f'\n{CONTINUE_PROMPT}', ['Y','N'], lambda l: True if l.lower()=='n' else self.perform_scan(state)
            )
        else:
            prompt_credentials(
                state, PASSWORD, on_success=lambda: self.initiate_scan(state), on_fail=lambda: True
            )

    def perform_scan(self, state):
        print('Scanning')
        print_progress_bar(self.scan_seconds)
        clear()
        print_table(self.results)
        state['scans_completed']+=1
        if state['scans_completed']==1:
            state['is_logged_in'] = False
        _user_input = input(RETURN_TO_MAIN_MENU_INSTRUCTION)
        clear()
