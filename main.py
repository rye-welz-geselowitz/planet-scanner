from scanner import Scanner
from utils import await_valid_input, clear, prompt_credentials
from password import PASSWORD
from time import sleep

INITIAL_LOGIN_PROMPT = 'Please log in.'
SCAN_SECONDS = 1


PLANT_LIFE_DATA = [
    {'name': 'banana', 'color': 'yellow', 'deliciousness': 'high' },
    {'name': 'apple', 'color': 'red', 'deliciousness': 'medium' },
    {'name': 'potato', 'color': 'poop-brown', 'deliciousness': 'v. low' },
]

ANIMAL_LIFE_DATA = [
    {'name': 'horse', 'color': 'red'},
    {'name': 'giraffe', 'color': 'green' },
    {'name': 'pony', 'color': 'poop-brown' },
]

SCANNERS = [
    Scanner('Animal Life', 'About to scan for animal life', ANIMAL_LIFE_DATA, SCAN_SECONDS),
    Scanner('Plant Life', 'Gonna scan for plant life!', PLANT_LIFE_DATA, SCAN_SECONDS),
]

def display_main_menu(state):
    label_to_scanner={
        str(i):scanner for i, scanner in enumerate(SCANNERS, start=1)
    }
    while True:
        for label, scanner in label_to_scanner.items():
            print(f'({label}) {scanner.name}')
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
