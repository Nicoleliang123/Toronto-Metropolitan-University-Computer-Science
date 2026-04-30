
public class Polynomial {

    //Feb. 15th 2026
    
    /*
     * Fill in the methods below according to the descriptions given
     * in the lab document. See the PDF in this archive.
     * 
     * To test your code, you can scroll down to the very bottom of this
     * file for instructions on how to run the unit tests.
     * 
     * Note that your official lab grade will be based on the proportion
     * of unit tests that you pass.
     */

    final int[] coeff;

    public Polynomial(int[] coefficients) {
        coeff = new int[coefficients.length];
        for (int i = 0; i < coefficients.length; i++) {
            coeff[i] = coefficients[i];
        }
    }

    public int getDegree() {
        for (int i = coeff.length - 1; i >= 0; i--) {
            if (coeff[i] != 0) {
                return i;
            }
        }
        return 0; // zero polynomial case
    }

    public int getCoefficient(int k) {
        if (k < 0 || k >= coeff.length)
            return 0;
        return coeff[k];
    }

    public long evaluate(int x) {

        long result = 0;
        long power = 1; // represents x^0 initially

        for (int i = 0; i < coeff.length; i++) {
            result += coeff[i] * power;
            power *= x; // move to next power of x
        }
        return result;

    }

    public Polynomial add(Polynomial other) {
        int maxLen = Math.max(this.coeff.length, other.coeff.length);
        int[] sum = new int[maxLen];

        for (int i = 0; i < maxLen; i++) {
            sum[i] = this.getCoefficient(i) + other.getCoefficient(i);
        }

        int deg = maxLen - 1;
        while (deg > 0 && sum[deg] == 0) {
            deg--;
        }

        int[] trimmed = new int[deg + 1];
        for (int i = 0; i <= deg; i++) {
            trimmed[i] = sum[i];
        }

        return new Polynomial(trimmed);

    }

    @Override
    public String toString() {

        StringBuilder sb = new StringBuilder();

        for (int i = getDegree(); i >= 0; i--) {
            int c = coeff[i];
            if (c == 0)
                continue;

            if (sb.length() > 0) {
                sb.append(c > 0 ? " + " : " - ");
            } else if (c < 0) {
                sb.append("-");
            }

            int abs = Math.abs(c);

            if (i == 0)
                sb.append(abs);
            else if (i == 1)
                sb.append(abs + "x");
            else
                sb.append(abs + "x^" + i);
        }

        if (sb.length() == 0)
            return "0";

        return sb.toString();
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
 * javac -cp junit-1.11.0-M2.jar Polynomial.java PolynomialTestTwo.java
 *
 * Run tests)
 * java -jar junit-1.11.0-M2.jar execute -cp . -c PolynomialTestTwo
 *
 * When all test report a pass, you're good to go.
 * 
 */
