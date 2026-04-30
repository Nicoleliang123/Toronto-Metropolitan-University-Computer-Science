
public class PolynomialComments implements Comparable<Polynomial> {
    /*
     * Fill in the methods below according to the descriptions given
     * in the lab document. See the PDF in this archive.
     * 
     * To test your code, you can scroll down to the very bottom of this
     * file for instructions on how to run the unit tests.
     * 
     * Note that your official lab grade will be based on the proportion
     * of unit tests that you pass.
     * 
     * Many of the methods below are from previous Polynomial labs. You
     * can simply copy and paste your previous solutions into this file.
     */

    final int[] coeff;

    // array and trailing zeros
    public PolynomialComments(int[] coefficients) {
        int deg = coefficients.length - 1;

        while (deg > 0 && coefficients[deg] == 0) {
            deg--;
        }

        coeff = new int[deg + 1];

        for (int i = 0; i <= deg; i++) {
            coeff[i] = coefficients[i];
        }
    }

    public int getDegree() {

        return coeff.length - 1;
    }

    public int getCoefficient(int k) {
        if (k < 0 || k >= coeff.length) {
            return 0;
        }

        return coeff[k];
    }

    public long evaluate(int x) {
        long result = 0;
        long power = 1;

        for (int i = 0; i < coeff.length; i++) {
            result += coeff[i] * power;
            power *= x;
        }

        return result;
    }

    public String toString() {
        String result = "";

        for (int i = getDegree(); i >= 0; i--) {
            if (coeff[i] != 0) {
                if (!result.equals("") && coeff[i] > 0) {
                    result += "+";
                }

                result += coeff[i];

                if (i > 0) {
                    result += "x";

                    if (i > 1) {
                        result += "^" + i;
                    }
                }
            }
        }

        if (result.equals("")) {
            return "0";
        }

        return result;
    }

    public Polynomial add(Polynomial other) {
        int maxDeg = Math.max(this.getDegree(), other.getDegree());

        int[] result = new int[maxDeg + 1];

        for (int i = 0; i <= maxDeg; i++) {
            result[i] = this.getCoefficient(i) + other.getCoefficient(i);
        }

        return new Polynomial(result);
    }

    // Multiply each pair of terms and add to the index of i+j
    public Polynomial multiply(Polynomial other) {
        int deg1 = this.getDegree();
        int deg2 = other.getDegree();

        int[] result = new int[deg1 + deg2 + 1];

        for (int i = 0; i <= deg1; i++) {
            for (int j = 0; j <= deg2; j++) {
                result[i + j] += this.coeff[i] * other.coeff[j];
            }
        }

        return new Polynomial(result);
    }

    // Return true if other is a polynomial
    // with same degree and every coefficient is equal
    @Override
    public boolean equals(Object other) {

        if (!(other instanceof Polynomial)) {
            return false;
        }

        Polynomial p = (Polynomial) other;

        if (this.getDegree() != p.getDegree()) {
            return false;
        }

        for (int i = 0; i <= this.getDegree(); i++) {
            if (this.coeff[i] != p.coeff[i]) {
                return false;
            }
        }

        return true;
    }

    // Higher degree will become greater one
    // If degree are equal, compare coefficient
    public int compareTo(Polynomial other) {
        int deg1 = this.getDegree();
        int deg2 = other.getDegree();

        if (deg1 > deg2) {
            return 1;
        } else if (deg1 < deg2) {
            return -1;
        }

        for (int i = deg1; i >= 0; i--) {
            if (this.coeff[i] > other.coeff[i]) {
                return 1;
            } else if (this.coeff[i] < other.coeff[i]) {
                return -1;
            }
        }

        return 0;
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
     * javac -cp junit-1.11.0-M2.jar Polynomial.java PolynomialTestThree.java
     *
     * Run tests)
     * java -jar junit-1.11.0-M2.jar execute -cp . -c PolynomialTestThree
     *
     * When all test report a pass, you're good to go.
     * 
     */
}