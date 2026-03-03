import java.util.*;
public class Main {
    public static void main(String[] args){
        // the logic to understanding commands
        TaskService service = new TaskService();
        TaskService newTask = new TaskService();
        TaskService newDone = new TaskService();
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter your command ");
        String command = myObj.nextLine();
        command.trim();
        String[] actions = command.split("\\s+");
        // i want to check the first word for the actions

        // TODO a loop that asked the user for a new promt after each entry
        while (!actions[0].equals("exit"))
        {
        if (actions[0] == "add"){
            newTask.addTask(command);
        }

        if (actions[0].equals("list")){
            service.listTasks();
        }

        if (actions[0].equals("exit")){

        }

        if (actions[0].equals("done")){

        }
    }


        // TODO split the word right and 
        //TODO if Befehele für den richtige nutzen des INputs

        // so we need to trim() ; dann we need to split it ; than we need to check what the left part is and if it is equal to an command
        // if it is equal to an command than we compile an response with the right Part of the output

    }
}

// TODO : User Input erlauben und diesen mit richtigen Commands verbinden
// TODO : Sinvolle Outputs
// TODO : Endlos Schleife die mit exit beendet wird