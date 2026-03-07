package Java_Konstruktors2.Konstruktor_Validation;

public class Rectangle {
    double width;
    double height;
    double area;

    public Rectangle(double width, double height){
            this.area = Math.sqrt((width * height)*(width * height));
    }

}
