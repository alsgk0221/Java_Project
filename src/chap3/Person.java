package chap3;

public class Person {
    private String name;
    private int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "chap3.Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
