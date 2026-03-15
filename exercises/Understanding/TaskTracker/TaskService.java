package TaskTracker;
import java.util.ArrayList;
import java.util.List;


public class TaskService {
    private List<Task> tasks = new ArrayList<>();
    private int idCounter = 0;
    public void addTask(String title){
        tasks.add(new Task(this.idCounter++,title));
    }
    public void listTask(){
        for (int i = 0; i <  tasks.size();){
            System.out.println(tasks.get(i));
            i++;
        }
    }
    public Task findById(int id){
        return id;
    }
    
}
