public class PolynomialComments {
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

    public PolynomialComments(int[] coefficients) {
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

        // Add coefficients term-by-term
        for (int i = 0; i < maxLen; i++) {
            sum[i] = this.getCoefficient(i) + other.getCoefficient(i);
        }

        // Trim trailing zeros so degree is correct
        int deg = maxLen - 1;
        while (deg > 0 && sum[deg] == 0) {
            deg--;
        }

        int[] trimmed = new int[deg + 1];
        for (int i = 0; i <= deg; i++) {
            trimmed[i] = sum[i];
        }

        // Return NEW polynomial (do not modify originals)
        return new Polynomial(trimmed);

    }

    @Override
    public String toString() {

        // Build readable polynomial string
        StringBuilder sb = new StringBuilder();

        for (int i = getDegree(); i >= 0; i--) {
            int c = coeff[i];
            if (c == 0)
                continue;

            // Handle signs
            if (sb.length() > 0) {
                sb.append(c > 0 ? " + " : " - ");
            } else if (c < 0) {
                sb.append("-");
            }

            int abs = Math.abs(c);

            // Format term depending on exponent
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
