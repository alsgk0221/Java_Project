class Calc:

    def sumfunc(self, score):
        tmp = [0, None]
        for i in score:
            tmp[0] += i
        tmp[1] = tmp[0]/len(score)
        return tmp


score = [70, 60, 80, 100]
res = Calc().sumfunc(score)
print("총점은 {0}이고 평균은 {1} 입니다.".format(res[0], res[1]))