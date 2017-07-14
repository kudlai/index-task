#!/usr/bin/env python

from storage import storage
import yaml
import time
import sys

stor = storage()
with open("test_cases.yml", "r") as f:
    cases = yaml.load(f)

for case in cases['cases']:
    for element in case['elements']:
        stor.add_element(element)
    name = case['name']
    time_limit = case['time_limit']
    operation = case['operation']
    expected_results = set(case['expected_nums'])
    time_start = time.time()
    if operation == "lt":
        results = stor.get_nums_with_value_lt(case['value'])

    time_end = time.time()
    op_time = time_end - time_start
    print op_time
    results = set(results)
    passed = True

    if results != expected_results:
        passed = False

    if op_time > time_limit:
        passed = False

    print "Name: %s" % ( name )
    print "Time: %.3f / %.3f" % ( op_time, time_limit )
    print "Passed: %r" % ( passed )
    if not passed:
        sys.exit(1)
