public class CourseTest {

    //Main file
    public static void main(String[] args) {

        // Pre-requisite course
        Course cps209 = new Course("CPS209");

        //Lecture time, Lab time, Year, Semester
        cps209.setLectureTime(9, 11);
        cps209.setLabTime(12, 14);
        cps209.setYear(2023);
        cps209.setSemester("fall");

        // Current course
        Course cps305 = new Course("CPS305");
        cps305.setLectureTime(10, 12);
        cps305.setLabTime(11, 13); // conflict, overlap of end/start
        cps305.setYear(2024);
        cps305.setSemester("winter");

        // Required course: CPS383
        Course cps383 = new Course("CPS383");
        cps383.setLectureTime(14, 16);
        cps383.setLabTime(16, 18);
        cps383.setYear(2024);
        cps383.setSemester("winter");

        // Required course: CPS510
        Course cps510 = new Course("CPS510");
        cps510.setLectureTime(10, 13);
        cps510.setLabTime(12, 14); // conflict
        cps510.setYear(2025);
        cps510.setSemester("spring");

        System.out.println("Testing completed.");
    }
}