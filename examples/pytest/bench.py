import json
from pathlib import Path

from benchmarking_utils import log_data_qd_algorithm
from fib import fib
import pytest
import time

NAME_FILE = "logs.json"

def test_fib_10():

    start = time.time()
    res = fib(10)
    end = time.time()

    log_data_qd_algorithm(
        func=test_fib_10,
        timing=end - start,
        qd_score=res,
    )


def test_fib_20():
    start = time.time()
    res = fib(10)
    end = time.time()
    log_data_qd_algorithm(
        func=test_fib_20,
        timing=end - start,
        qd_score=res,
    )

