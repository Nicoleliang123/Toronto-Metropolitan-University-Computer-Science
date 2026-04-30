public class LabOne {
    //Jan. 25th 2026
    
    /*
     * PROBLEM 1)
     *
     * Python has the integer exponentiation operator ** conveniently built
     * in the language, whereas Java unfortunately does not offer that.
     *
     * Instead of integer exponentiation, however, you will implement the
     * related operation of "falling power". Each term multiplied into the
     * product is always one less than the previous term.
     * 
     * For example, the fallingPower(8, 3) is computed as 8 × 7 × 6 = 336.
     * Similarly, the fallingPower(10, 5) equals 10 × 9 × 8 × 7 × 6 = 30240.
     * 
     * Nothing essential changes in this calculation when the base is negative;
     * the fallingPower(–4, 5) is computed as –4 × –5 × –6 × –7 × –8 = –6720.
     * Similar to normal exponentiation, fallingPower(n, 0) = 1 for any nonzero
     * integer n.
     * 
     * This method should return the fallingPower(n, k) where the base n can be
     * any integer, and the exponent k can be any integer greater than zero.
     * 
     * Hint: notice that the return type is long... you should probably declare
     * and store your running result similarly, as a long int.
     */

    public static long fallingPower(int n, int k) {

        long result = 1;

        for (int i = 0; i < k; i++) {

            result *= n - i;
        }

        return result;

    }

    /*
     * PROBLEM 2)
     *
     * Inside an array arr, an inversion is a pair of two positions i<j
     * such that arr[i]>arr[j]. In combinatorics, the inversion count inside
     * an array is a rough measure of how “out of order” that array is.
     *
     * If an array is sorted in ascending order, it has zero inversions,
     * whereas an n-element array sorted in reverse order has n(n–1)/2
     * inversions, the largest number possible.
     *
     * This method should count the inversions inside the given array arr,
     * and return that count. As always when writing methods that operate on
     * arrays, make sure that your method works correctly for arrays of any
     * length, including the important special cases arrays with length zero
     * and one.
     */

    public static int countInversions(int[] arr) {
        int count = 0;

        if (arr.length == 0 || arr.length == 1) {
            return count;
        }

        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {

                if (arr[i] > arr[j]) {

                    count++;
                }
            }
        }

        return count;
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
