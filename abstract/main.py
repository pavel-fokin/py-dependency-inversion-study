from typing import Iterable


class AbstractFetcher:
    def fetch(self) -> Iterable:
        raise NotImplementedError


class AbstractProcessor:
    def process(self, data: Iterable) -> Iterable:
        raise NotImplementedError


class Fetcher(AbstractFetcher):
    def fetch(self) -> list:
        return [1, 2, 3]


class Processor(AbstractProcessor):
    def process(self, data: list):
        return [each * each for each in data]


class Script:
    def __init__(self, fetcher: AbstractFetcher, processor: AbstractProcessor):
        self.fetcher = fetcher
        self.processor = processor

    def run(self):
        data = self.fetcher.fetch()
        return self.processor.process(data)


if __name__ == "__main__":
    fetcher = Fetcher()
    processor = Processor()

    script = Script(fetcher, processor)
    result = script.run()
    print(result)
