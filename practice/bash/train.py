#!/usr/bin/env python3
import os
import sys
import json
from time import time
from importlib import import_module
from inspect import getmembers, isfunction

MODULES_TO_TEST = ['bash_tests']

class TestResult:
    def __init__(self, name, total=0, failed=0, suc_streak=0, last_done=0):
        self.name = name
        self.total = total
        self.failed = failed
        self.suc_streak = suc_streak
        self.last_done = last_done

    def add_suc(self):
        self.last_done=int(time())
        self.total+=1
        self.suc_streak+=1

    def add_fail(self):
        self.last_done=int(time())
        self.failed+=1
        self.suc_streak=0

    def to_dict(self):
        return {'total': self.total, 'failed': self.failed, 'suc_streak': self.suc_streak, 'last_done': self.last_done }

if __name__ == "__main__":
    ret = 0
    results=dict()
    try:
        with open('train.db', 'r') as file_obj:
            history = json.load(file_obj)
    except:
        history = None
    print(chr(27) + "[2J")
    for module_name in MODULES_TO_TEST:
        module = import_module(module_name)
        functions_list = [o for o in getmembers(module, isfunction) if o[0].startswith('ktz_')]
        for fun in functions_list:
            if history is not None:
                result_obj=TestResult(fun[0], history[fun[0]]['total'], history[fun[0]]['failed'], history[fun[0]]['suc_streak'], history[fun[0]]['last_done'])
            else:
                result_obj=TestResult(fun[0])
            ret = fun[1]()
            if ret != 0:
                result_obj.add_fail()
            else:
                result_obj.add_suc()
            results['{}'.format(fun[0])] = result_obj.to_dict()
            print()
    with open('train.db', 'w') as file_obj:
        json.dump(results, file_obj)

