//Feb. 8th 2026
import java.util.Arrays;

public class Polynomial {
    
    private final int[] r_coeff;

    public Polynomial(int[] coefficients) {

        int len = coefficients.length - 1;

        while (len > 0 && coefficients[len] == 0) {

            len--;
        }

        r_coeff = Arrays.copyOf(coefficients, len + 1);
    }

    public int getDegree() {

        return r_coeff.length - 1;

    }

    public int getCoefficient(int k) {

        if (k >= 0 && k < r_coeff.length) {
            return r_coeff[k];

        } else {

            return 0;
        }
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
