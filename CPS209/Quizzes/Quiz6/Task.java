public class Task implements Comparable<Task> {

    //Private variables
    private String description; //Store what task is
    private int time; //Estimated length of time 
    private int priority; //Number to indicate priority of task


    //Constructor
    public Task(String description, int time, int priority){

        //Initialize 
        this.description = description;
        this.time = time;
        this.priority = priority; 
    }

    //Getter method
    public String getDescription(){

        return description;
    }

    public int getTime(){

        return time;
    }

    public int getPriority(){

        return priority; 
    }

    //How tasks are being compared in the priority queue
    @Override
    public int compareTo(Task other){

        //Higher priority comes first (compare through numbers)
        return other.priority - this.priority;
    }
    
    //Output
    @Override
    public String toString(){

        return "Task: " + description + " | Time: " + time + "mins | Priority: " + priority; 

    }
}
