public class fakultät_rekursive{
public static int fakultaetRekursiveCalc(int n) {
    if ( n == 0){
        return 1;
    }
    return n * fakultaetRekursiveCalc(n-1);
}
public static void main(String[] args) {
    int n = 5;
    int result = fakultaetRekursiveCalc(n);
    System.out.println("this is the result " + result);
}
}