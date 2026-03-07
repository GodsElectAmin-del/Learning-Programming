package Java_Konstruktors2.Konstruktor_Overloading;

public class Main {
    public static void main(String[] args) {
        Book newBook1 = new Book("Bible", "God", 3000);
        Book newBook2 = new Book("How to win at live", "Elect");

        System.out.println(newBook1.information);
        System.out.println(newBook2.information);

    }
}
