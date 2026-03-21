public class fakultaet {
    public static void main(String[] args) {
        int fakultaet_5 = 1;
        for (int i = 5; i > 0;){
            fakultaet_5 = fakultaet_5 * i;
            i--;
        }

        System.out.println("The result is " + fakultaet_5);
        int fakultaet_6 = 6 * fakultaet_5;
        System.out.println("The result is " + fakultaet_6);
    }

    // solving fakulätt 6 mit fakultät 4
    
}
