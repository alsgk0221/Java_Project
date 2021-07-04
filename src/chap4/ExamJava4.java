package chap4;

class Animal {
    protected String name;
    Animal(String name) {
        this.name = name;
    }
    public void move() {
        System.out.printf("%s가 움직인다.",this.name);
    }
}

class Bird extends Animal {
    int legs;

    Bird(String name, int legs) {
        super(name);
        this.legs = legs;
    }

    public void legsNum() {
        System.out.printf("다리 개수 : ", this.legs);
    }

}





public class ExamJava4 {
    public static void main(String[] args) {
        Bird b1 = new Bird("참새", 2);
        b1.move();
        System.out.println(b1.name);

    }
}
