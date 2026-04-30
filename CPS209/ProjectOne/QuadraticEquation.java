public class QuadraticEquation implements Comparable<QuadraticEquation> {

    /*
     * This class represents a Quadratic Equation in form
     * of ax^2 + bx + c = 0
     */

    // Declaring of instance variables - for equation sub in
    private double a;
    private double b;
    private double c;

    // Constructor for Quadratic Equation

    public QuadraticEquation(double a, double b, double c) {

        // Variables are double as decimal numbers are normal in
        // quadratic equations

        // Initialize coefficients
        this.a = a;
        this.b = b;
        this.c = c;

    }

    // Getters, get the value of A/B/C Variables
    public double getA() {

        return a;
    }

    public double getB() {

        return b;
    }

    public double getC() {

        return c;
    }

    // Setters, to call this variable is the variable
    public void setA(double a) {
        this.a = a;
    }

    public void setB(double b) {
        this.b = b;
    }

    public void setC(double c) {
        this.c = c;
    }

    // getDiscriminant method -- Calculates the discriminant of quadratic equation
    public double getDiscriminant() {

        // Formula - b^2-4ac

        // Return the value of calculation, which can later solve real roots
        return (b * b) - (4 * a * c);
    }

    // solve method -- Solves quadratic equation & returns string
    public String solve() {

        // Calling method - Get discriminant from getters
        double d = getDiscriminant();

        // Under Conditions of discriminant, determines root type
        // If discriminant smaller then 0
        if (d < 0) {
            return "No real roots.";
        } else if (d == 0) {

            // There is one root
            double root = -b / (2 * a);
            return "One root: " + root;
        } else {

            // There is two roots
            double r1 = (-b + Math.sqrt(d)) / (2 * a);
            double r2 = (-b - Math.sqrt(d)) / (2 * a);

            return "Two roots: " + r1 + " and " + r2;
        }

    }

    // sum of root method
    public double sumOfRoots() {
        return -b / a;
    }

    // product of roots method
    public double productOfRoots() {
        return c / a;
    }

    // Override equals
    @Override
    public boolean equals(Object obj) {

        // If this object is equal to obj, return true
        if (this == obj) {
            return true;
        }

        // Otherwise false if null or not instance of QuadraticEquation
        if (obj == null || !(obj instanceof QuadraticEquation)) {
            return false;
        }

        // Casting
        QuadraticEquation other = (QuadraticEquation) obj;

        // Checks if variables of a,b,c are equal between other and this
        return a == other.a && b == other.b && c == other.c;
    }

    // Override comparable
    @Override
    public int compareTo(QuadraticEquation other) {

        // Compare this discriminant to other discriminant,
        // if equal will return 0
        return Double.compare(this.getDiscriminant(), other.getDiscriminant());
    }

    // Override toString
    @Override
    public String toString() {

        return a + "x^2 + " + b + "x + " + c;
    }
}
