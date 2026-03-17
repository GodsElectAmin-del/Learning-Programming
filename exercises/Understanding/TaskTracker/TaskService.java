package TaskTracker;
import java.util.ArrayList;
import java.util.List;


public class TaskService {
    private List<Task> tasks = new ArrayList<>();
    private int idCounter = 1;
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
        for (int i = 0; i < tasks.size();){
        Task t = tasks.get(i);
            if (t.getId() == id){
                return t;
            }
            i++;
        }
        return null;
    }
    public void markDoneTask(int id){
        for(int i = 0; i < tasks.size();){
            Task t = tasks.get(i);
            if(id == t.getId()){
                t.markDone();
            }
            i++;
        }
    }
    
}
