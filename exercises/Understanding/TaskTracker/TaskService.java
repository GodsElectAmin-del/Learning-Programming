package TaskTracker;
import java.util.ArrayList;
import java.util.List;


public class TaskService {
    private List<Task> tasks = new ArrayList<>();
    private int idCounter = 0;
    public void addTask(String title){
        tasks.add(new Task(this.idCounterdCounter++,title));
    }
    public Task listTask(){
        for (int i; i <  tasks.size()){
            tasks.get(i);
        }
    }
    public Task findById(int id){
        tasks
    }
    
}
