package TaskTracker;

public class TaskService {
    private List<Task> tasks = new ArrayList<>();

    public void addTask(String title){
        this.title = title;
    }
    public Task listTask(){
        return tasks;
    }
    public Task findById(int id){
        return Task[id];
    }
    
}
