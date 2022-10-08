from data_aggregation import process_data
import json


def test_process_data_1():
    result = {"Canada": {"people": ["John", "Sam", "Alex", "Bob", "Sue", "Rick", "George"], "count": 7}}
    assert json.loads(process_data('data/test1.csv')) == result


def test_process_data_2():
    result = {"Hungary": {"people": ["Ervin"], "count": 1}}
    assert json.loads(process_data('data/test2.csv')) == result


def test_process_data_3():
    result = {"Country1": {"people": ["Name1", "Name2", "Name3"], "count": 3},
              "Country2": {"people": ["Name4", "Name5", "Name6", "Name7", "Name8"], "count": 5},
              "Country3": {"people": ["Name9"], "count": 1}}
    assert json.loads(process_data('data/test3.csv')) == result


def test_process_data_4():
    result = "File is empty"
    assert process_data('data/test4.csv') == result
