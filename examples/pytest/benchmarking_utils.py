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
    DEFAULT_NAME = "output"

    def __init__(self, name: str):
        if name is None:
            name = self.DEFAULT_NAME
        self.name = name
        self.path = Path(__file__).parent / self.name
        if self.path.suffix != ".json":
            self.path = self.path.with_suffix(".json")

    @classmethod
    def default(cls):
        return cls(name=cls.DEFAULT_NAME)

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
    def _dump_data(cls, data, path):
        with open(path,
                  "w") as f:
            json.dump(data,
                      f,
                      indent=4)

    def log(self, func, value, unit: str, name_extra=None):
        name = NameWrapper(func,
                           name_extra)

        data = self._load_data(self.path)

        data.append({
            "name": str(name),
            "unit": str(unit),
            "value": str(value),
        })

        self._dump_data(data,
                        self.path)

    @classmethod
    def add_name_component(self, name_component, name=None):
        if name is None:
            name = ""
        name += f" :: {name_component}"
        return name

    def add_timing(self, func, timing, name_extra=None):
        if name_extra is None:
            name_extra = self.add_name_component(name_extra, "Timing")
        self.log(func, -1. * timing, unit="(-1 * Seconds)", name_extra=name_extra)

    def add_qd_score(self, func, qd_score, name_extra=None):
        if name_extra is None:
            name_extra = self.add_name_component(name_extra, "QD Score")
        self.log(func, qd_score, unit="(QD Score)", name_extra=name_extra)

    def add_max_fitness(self, func, max_fitness, name_extra=None):
        if name_extra is None:
            name_extra = self.add_name_component(name_extra, "Max Fitness")
        self.log(func, max_fitness, unit="(Max Fitness)", name_extra=name_extra)

    def add_coverage(self, func, coverage, name_extra=None):
        if name_extra is None:
            name_extra = self.add_name_component(name_extra, "Coverage")
        self.log(func, coverage, unit="(Coverage)", name_extra=name_extra)

    def add_return_policy(self, func, return_policy, name_extra=None):
        if name_extra is None:
            name_extra = self.add_name_component(name_extra, "Return Policy")
        self.log(func, return_policy, unit="(Return)", name_extra=name_extra)



    def log_data_qdax(self,
                      func,
                      timing=None,
                      qd_score=None,
                      max_fitness=None,
                      coverage=None,
                      return_policy=None,
                      name_extra=None,
                      ):
        if timing is not None:
            self.add_timing(func, timing, name_extra=name_extra)
        if qd_score is not None:
            self.add_qd_score(func, qd_score, name_extra=name_extra)
        if max_fitness is not None:
            self.add_max_fitness(func, max_fitness, name_extra=name_extra)
        if coverage is not None:
            self.add_coverage(func, coverage, name_extra=name_extra)
        if return_policy is not None:
            self.add_return_policy(func, return_policy, name_extra=name_extra)


