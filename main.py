from scanner import Scanner
from utils import await_valid_input, clear, prompt_credentials
from password import PASSWORD
from time import sleep

INITIAL_LOGIN_PROMPT = 'Please log in.'
SCAN_SECONDS = 1


PLANT_LIFE_DATA = [
    'There is a yummy yellow banana',
    'There is a kinda mealy red apple',
    'I also found a delicious poop-brown potato!!!!'
]

ANIMAL_LIFE_DATA = [
    'There is a red horse',
    'There is a green giraffe',
    'I also found a beautiful poop-brown pony!!!!'
]

ANIMAL_LIFE_DATA_SENSITIVE = [
    'There is a red horse who is vegan',
    'There is a green giraffe who cries a lot',
    'I also found a beautiful poop-brown pony who is "nice"!!!!'
]

SCANNERS = [
    Scanner('Animal Life', 'About to scan for animal life', [ANIMAL_LIFE_DATA, ANIMAL_LIFE_DATA_SENSITIVE], SCAN_SECONDS),
    Scanner('Plant Life', 'Gonna scan for plant life!', [PLANT_LIFE_DATA], SCAN_SECONDS),
]

def display_main_menu(state):
    label_to_scanner={
        str(i):scanner for i, scanner in enumerate(SCANNERS, start=1)
    }
    while True:
        for label, scanner in label_to_scanner.items():
            print(f'({label}) {scanner.get_menu_item_label()}')
        await_valid_input(
            '\nScan for',
            sorted([k for k in label_to_scanner.keys()]),
            lambda label: label_to_scanner[label].initiate_scan(state)
        )

def main():
    state = {'is_logged_in': False, 'scans_completed': 0}
    clear()
    prompt_credentials(state, PASSWORD, on_success=lambda:display_main_menu(state), on_fail=lambda: main())


if __name__ == "__main__":
    main()
