package TaskTracker;
import java.util.Scanner;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        TaskService service = new TaskService();
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter your Command");
       String command = null;
       String actualCommand = null;
       String theCommand;

    while (command == null || command != "exit" ){
        System.out.println("Enter your Command");
        command = myObj.nextLine();
        String trimeedCommand = command.trim();
        int myCommandIndex = trimeedCommand.indexOf(" ");
        if (myCommandIndex == -1){
            theCommand = trimeedCommand;
            //actualCommand = " ";
        }
        else{
            theCommand = trimeedCommand.substring(0, myCommandIndex);
            actualCommand = trimeedCommand.substring(myCommandIndex + 1);
        }
        if (theCommand.equals("add")) {
            service.addTask(actualCommand);
        }
        if (theCommand.equals("list")){
            service.listTask();
        }
        if (theCommand.equals("done")){
            try{
            int numActualCommand = Integer.parseInt(actualCommand);
            service.markDoneTask(numActualCommand);}
            catch (NumberFormatException e){
                System.out.println("you are slow!");
            }
        }
        if(theCommand.equals("exit")){
            break;
        } 
    }
    
}
}
// Learning variables alsways have to be decplared
//can be improved apprantly
// TODO when the slitting think gets a "-1" meaning there is " " space has to be understood