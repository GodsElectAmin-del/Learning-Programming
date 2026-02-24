class BankAccount {
  String ownerName;
  String accountNumber;
  double balance;

  public BankAccount(String ownerName, String accountNumber) {
    // TODO
    balance =0;
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
    System.out.println("The Account Owner is: " + ownerName);
    System.out.println("The Account Owners Balance is: " + balance );
  }

  public static void transfer(BankAccount from, BankAccount to, double amount) {
    // TODO
    // i need to check for Null Point exceptions
 

    if (from.withdraw(amount)){
      to.deposit(amount);
      System.out.println("The New Account balance of" + from.ownerName + "is " + from.balance);
      System.out.println("The New Account balance of" + to.ownerName + "is " + to.balance);
    }
    else {
      System.out.println("transfer faild! ");
    }
  }
}