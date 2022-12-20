import json
from pathlib import Path

from fib import fib
import pytest
import time

NAME_FILE = "logs.json"

def test_fib_10():
    if Path(NAME_FILE).exists():
        with open(NAME_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    start = time.time()
    _ = fib(10)
    end = time.time()
    name_file = Path(__file__).name
    data.append({
        "name": f"{name_file}::{test_fib_10.__name__}",
        "unit": "seconds",
        "value": f"{end - start}",
    })
    with open(NAME_FILE, "w") as f:
        json.dump(data, f, indent=4)


def test_fib_20():
    if Path(NAME_FILE).exists():
        with open(NAME_FILE,
                  "r") as f:
            data = json.load(f)
    else:
        data = []
    start = time.time()
    _ = fib(10)
    end = time.time()
    name_file = Path(__file__).name
    data.append({
        "name": f"{name_file}::{test_fib_20.__name__}",
        "unit": "seconds",
        "value": f"{end - start}",
    })
    with open(NAME_FILE,
              "w") as f:
        json.dump(data,
                  f,
                  indent=4)
