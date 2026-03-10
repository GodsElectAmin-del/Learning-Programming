public class Temperature{
    private double celsius;

    public Temperature(double celsius){
        this.celsius = celsius;
    }
    public void setCelsius(double celsius) {
        if (celsius >= -273.5){
            this.celsius = celsius;
        }
        else{
            
        }
    }
    public double getcelsius() {
        return this.celsius;
    }

    
}

// TODO was funktioniert gerade nicht: Also, dass zu lösende Problem ist, das man 
//einen Wert einsetzen möchte mit set.celsius 
// TODO i think this is a Fahrenheit to Celcius calculator
//TODO es ist keine Fahrenheit converter, sondern soll verhindern, das Werte unter 273, t eingegeben werden

// TODO: Wert in Feld einsetzen, achso es sollen nur Sachen in Feld eingesetz werden die gröér -273.5 sind