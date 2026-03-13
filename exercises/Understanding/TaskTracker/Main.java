package TaskTracker;

public class Main {
    public static void main(String[] args) {
        Task newTask1 = new Task();
        newTask1.IdMaker(1);
        newTask1.TitleMaker("The Singularity is Near");
        newTask1.DoneMaker(false);
        System.out.println(newTask1);

        Task newTask2 = new Task();
        newTask2.IdMaker(2);
        newTask2.TitleMaker("Habits by James Clear");
        newTask2.DoneMaker(true);
        System.out.println(newTask2);
    }
    
}
//can be improved apprantly