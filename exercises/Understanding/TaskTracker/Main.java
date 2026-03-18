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
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter your Command");
        String command = myObj.nextLine();
        String trimeedCommand = command.trim();
        String myCommand = trimeedCommand.indexOf(" ");
        If (myCommand != -1);{
            String theCOmmand = input.substring(0, myCommand);
            String actualCommand = input.substring(myCommand + 1);
        }
        // using indexOf and substring


       // Service.addTask(myObj);
        TaskService service = new TaskService();
        service.addTask("Amazon Sci-Fi kucken ");
        service.addTask("The Wolf of Wall Street");
        service.findById(1);
        service.listTask();
        service.findById(1);
        service.markDoneTask(1);
        service.markDoneTask(2);
        service.listTask();

    }
    
}
//can be improved apprantly