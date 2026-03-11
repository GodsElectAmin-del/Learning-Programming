package PassWort;

public class Main {
    public static void main(String[] args) {
        Password newUser = new Password("Peter", "1234$ACAb");
        newUser.setUsername("Miles Morales ");
        newUser.changePassword("1234$ACAb", "12345");
        System.out.println(newUser.password + " has as Username "+ newUser.username);
    }
    
}
