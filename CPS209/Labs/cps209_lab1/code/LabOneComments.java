public class LabOneComments {
    /*
     * For learning purposes, certain lines are commented.
     * This helps for programmers to understand certain code logic
     * and the functionality of certain codes.
     * 
     */

    // PROBLEM 1

    public static long fallingPower(int n, int k) {
        // long used due to result can be large, avoid overflow
        long result = 1;

        // for loop, run k times
        // each, will multiply by (n-i)
        for (int index = 0; index < k; index++) {
            result *= (n - index);
        }

        return result;
    }

    // PROBLEM 2

    public static int countInversions(int[] arr) {
        // Counter for inversions found
        int counter = 0;

        // For loop for first position i
        // arr.length, determines how long the array is
        for (int i = 0; i < arr.length; i++) {

            // Loop for second position j
            // j starts after i by i+1=j
            for (int j = i + 1; j < arr.length; j++) {

                // If value at position i is greater than j
                // Counter adds one (inversion)
                if (arr[i] > arr[j]) {
                    counter++;
                }
            }
        }

        return counter;
    }

    /*
     * RUNNING THE UNIT TESTS)
     *
     * Evaluate your code by using the following commands in the terminal.
     * Any time you make changes to your code, you will have to run
     * both commands again. The first one compiles your code and the
     * tester into two Java class files. The second command runs the
     * unit tests and displays the results.
     *
     * Compile)
     * javac -cp junit-1.11.0-M2.jar LabOne.java LabOneTest.java
     *
     * Run tests)
     * java -jar junit-1.11.0-M2.jar execute -cp . -c LabOneTest
     *
     * When all test report a pass, you're good to go.
     * 
     */

}
