package TaskTracker;
import java.util.ArrayList

public class TaskService {
    private List<Task> tasks = new ArrayList<>();

    public void addTask(String title){
        tasks.add(title);
    }
    public Task listTask(){
        return tasks;
    }
    public Task findById(int id){
        return Task[id];
    }
    
}
