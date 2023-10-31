class Counter:
    def __init__(self):
        self.cnt = 0

    def print_cnt(self):
        print(self.cnt)
        return


if __name__ == "__main__":
    cnt_a = Counter()
    cnt_b = Counter()

    for _ in range(10):
        cnt_a.cnt += 1
        cnt_b.cnt += 1

    cnt_a.print_cnt()
    cnt_b.print_cnt()

