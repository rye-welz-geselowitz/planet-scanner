from scanner import Scanner
from utils import await_valid_input, clear, prompt_credentials, print_cyan
from password import PASSWORD
from time import sleep

MAIN_MENU_TITLE = 'Scan Nearest Planet For: '
SCAN_SECONDS = 60 * 3

WATER_DESCRIPTION = (
    'Scan planetary surface for sources of liquid water (or appropriate chemical '
    'substitutes as per the Council For Human Adaptability of X982). May '
    'detect exposed bodies of water whose circumference exceeds approximately '
    ' (112 / x) where x is the machine\'s Adjusted Scanning Sensitivity Factor. '
    'Less reliably, may register groundwater at less than 10 hectares below '
    'the planetary surface, or regions dense with phytotelmata.'
)

FUEL_DESCRIPTION = (
    'Scan planetary surface for geological signatures associated with deposits '
    'of E77-compatible fuel sources including tylium and dilithium. Tylium '
    'detection yields high rate of false positives '
    '(nearly 20% for scans performed with SSF<2); results should be '
    'interpreted with caution.'
)

LIFE_DESCRIPTION = (
    'Lower sensitivity scans detects thermal activity patterns consistent with '
    'Chifoilisk\'s "Universal Guidelines For the Detection of "Animal" Life" '
    '(X972). Higher sensitivity scans (exceeding SSF=2) apply the more '
    'resource-intensive approach outlined by Mitis (X974), yielding a 65% '
    'increase in the detection of non-"animal" life.'
)


SCANNERS = [
    Scanner(
        'Water',
        WATER_DESCRIPTION,
        [
            [
                'non-sensitive item 1',
                'non-sensitive item 2',
                'non-sensitive item 3'
            ],
            [
                'sensitive item 1',
                'sensitive item 2',
                'sensitive item 3'
            ],
        ],
        SCAN_SECONDS
    ),
    Scanner(
        'Fuel',
        FUEL_DESCRIPTION,
        [
            [
                'non-sensitive item 1',
                'non-sensitive item 2',
                'non-sensitive item 3'
            ],
            [
                'sensitive item 1',
                'sensitive item 2',
                'sensitive item 3'
            ],
        ],
        SCAN_SECONDS
    ),
    Scanner(
        'Life',
        LIFE_DESCRIPTION,
        [
            [
                'non-sensitive item 1',
                'non-sensitive item 2',
                'non-sensitive item 3'
            ],
            [
                'sensitive item 1',
                'sensitive item 2',
                'sensitive item 3'
            ],
        ],
        SCAN_SECONDS
    ),
]

def display_main_menu(state):
    label_to_scanner={
        str(i):scanner for i, scanner in enumerate(SCANNERS, start=1)
    }
    while True:
        print(MAIN_MENU_TITLE.upper())
        print()
        for label, scanner in label_to_scanner.items():
            print_cyan(f'({label}) {scanner.get_menu_item_label()}')
        print()
        await_valid_input(
            'ENTER SELECTION',
            sorted([k for k in label_to_scanner.keys()]),
            lambda label: label_to_scanner[label].initiate_scan(state)
        )

def main():
    state = {'is_logged_in': False, 'scans_completed': 0}
    clear()
    prompt_credentials(state, PASSWORD, on_success=lambda:display_main_menu(state), on_fail=lambda: main())


if __name__ == "__main__":
    main()
