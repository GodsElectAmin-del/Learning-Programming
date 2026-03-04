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

        public void markDone(){
        this.done = true;
    }
    
    public Task(int id, String title){
        // ist das hinreichend oder muss hier noch was hin
        this.id = id;
        this.title = title;
        this.done = false;
    }



}
