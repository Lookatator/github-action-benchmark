import json
from pathlib import Path


class NameWrapper:
    """
    This class is copied from pytest-benchmark.
    """

    def __init__(self, target, name_extra=None):
        self.target = target
        self.name_extra = name_extra

    def __str__(self):
        name = (self.target.__module__ + "::") if hasattr(self.target, '__module__') else ""
        name += self.target.__name__ if hasattr(self.target, '__name__') else repr(self.target)
        name += ("::" + self.name_extra) if self.name_extra is not None else ""
        return name

    def __repr__(self):
        return f"NameWrapper({repr(self.target)})"


class Benchmarker:

    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit
        self.path = Path(__file__).parent / self.name
        if self.path.suffix != ".json":
            self.path = self.path.with_suffix(".json")

    @classmethod
    def _load_data(cls, path):
        if Path(path).exists():
            with open(path,
                      "r") as f:
                data = json.load(f)
        else:
            data = []
        return data

    @classmethod
    def log_data(cls, func, value, unit, path, name_extra=None):
        name = NameWrapper(func, name_extra)

        data = cls._load_data(path)

        data.append({
            "name": str(name),
            "unit": str(unit),
            "value": str(value),
        })

        cls._dump_data(data, path)

    @classmethod
    def _dump_data(cls, data, path):
        with open(path,
                  "w") as f:
            json.dump(data,
                      f,
                      indent=4)

    def log(self, func, value, name_extra=None):
        self.log_data(func, value, self.unit, self.path, name_extra=name_extra)


# Defining benchmarking objects
benchmarker_timing = Benchmarker(name="timing", unit="seconds")
benchmarker_qd_score = Benchmarker(name="qd_score", unit="QD Score")
benchmarker_max_fitness = Benchmarker(name="max_fitness", unit="Max Fitness")
benchmarker_coverage = Benchmarker(name="coverage", unit="Coverage")
benchmarker_return_policy = Benchmarker(name="return", unit="Return")


def log_data_qd_algorithm(func,
                          timing=None,
                          qd_score=None,
                          max_fitness=None,
                          coverage=None,
                          return_policy=None,
                          name_extra=None):
    if timing is not None:
        benchmarker_timing.log(func, timing, name_extra=name_extra)
    if qd_score is not None:
        benchmarker_qd_score.log(func, qd_score, name_extra=name_extra)
    if max_fitness is not None:
        benchmarker_max_fitness.log(func, max_fitness, name_extra=name_extra)
    if coverage is not None:
        benchmarker_coverage.log(func, coverage, name_extra=name_extra)
    if return_policy is not None:
        benchmarker_return_policy.log(func, return_policy, name_extra=name_extra)

