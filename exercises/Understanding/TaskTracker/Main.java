package TaskTracker;
import java.util.Scanner;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        /* 
        Task newTask1 = new Task(1, "The War of Art");
        newTask1.markDone(true);
        System.out.println(newTask1);

        Task newTask2 = new Task(2, "Ein Gespür für Zahlen");
        newTask2.markDone(false);
        System.out.println(newTask2);
        */
        TaskService service = new TaskService();
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter your Command");
        //String command = myObj.nextLine();
       String command = null;
       // String trimeedCommand = command.trim();
       // int myCommandIndex = trimeedCommand.indexOf(" ");
       // String theCommand = trimeedCommand.substring(0, myCommandIndex);
       // String actualCommand = trimeedCommand.substring(myCommandIndex + 1);
        /* 
        if (myCommandIndex != -1){
            String theCommand = trimeedCommand.substring(0, myCommandIndex);
            String actualCommand = trimeedCommand.substring(myCommandIndex + 1);
        }
            */
    while (command == null || command != "exit" ){
        System.out.println("Enter your Command");
        command = myObj.nextLine();
        String trimeedCommand = command.trim();
        int myCommandIndex = trimeedCommand.indexOf(" ");
        String theCommand = trimeedCommand.substring(0, myCommandIndex);
        String actualCommand = trimeedCommand.substring(myCommandIndex + 1);
        if (theCommand.equals("add")) {
            service.addTask(actualCommand);
        }
        if (trimeedCommand.equals("list")){
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
        

    }
    
}
}
//can be improved apprantly
// TODO when the slitting think gets a "-1" meaning there is " " space has to be understood