 class Task{
    private int id;
    private String title;
    private boolean done;

    public int getid(){
        return id;
    }
    public void setid (int newID){
         this.id = newID;
}
    public String gettitle(){
        return title;
    }

    public void settitle(String newTitle){
        this.title = newTitle;
    }

    public boolean getdone(){
        return done;
}
    public void setdone(boolean newDone){
        this.done = newDone;
    }

}