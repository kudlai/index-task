#!/usr/bin/env python

from storage import storage
import yaml
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cases", default="test_cases.yml",
                    help="Path to cases file")
args = parser.parse_args()
cases_file = args.cases

stor = storage()
with open(cases_file, "r") as f:
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
    elif operation == "gt":
        results = stor.get_nums_with_value_gt(case['value'])
    elif operation == "eq":
        results = stor.get_nums_with_value_eq(case['value'])
    elif operation == "between":
        results = stor.get_nums_with_value_between(case['low_value'], case['high_value'])

    time_end = time.time()
    op_time = time_end - time_start
    results = set(results)
    passed = True
    reason = ""

    if results != expected_results:
        passed = False
        reason += "Wrong results. "

    if op_time > time_limit:
        passed = False
        reason += "Time limit exceeded."

    print "Name: %s" % ( name )
    print "Time: %.3f / %.3f" % ( op_time, time_limit )
    print "Passed: %r" % ( passed )
    if not passed:
        print "Reason: %s" % ( reason )
        sys.exit(1)
