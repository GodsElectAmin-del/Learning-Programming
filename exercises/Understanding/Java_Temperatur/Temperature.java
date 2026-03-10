public class Temperature{
    private double celsius;

    public Temperature(double celsius){
        this.celsius = celsius;
    }
    public void setCelsius(double celsius) {
        this.celsius = (celsius - 32)*(5.0/9.0) ;
    }
    public double getcelsius() {
        return this.celsius;
    }
    public void myTemperature(double celsius){
      // this.celsius = (this.celsius - 32)*(5/9) ;
    }
    
}

// TODO i think this is a Fahrenheit to Celcius calculator