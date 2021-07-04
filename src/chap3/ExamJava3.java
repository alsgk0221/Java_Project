package chap3;

import java.util.ArrayList;

public class ExamJava3 {
    public static void sam(int ... num) {
        for(int i : num) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        Person man1 = new Person("kim", 20);
        man1.setName("kim",20);
        System.out.println(man1);

        sam(10, 30, 20, 8, 9);

    }
}
