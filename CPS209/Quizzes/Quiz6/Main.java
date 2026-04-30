public class Main {
    public static void main(String[] args) {

        // Create ToDoList
        ToDoList list = new ToDoList();

        // Create tasks
        Task t1 = new Task("Clean dishes", 20, 2);
        Task t2 = new Task("Finish assignment", 60, 5);
        Task t3 = new Task("Workout", 45, 3);
        Task t4 = new Task("Watch Netflix", 120, 1);

        // Add tasks
        list.addTask(t1);
        list.addTask(t2);
        list.addTask(t3);
        list.addTask(t4);

        // Process tasks in order of priority
        System.out.println("Tasks in priority order:\n");

        //to loop until list is empty (all tasks are removed)
        while (!list.isEmpty()) {
            
            System.out.println(list.getNextTask());
        }
    }
}
