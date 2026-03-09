package Account_Balance;

public class Main {
    public static void main(String[] args) {
        Account newAccount = new Account(0.0);
        System.out.println("the starting Balance is " + newAccount.getbalance());
        newAccount.setbalance(10.0);
        System.out.println("the new Balance is " + newAccount.getbalance());
        newAccount.deposit(30);
        System.out.println("the real new Balance is " + newAccount.getbalance());
    }
}
