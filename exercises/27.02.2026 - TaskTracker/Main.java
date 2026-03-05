import java.util.*;
public class Main {
    public static void main(String[] args){
        // the logic to understanding commands
        TaskService service = new TaskService();
        Scanner myObj = new Scanner(System.in);


        // TODO a loop that asked the user for a new promt after each entry
        while (true )
        {
        System.out.println("Enter your command ");
        String command2 = myObj.nextLine();
        command2 = command2.trim();
        String[] actions2 = command2.split("\\s+");
        
        if (actions2[0].equals("exit")){
            break;
        }

        if (actions2[0].equals("add")){
            service.addTask(actions2[1]);
        }

        if (actions2[0].equals("list")){
            service.listTasks();
        }

        if (actions2[0].equals("exit")){

        }

        if (actions2[0].equals("done")){
            service.markDone(Integer.parseInt(actions2[1]));
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
//TODO after edding the infinite loop it only allows one input
// TODO we need to allow the program to get a new action

// TODO 1) understanding the toString stuff gpt recomends