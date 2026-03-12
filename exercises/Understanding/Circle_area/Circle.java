package Circle_area;

public class Circle {
   public static final double PI = 3.141592653589793;
   double radius;
   double area;

   public Circle(double radius){
    this.radius = radius;
    // this.area = radius * radius * PI;
   }

   public void area_calc(){
    this.area = this.radius*this.radius * PI;
   }
   public double area(){
    return this.area;
   } 
}
