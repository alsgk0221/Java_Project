package chap2;

class Algo {
    String[] d;
    int[] score;
    int[] tmp = new int[2];
    Algo(String[] d, int[] score) {
        this.d = d;
        this.score = score;
    }

    String[] swap() {
        String temp = d[0];
        d[0] = d[1];
        d[1] = temp;
        return d;

    }

    int[] sumFunc() {
        for(int i : score) {
            tmp[0] += i;
        }
        tmp[1] = tmp[0]/score.length;
        return tmp;
    }
}

public class ExamJava2 {
    public static void main(String[] args) {
        String[] data = {"식초", "식용유"};
        int[] score = {70, 80, 60, 100};
        Algo res = new Algo(data, score);
        res.swap();
        System.out.println(res.d[0] + "," + res.d[1]);
        res.sumFunc();
        System.out.println("합계 : " + res.tmp[0]);
    }
}

