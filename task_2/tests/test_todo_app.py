import csv
import os
import datetime

from todo_app import STORAGE, addItem, deleteItem, doneItem, clearStorage

task1 = {"Item": "task 1", "Date": "Not completed yet"}
task2 = {"Item": "task 2", "Date": "Not completed yet"}
task3 = {"Item": "task 3", "Date": "Not completed yet"}
task4 = {"Item": "task 4", "Date": "Not completed yet"}


def test_addItem_deleteItem():
    addItem(task1)
    addItem(task2)

    with open(STORAGE) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        data_from_csv = list(rows)
    
    assert data_from_csv[0][0] == task1["Item"]
    assert data_from_csv[1][0] == task2["Item"]

    deleteItem(task1["Item"])
    deleteItem(task2["Item"])

    assert os.path.getsize(STORAGE) == 0


def test_addItem_doneItem_deleteItem():
    addItem(task3)
    addItem(task4)
    
    doneItem(task3["Item"])
    doneItem(task4["Item"])

    with open(STORAGE) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        data_from_csv = list(rows)

    assert data_from_csv[0][1] == datetime.datetime.today().strftime("%Y.%m.%d")
    assert data_from_csv[1][1] == datetime.datetime.today().strftime("%Y.%m.%d")

    clearStorage()
