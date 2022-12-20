import json
from pathlib import Path

from benchmarking_utils import Benchmarker
from fib import fib
import pytest
import time

NAME_FILE = "logs.json"

def test_fib_10():

    start = time.time()
    res = fib(10) / 3.
    end = time.time()

    Benchmarker.default().log_data_qdax(
        func=test_fib_10,
        timing=end - start,
        qd_score=res,
    )


def test_fib_20():
    start = time.time()
    res = fib(20)
    end = time.time()
    Benchmarker.default().log_data_qdax(
        func=test_fib_20,
        timing=end - start,
        qd_score=res,
    )

