def fetch():
    return [1, 2, 3]


def process(data):
    return [each * each for each in data]


def run(fetch, process):
    data = fetch()
    return process(data)


if __name__ == "__main__":
    result = run(fetch, process)
    print(result)
