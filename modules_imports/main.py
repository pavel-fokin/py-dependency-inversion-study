import data


def run():
    fetched = data.fetch()
    return data.process(fetched)


if __name__ == "__main__":
    result = run()
    print(result)
