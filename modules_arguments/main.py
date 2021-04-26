import data


def run(fetch, process):
    fetched = fetch()
    return process(fetched)


if __name__ == "__main__":
    result = run(data.fetch, data.process)
    print(result)
