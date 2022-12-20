window.BENCHMARK_DATA = {
  "lastUpdate": 1671548660418,
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
      },
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
          "id": "8a4450a80ff0f9e5f23a11904be0eb1c282256bf",
          "message": "fix minimal 3",
          "timestamp": "2022-12-20T16:03:52+01:00",
          "tree_id": "810fc9f5678d674552088ad31ef49ea52b72f063",
          "url": "https://github.com/Lookatator/github-action-benchmark/commit/8a4450a80ff0f9e5f23a11904be0eb1c282256bf"
        },
        "date": 1671548658347,
        "tool": "pytest",
        "benches": [
          {
            "name": "bench.py::test_fib_10",
            "value": 52759.59984638623,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013935989402536079",
            "extra": "mean: 18.95389659723689 usec\nrounds: 25773"
          },
          {
            "name": "bench.py::test_fib_20",
            "value": 433.44830544607106,
            "unit": "iter/sec",
            "range": "stddev: 0.00001709414457561447",
            "extra": "mean: 2.3070801925753943 msec\nrounds: 431"
          }
        ]
      }
    ]
  }
}