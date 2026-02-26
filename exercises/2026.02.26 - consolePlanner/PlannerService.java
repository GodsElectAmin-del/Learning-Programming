import java.util.ArrayList;
import java.util.List;

public class PlannerService{
  private final List<Entry> entries = new ArrayList()List<>();

// Getter
public String getEntry(){
    return entries;
}
// Setter
public void setEntry(Entry newEntry){
    this.entries = newEntry;
}
}