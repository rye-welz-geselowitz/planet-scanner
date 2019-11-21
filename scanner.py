from utils import (
    await_valid_input,
    print_progress_bar,
    clear,
    print_list,
    prompt_credentials,
)
from time import sleep
from password import PASSWORD

CONTINUE_PROMPT = 'Are you sure you want to proceed?'
RETURN_TO_MAIN_MENU_INSTRUCTION = 'Press enter to main menu.'

class Scanner():
    def __init__(
        self,
        name,
        description,
        result_sets, # order these by sensitivity, least sensitive first, most sensitive last
        scan_seconds
    ):
        self.name=name
        self.description=description
        self.result_sets=result_sets
        self.scan_seconds=scan_seconds
        self.next_scan_sensitivity_level = 0

    def get_menu_item_label(self):
        return self.name if self.next_scan_sensitivity_level==0 else f'{self.name} (increased sensitivity)'

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
        print_list(self.result_sets[self.next_scan_sensitivity_level])
        # If our scanner has another, more sensitive result set available,
        # prepare to return it on the next scan. Otherwise stick with current
        # sensitivity level.
        if (self.next_scan_sensitivity_level + 1) < len(self.result_sets):
            self.next_scan_sensitivity_level+=1
        state['scans_completed']+=1
        if state['scans_completed']==1:
            state['is_logged_in'] = False
        _user_input = input(RETURN_TO_MAIN_MENU_INSTRUCTION)
        clear()
