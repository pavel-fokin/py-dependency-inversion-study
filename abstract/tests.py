import main


class MockFetcher(main.AbstractFetcher):
    def fetch(self) -> list:
        return [2, 3, 4]


class MockProcessor(main.AbstractProcessor):
    def process(self, data: list) -> list:
        return [2, 3, 4]


def test_integration():
    script = main.Script(main.Fetcher(), main.Processor())
    result = script.run()
    assert result == [1, 4, 9], f"actual {result=}"


def test_unit(_mocked_fetch=None, _mocked_process=None):
    script = main.Script(MockFetcher(), MockProcessor())
    result = script.run()
    assert result == [2, 3, 4], f"actual {result=}"


if __name__ == "__main__":
    test_integration()
    test_unit()
