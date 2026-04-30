public class Course {

    //Instance variables - store info
    private String courseCode;
    private int lectureStart;
    private int lectureEnd;
    private int labStart;
    private int labEnd;
    private int year;
    private String semester;

    //Constructor - runs when Course object created
    //Initializes course code 
    public Course(String code) {
        courseCode = code;
    }

    //Getter methods 
    //Return private variable values that were made earlier
    //Getting from CourseTest file

    public String getCourseCode() {
        return courseCode;
    }

    public int getLectureStart() {
        return lectureStart;
    }

    public int getLectureEnd() {
        return lectureEnd;
    }

    public int getLabStart() {
        return labStart;
    }

    public int getLabEnd() {
        return labEnd;
    }

    public int getYear() {
        return year;
    }

    public String getSemester() {
        return semester;
    }

    //Setter methods
    //Update values when object is created

    //Set lecture start and end times
    public void setLectureTime(int start, int end) {
        lectureStart = start;
        lectureEnd = end;

        //Check for conflic with lab
        //Calls on the timesOverlap method to compare, and if it holds overlap
        //Print out warning
        if (timesOverlap(lectureStart, lectureEnd, labStart, labEnd)) {
            System.out.println("Warning: Lecture and lab times overlap for " + courseCode);
        }
    }

    //Set lab times
    public void setLabTime(int start, int end) {
        labStart = start;
        labEnd = end;

        //Check for conflict with lecture
        //Calls timesOverlap method
        if (timesOverlap(lectureStart, lectureEnd, labStart, labEnd)) {

            //Prints out warning system if timing are overlapping
            System.out.println("Warning: Lecture and lab times overlap for " + courseCode);
        }
    }


    //Year of course taken
    public void setYear(int y) {
        year = y;
    }

    //Semester
    public void setSemester(String s) {
        semester = s;
    }

    //Helper method - timesOverlap
    //If two time intervals overlaps
    //s = start | e = end
    private boolean timesOverlap(int s1, int e1, int s2, int e2) {

        //If both time not been set yet, no overlap
        if ((s1 == 0 && e1 == 0) || (s2 == 0 && e2 == 0)) {
            return false;
        }

        //If one starts before the other and vice versa
        //Overlaps
        return s1 < e2 && s2 < e1;
    }
}