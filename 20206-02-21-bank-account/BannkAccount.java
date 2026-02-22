class BankAccount {
  String ownerName;
  String accountNumber;
  double balance;

  public BankAccount(String ownerName, String accountNumber) {
    // TODO
    balance = 0.0;
    this.ownerName = ownerName;
    this.accountNumber = accountNumber; 
  }

  public void deposit(double amount) {
    // TODO
    if (amount <= 0){
        System.err.println("ERROR");
    }
    else {
        balance += amount;
    }
  }

  public boolean withdraw(double amount) {
    // TODO
    if (amount <= 0 || amount > balance ){
        System.err.println("ERROR");
        return false;
    }
    else{
        balance -= amount;
        return true;
    }
  }

  public double getBalance() {
    // TODO
    return balance;
  }

  public void printSummary() {
    // TODO
    System.err.println("The Account Owner is: " + ownerName);
    System.err.println("The Account Owners Balance is: " + balance );
  }

  public static void transfer(BankAccount from, BankAccount to, double amount) {
    // TODO
  }
}