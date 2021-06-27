class Calc:
    def __init__(self, s):
        self.s = s
        self.adding()

    def adding(self):
        self.tmp = [0, None]
        for i in self.s:
            self.tmp[0] += i
        self.tmp[1] = self.tmp[0]/len(self.s)
        return self.tmp


score = [70, 60, 80, 100]

res = Calc(score)
print("총점은 {0}이고 평균은 {1} 입니다.".format(res.tmp[0], res.tmp[1]))

