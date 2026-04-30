import java.util.Arrays;

public class PolynomialComments {
    private final int[] coeff;

    public PolynomialComments(int[] coefficients) {
        int last = coefficients.length - 1;

        // Remove leading zeros from highest power

        while (last > 0 && coefficients[last] == 0) {
            last--;
        }

        // Defensive copy
        coeff = Arrays.copyOf(coefficients, last + 1);
    }

    // Degree highest power = last index
    public int getDegree() {
        return coeff.length - 1;
    }

    public int getCoefficient(int k) {
        if (k < 0 || k >= coeff.length)
            return 0;

        return coeff[k];
    }
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
 * javac -cp junit-1.11.0-M2.jar Polynomial.java PolynomialTestOne.java
 *
 * Run tests)
 * java -jar junit-1.11.0-M2.jar execute -cp . -c PolynomialTestOne
 *
 * When all test report a pass, you're good to go.
 * 
 */
