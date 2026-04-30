//Import PriorityQueue class
import java.util.PriorityQueue; 

public class ToDoList {

    //Declares prirority queue to store Task objects
    private PriorityQueue<Task> tasks;

    // Constructor
    public ToDoList() {

        //PriorityQueue automatically orders using compareTo from Task
        //Initializing priority queue
        tasks = new PriorityQueue<>();
    }

    //Method in adding task
    public void addTask(Task task) {
        
        tasks.add(task); //inserts into correct position (sorted)
    }

    //Method to get and remove the highest priority task
    public Task getNextTask() {

        return tasks.poll(); // removes and returns highest priority task
    }

    //Checks if there are no tasks left
    public boolean isEmpty() {

        return tasks.isEmpty(); 
        //returns true if queue is empty
    }
}
