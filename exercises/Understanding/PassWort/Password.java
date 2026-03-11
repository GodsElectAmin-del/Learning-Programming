package PassWort;

public class Password {
    private String username;
    private String password;

    public Password(String username, String password){
        this.username = username;
        this.password = password; 
    }
    public void setUsername (String username){
        this.username = username;
    }
    public void changePassword(String OldPassWord, String NewPassWord){
        if (OldPassWord == this.password){
            this.password = NewPassWord;
        }
        else{
            
        }
    }
    public String getUserName(){
        return this.username;
    }

    public String  getPasswrod(){
        return this.password;
    }
}
