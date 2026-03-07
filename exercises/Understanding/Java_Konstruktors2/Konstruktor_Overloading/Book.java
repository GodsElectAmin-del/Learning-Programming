package Java_Konstruktors2.Konstruktor_Overloading;

public class Book {
    String title;
    String author;
    int pages;
    String information;

    public Book(String title, String author, int pages){
        this.title = title;
        this.author = author;
        this.pages = pages;
        this.information = "the title is " + title + " the Author is " + author + " the amount of pages are " + pages;
    }

    public Book(String title, String author){
        this.title = title;
        this.author = author;
        this.pages = 0;
        this.information = "the title is " + title + " the Author is " + author + " the amount of pages are " + pages;
    }
}

// learning: the stuff that system.out.println is a String the stuff is not saved as a int when using the infor, so you can build a string by adding ints
