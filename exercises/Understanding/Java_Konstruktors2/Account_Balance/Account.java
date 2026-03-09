package Account_Balance;

public class Account {
    double balance;

    public Account(double balance){
        this.balance = balance ;
    }
    
    public void setbalance(double balance){
        this.balance = balance;
    }
    public void deposit(int balance){
        this.balance = this.balance + balance;
    }

    public double getbalance(){
        return this.balance;
    }
}
