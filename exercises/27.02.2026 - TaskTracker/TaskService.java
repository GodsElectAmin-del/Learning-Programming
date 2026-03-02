import java.util.ArrayList;
import java.util.List;

public class TaskService {
    private int nextID = 1;
    private final List<Task> tasks = new ArrayList<>();

    public void addTask(String title){
        Task t = new Task(nextID++, title);
        tasks.add(t);
    }

    public void listTasks(){
        for (int i = 0; i < tasks.size(); i++){
            System.out.println(tasks.get(i));
        }
    }

    public boolean markDone(int id){
    for(Task t : tasks){
        if (t.getId() == id){
            t.markDone();
            return true;
        }
    }
    return false;
    }

}

// Also man kann anscheind Objekte in Array List speichern
// you can store objekts in a arraylist