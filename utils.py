from os import system
from time import sleep

def _clean(string):
    return string.strip().lower()

INCORRECT_PASSWORD_MESSAGE = 'Unauthorized'
INCORRECT_PASSWORD_MESSAGE_DURATION_SECONDS = 2
CREDENTIALS_PROMPT = "Enter captain's override code to proceed"

def prompt_credentials(state, correct_password, on_success, on_fail):
    user_input = input(f'{CREDENTIALS_PROMPT.upper()}: ')
    if user_input==correct_password:
        state['is_logged_in']=True
        clear()
        on_success()
    else:
        clear()
        print(INCORRECT_PASSWORD_MESSAGE.upper())
        sleep(INCORRECT_PASSWORD_MESSAGE_DURATION_SECONDS)
        clear()
        on_fail()

def clear():
    system('clear')

def await_valid_input(prompt, valid_inputs, process_valid_input):
    while True:
        user_input = input(f'{prompt}: ')
        cleaned_input = user_input.strip().lower()
        if _clean(user_input) in [_clean(x) for x in valid_inputs]:
            clear()
            return process_valid_input(cleaned_input)
        else:
            print(f'Please enter valid input: {", ".join(valid_inputs)}')

def print_progress_bar(duration_seconds):
    l = 100
    # Initial call to print 0% progress
    _printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(list(range(0, l))):
        # Do stuff...
        sleep(duration_seconds / l)
        # Update Progress Bar
        _printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

def print_list(items):
    print('SCAN RESULTS')
    print('-------------------------------------------')
    for item in items:
        print(f'* {item}')
    print('-------------------------------------------')
    print()

# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def _printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
