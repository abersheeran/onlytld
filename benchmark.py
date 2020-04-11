import time

from onlytld import get_tld


def main():
    time.perf_counter_ns()
    for num in range(10 ** 6):
        get_tld(f"{num}.cn")
    time_count = time.process_time_ns()
    print(time_count / 10 ** 9)


if __name__ == "__main__":
    main()
