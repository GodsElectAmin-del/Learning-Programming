public class Main {
  public static void main(String[] args) {
    // TODO: create 2 accounts
BankAccount AccountOne = new  BankAccount("Peter", "1");
BankAccount AccountTwo = new BankAccount("Max", "2");

AccountOne.deposit(100.0);
AccountTwo.deposit(10.0);

AccountOne.withdraw(5.0); // succesful withdraw
AccountTwo.withdraw(20.0); // unsuxesful withdraw 

BankAccount.transfer(AccountOne, AccountTwo, 50.0);
AccountOne.printSummary();
BankAccount.transfer(AccountTwo, AccountOne, 1000);
AccountTwo.printSummary();


    // TODO: deposits

    // TODO: withdrawals (one success, one fail)

    // TODO: transfers (one success, one fail)

    // TODO: print summaries along the way
  }
}
// This is my First Commit

// are the accounts there own Method