from unittest.mock import MagicMock

import main


def test_integration():
    result = main.run(main.fetch, main.process)
    assert result == [1, 4, 9], f"actual {result=}"


def test_unit(_mocked_fetch=None, _mocked_process=None):
    fetch_mock = MagicMock(return_value=[1, 1, 1])
    process_mock = MagicMock(return_value=[2, 2, 2])

    result = main.run(fetch_mock, process_mock)

    # Assertations
    fetch_mock.assert_called_with()
    process_mock.assert_called_with([1, 1, 1])

    assert result == [2, 2, 2], f"actual {result=}"


if __name__ == "__main__":
    test_integration()
    test_unit()
