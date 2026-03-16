package TaskTracker;

public class Task {
   private int id;
    private String title;
    private boolean done;


    public Task(int id, String title){
        this.id = id;
        this.title = title;
    }
    public boolean markDone(){
        return done;
    }
    public int getId(){
        return this.id;
    }
    @Override
        public String toString(){
        return "#" + id + " [" + ((done)? "x" : " ") +"] " + title;
    }
    
}
