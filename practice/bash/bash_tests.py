from helpers import *

def ktz_test_file():
    correct_answers = ['-f', '-e']
    test_question='[TB101]How to check if file exists?'
    answer_line = 'Fill in the blank `[ __ /path/to/file ]`\r'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_test_directory():
    correct_answers = ['-d']
    test_question = '[TB102]How to check if directory exists?'
    answer_line = 'Fill in the blank `[ __ /path/to/directory.d ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_test_file_not_empty():
    correct_answers = ['-s']
    test_question = '[TB103]How to check if file exists and is not empty?'
    answer_line = 'Fill in the blank `[ __ /path/to/file ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_test_file_executable():
    correct_answers = ['-x']
    test_question = '[TB104]How to check if file is executable by you?'
    answer_line = 'Fill in the blank `[ __ /path/to/file ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_test_file_writable():
    correct_answers = ['-w']
    test_question = '[TB105]How to check if file is writable by you?'
    answer_line = 'Fill in the blank `[ __ /path/to/file ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_test_file_owned():
    correct_answers = ['-O']
    test_question = '[TB106]How to check if file is owned by you?'
    answer_line = 'Fill in the blank `[ __ /path/to/file ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line, normalize=False)

def ktz_test_file_group_owned():
    correct_answers = ['-G']
    test_question = '[TB107]How to check if file is owned by your group?'
    answer_line = 'Fill in the blank `[ __ /path/to/file ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line, normalize=False)

def ktz_compare_newer_than():
    correct_answers = ['-nt']
    test_question = '[TB121]How to compare if file is newer than other file?'
    answer_line = 'Fill in the blank `[ /path/to/file1 ____ /path/to/file2 ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_compare_older_than():
    correct_answers = ['-ot']
    test_question = '[TB122]How to compare if file is older than other file?'
    answer_line = 'Fill in the blank `[ /path/to/file1 ____ /path/to/file2 ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_compare_empty_string():
    correct_answers = ['-z']
    test_question = '[TB123]How to check if string is empty?'
    answer_line = 'Fill in the blank `[ __ "${variable}" ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_compare_nonempty_string():
    correct_answers = ['-n']
    test_question = '[TB124]How to check if string is not empty?'
    answer_line = 'Fill in the blank `[ __ "${variable}" ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_compare_same_string():
    correct_answers = ['==']
    test_question = '[TB125]How to check if strings are the same?'
    answer_line = 'Fill in the blank `[ "${variable1}" __ "${variable2}" ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_compare_different_string():
    correct_answers = ['!=']
    test_question = '[TB126]How to check if strings are not the same?'
    answer_line = 'Fill in the blank `[ "${variable1}" __ "${variable2}" ]`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)







def ktz_bash_emacs_start_of_the_line():
    correct_answers = ['ctrl+a']
    test_question = '[TB214]How to got to the beginnig of the command prompt?'
    answer_line = '`really long command and you want to go and add sudo ______`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_bash_emacs_end_of_the_line():
    correct_answers = ['ctrl+e']
    test_question = '[TB215]How to got to the end of the command prompt?'
    answer_line = '`______ really long command and you want to go add new argument`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_bash_emacs_forward_word():
    correct_answers = ['alt+f']
    test_question = '[TB216]How to got to the end of the next word?'
    answer_line = '`really long command and _____ want to go one word forward`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

def ktz_bash_emacs_back_word():
    correct_answers = ['alt+b']
    test_question = '[TB116]How to got to the beggining of the previous word?'
    answer_line = '`really long command and _____ want to go one word back`'
    return fill_in_basic_test(correct_answers, test_question, answer_line)

