import java.util.Arrays;

public class LabTwoComments {

    public static void main(String[] args) {
        // Add your own tests here!
        int[] a1 = { 42, 99, 17, 33 };
        int[] b1 = everyOther(a1);

        System.out.println();
        System.out.println(Arrays.toString(b1));
    }

    // a = array given
    public static int[] everyOther(int[] a) {
        // for result array that contains integers
        // length will be a.length+1/2 for all conditions (even/odd/empty)
        int[] res = new int[(a.length + 1) / 2];

        // for loop indexing in boundary of result array length
        for (int i = 0; i < res.length; i++)

            // current result array index, plug in the value
            // from the given array of index times 2 (everyother)
            res[i] = a[i * 2];

        return res;

    }

    public static int[][] createZigZag(int rows, int cols, int start) {
        // Create a result array with given rows/cols integers
        int[][] res = new int[rows][cols];

        // Value tracker of the next number to insert
        int value = start;

        // For loop of rows, increasing to max regularly
        for (int r = 0; r < rows; r++) {

            // If current row is divisible by 2, even row
            if (r % 2 == 0) {

                // Column in increasing order
                // left to right
                for (int c = 0; c < cols; c++) {

                    // Current row/column = value
                    res[r][c] = value;

                    // Increase value tracker
                    value++;
                }

                // Otherwise, odd row
            } else {

                // Column in decreasing order
                // cols-1, go from the right to left
                for (int c = cols - 1; c >= 0; c--) {

                    // Current row/column = value
                    res[r][c] = value;

                    // Increase value tracker
                    value++;
                }
            }
        }
        return res;
    }

    public static void reverseAscendingSubarrays(int[] items) {

        int i = 0;

        // while loop for index till the length of items array
        while (i < items.length) {

            int start = i;

            // While loop starting from 1
            // to compare initial index 0 to 0+1 (1) | for strictly increasing
            // ends at items array length
            while (i + 1 < items.length && items[i] < items[i + 1]) {

                // index increases, loop continues if condition is still true
                i++;
            }

            // end of subarray is current index that hold false in previous while loop
            int end = i;

            // While loop for SUBARRAY
            // Start acts as index
            while (start < end) {

                // Temporary variable i
                int temp = items[start];
                items[start] = items[end];
                items[end] = temp;

                start++;
                end--;

            }

            // Move to the next position
            i++;

        }

    }

    public static String pancakeScramble(String text) {

        // Character 1 reversing will do nothing
        // so start i=2
        for (int i = 2; i <= text.length(); i++) {

            // Take first i character of string
            String prefix = text.substring(0, i);

            // Reverse first i characters
            String reversedPrefix = new StringBuilder(prefix).reverse().toString();

            // Take rest of string (after index i)
            text = reversedPrefix + text.substring(i);
        }
        return text;
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
     * javac -cp junit-1.11.0-M2.jar LabTwo.java LabTwoTest.java
     *
     * Run tests)
     * java -jar junit-1.11.0-M2.jar execute -cp . -c LabTwoTest
     *
     * When all test report a pass, you're good to go.
     * 
     */
}
