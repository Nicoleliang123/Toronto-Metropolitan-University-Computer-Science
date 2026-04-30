import java.util.Arrays;

public class LabTwo {

    //Feb. 2nd 2026
    /*
     * Fill in the methods below according to the descriptions given
     * in the lab document. See the PDF in this archive.
     * 
     * You should test your code by calling your methods in the main
     * method provided. One sample call is given, but you should write
     * your own test cases in main() and try them out as you go.
     * 
     * Once you're satisfied that your methods are producing the correct
     * results, you can scroll down to the very bottom of this file
     * for instructions on how to run the unit tests.
     * 
     * Note that your official lab grade will be based on the unit tests
     * and not what you wrote in main(), but it's still a good idea
     * to practice writing your own main() method. You won't always be
     * given unit tests.
     */

    public static void main(String[] args) {
        // Add your own tests here!

        int[] a1 = { 42, 99, 17, 33 };
        int[] b1 = everyOther(a1);

        System.out.println();
        System.out.println(Arrays.toString(b1));
    }

    public static int[] everyOther(int[] a) {

        int[] result = new int[(a.length + 1) / 2];

        int rindex = 0;

        for (int i = 0; i < a.length; i++) {

            if (i % 2 == 0) {

                result[rindex] = a[i];

                rindex++;
            }
        }

        return result;
    }

    public static int[][] createZigZag(int rows, int cols, int start) {

        int[][] result = new int[rows][cols];

        for (int r = 0; r < rows; r++) {

            if (r % 2 != 0) {

                for (int c = cols - 1; c >= 0; c--) {

                    result[r][c] = start;
                    start++;
                }

            } else {

                for (int c = 0; c < cols; c++) {

                    result[r][c] = start;
                    start++;

                }

            }
        }
        return result;
    }

    public static void reverseAscendingSubarrays(int[] items) {
        for (int i = 0; i < items.length; i++) {
            int start = i;

            while (i + 1 < items.length && items[i] < items[i + 1]) {

                i++;
            }

            int end = i;

            for (int left = start, right = end; left < right; left++, right--) {

                int temp = items[left];
                items[left] = items[right];
                items[right] = temp;

            }
        }
    }

    public static String pancakeScramble(String text) {

        for (int i = 2; i <= text.length(); i++) {

            String ss = text.substring(0, i);

            String reversed = new StringBuilder(ss).reverse().toString();

            text = reversed + text.substring(i);
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
