from unittest.mock import patch

from main import run


def test_integration():
    result = run()
    assert result == [1, 4, 9], f"actual {result=}"


@patch("data.process", return_value=[2, 2, 2])
@patch("data.fetch", return_value=[1, 1, 1])
def test_unit(fetch_mock=None, process_mock=None):
    result = run()

    fetch_mock.assert_called_with()
    process_mock.assert_called_with([1, 1, 1])

    assert result == [2, 2, 2], f"actual {result=}"


if __name__ == "__main__":
    test_integration()
    test_unit()
