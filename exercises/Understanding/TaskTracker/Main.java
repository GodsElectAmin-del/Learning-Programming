package TaskTracker;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Task newTask1 = new Task(1, "The War of Art");
        newTask1.markDone(true);
        System.out.println(newTask1);

        Task newTask2 = new Task(2, "Ein Gespür für Zahlen");
        newTask2.markDone(false);
        System.out.println(newTask2);
        
        TaskService service = new TaskService();
        service.addTask("Amazon Sci-Fi kucken ");
        service.listTask();
        
    }
    
}
//can be improved apprantly