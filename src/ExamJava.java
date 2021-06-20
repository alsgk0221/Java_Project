class Calc {
    int[] sumfunc(int[] score) {
        int[] tmp = {0, 0};
        for(int i : score) {
            tmp[0] += i;
        }
        tmp[1] = tmp[0]/score.length;
        return tmp;
    }
}



public class ExamJava {
    public static void main(String[] args) {
        int[] score = {70, 80, 60, 100};

        int[] res = new Calc().sumfunc(score);
        //System.out.println("총점은 " + res[0] + "이고 " + "평균은 " + res[1] + "입니다.");
        System.out.printf("총점은 %d이고 평균은 %d 입니다. \n", res[0], res[1]);
        System.out.printf("총점은 %d이고 평균은 %d 입니다.", res[0], res[1]);
    }
}