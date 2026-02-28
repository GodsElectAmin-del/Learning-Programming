 class Task{
    private int id;
    private String title;
    private boolean done;

    public int getId(){
        return id;
    }
    public void setId (int newID){
         this.id = newID;
}
    public String getTitle(){
        return title;
    }

    public void setTitle(String newTitle){
        this.title = newTitle;
    }

    public boolean getDone(){
        return done;
}
    public void setDone(boolean newDone){
        this.done = newDone;
    }

}