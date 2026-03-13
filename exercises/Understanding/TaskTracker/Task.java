package TaskTracker;

public class Task {
    int id;
    String title;
    boolean done;

    public String toString(){
        return "#" + id + " [" + ((done)? "x" : " ") +"] " + title;
    }

    public void IdMaker(int id){
        this.id = id;
    }

    public void TitleMaker(String title){
        this.title = title;
    }

    public void DoneMaker(boolean done){
        this.done = done;
    }
}
