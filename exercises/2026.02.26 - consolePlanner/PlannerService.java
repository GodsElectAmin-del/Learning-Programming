import java.util.ArrayList;
import java.util.List;

public class PlannerService{
  private final List<Entry> entries = new ArrayList<>();

// Getter
public String getEntry(){
    return entries;
}
// Setter
public void setEntry(Entry newEntry){
    entries.add(newEntry);
}
}