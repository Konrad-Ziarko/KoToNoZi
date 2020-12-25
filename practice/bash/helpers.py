### helpers
import sys
import termios
import contextlib

def fill_in_basic_test(correct_answers, test_question, answer_line, n=3, normalize=True):
    print(test_question)
    for i in range(n):
        if normalize is False:
            print('This question is case sensitive!')
        print('Attempt [{}/{}]'.format(i, n))
        print(answer_line, end='\r', flush=True)
        print(answer_line.split('__')[0], end='')
        try:
            ans = input()
            if normalize is True:
                ans = ans.strip().lower().replace(' ', '')
            if ans in correct_answers:
                print('Correct !')
                break
        except(KeyboardInterrupt, EOFError):
            print()
            sys.exit(1)
    else:
        print('You failed! Correct answers:\n{}'.format(correct_answers))
        return 1
    return 0

@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)



