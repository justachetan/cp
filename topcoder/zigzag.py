class ZigZag(object):

    def __init__(self):
        self.seq = None

    def longestZigZag(self, sequence):

        if len(sequence) == 1:
            return 1

        elif len(sequence) == 2:
            return 2

        # stores length of largest zigzag sequence till i
        lz_buf = [0] * len(sequence)
        # stores end index of largest zigzag sequence till i
        lz_last = [-1] * len(sequence)
        # stores second last index of largest zigzag sequence till i
        lz_before_last = [-1] * len(sequence)

        flag = "+"  # indicates sign of last difference of the longest zigzag subsequence

        for i in range(len(sequence)):

            if i == 0:
                lz_buf[i] = 1
                lz_last[i] = 0
                lz_before_last[i] = 0

            else:

                diff = sequence[i] - sequence[lz_last[i - 1]]
                if diff == 0:
                    lz_buf[i] = lz_buf[i - 1]
                    lz_last[i] = lz_last[i - 1]
                    lz_before_last[i] = lz_before_last[i - 1]
                else:
                    if lz_buf[i - 1] == 1:
                        increment = True
                    else:
                        increment = (diff > 0 and flag ==
                                     "-") or (diff < 0 and flag == "+")

                    if increment:
                        lz_buf[i] = lz_buf[i - 1] + 1
                        lz_last[i] = i
                        lz_before_last[i] = lz_last[i - 1]
                        if diff < 0:
                            flag = "-"
                        elif diff > 0:
                            flag = "+"
                    else:
                        lz_buf[i] = lz_buf[i - 1]
                        lz_last[i] = lz_last[i - 1]
                        lz_before_last[i] = lz_before_last[i - 1]
        print(lz_buf, lz_last, lz_before_last)
        return lz_buf[-1]
if __name__ == '__main__':
    test = ZigZag()
    print(test.longestZigZag((1, 17, 5, 10, 13, 15, 10, 5, 16, 8)))
