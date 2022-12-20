window.BENCHMARK_DATA = {
  "lastUpdate": 1671547985979,
  "repoUrl": "https://github.com/Lookatator/github-action-benchmark",
  "entries": {
    "Python Benchmark with pytest-benchmark": [
      {
        "commit": {
          "author": {
            "email": "luca.grillotti@gmail.com",
            "name": "Luca Grillotti",
            "username": "Lookatator"
          },
          "committer": {
            "email": "luca.grillotti@gmail.com",
            "name": "Luca Grillotti",
            "username": "Lookatator"
          },
          "distinct": true,
          "id": "ccd98ff90d4c00d412049536e98e3076af2d8c46",
          "message": "fix minimal",
          "timestamp": "2022-12-20T15:52:38+01:00",
          "tree_id": "83691333a63269f8949565b2015a6c2bfc2a51ee",
          "url": "https://github.com/Lookatator/github-action-benchmark/commit/ccd98ff90d4c00d412049536e98e3076af2d8c46"
        },
        "date": 1671547983760,
        "tool": "pytest",
        "benches": [
          {
            "name": "bench.py::test_fib_10",
            "value": 57799.4501674196,
            "unit": "iter/sec",
            "range": "stddev: 4.969853773368373e-7",
            "extra": "mean: 17.301202642991232 usec\nrounds: 40485"
          },
          {
            "name": "bench.py::test_fib_20",
            "value": 476.94683007762177,
            "unit": "iter/sec",
            "range": "stddev: 0.000012250209629701159",
            "extra": "mean: 2.0966697689074754 msec\nrounds: 476"
          }
        ]
      }
    ]
  }
}