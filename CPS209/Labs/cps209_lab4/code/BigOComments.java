public class BigOComments extends PolynomialComments {

    // store category string
    private String category;

    // Constructor
    public BigOComments(int[] coefficients) {

        // call Polynomial constructor
        super(coefficients);

        // determine degree using inherited method
        int degree = getDegree();

        // assign category based on degree
        if (degree == 0)
            category = "constant";
        else if (degree == 1)
            category = "linear";
        else if (degree == 2)
            category = "quadratic";
        else if (degree == 3)
            category = "cubic";
        else
            category = "polynomial";
    }

    // return category
    public String getCategory() {
        return category;
    }

    // Big-O string representation
    @Override
    public String toString() {

        int degree = getDegree();

        if (degree == 0)
            return "O(1)";
        else if (degree == 1)
            return "O(n)";
        else
            return "O(n^" + degree + ")";
    }
}
