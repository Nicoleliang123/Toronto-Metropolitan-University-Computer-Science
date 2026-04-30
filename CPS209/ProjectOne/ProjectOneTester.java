import java.util.ArrayList;
import java.util.Collections;

// Mar. 8th 2026

public class ProjectOneTester {
    
    public static void main(String[] args) {

        /*
         * Program Description:
         * This program reads the given quadratic equation of all kinds,
         * and calculates according to values given and return back the
         * result of evaluation and detailed properties of the equation.
         * The amount of quadratic equation that is wished to be solved at
         * once is unlimited, as "sort" is used by Collections, to later on
         * sort your equations in order.
         * 
         * Superclass - QuadraticEquation
         * Subclass - AdvancedQuadraticEquation
         */

        // Create QuadraticEquation (with different types)
        QuadraticEquation q1 = new QuadraticEquation(1, -3, 2);
        QuadraticEquation q2 = new QuadraticEquation(1, 2, 1);
        QuadraticEquation q4 = new QuadraticEquation(1, 1, 1);

        // Creating AdvancedQuadraticEquation (with different cases)
        AdvancedQuadraticEquation q3 = new AdvancedQuadraticEquation(2, 5, 3);
        AdvancedQuadraticEquation q5 = new AdvancedQuadraticEquation(1, -4, 3);

        // Display the original equations
        System.out.println("Equations:");
        System.out.println(q1);
        System.out.println(q2);
        System.out.println(q3);
        System.out.println(q4);
        System.out.println(q5);

        // Solutions of the equation & result of
        // full properties from AdvancedQuadraticEquation subclass
        System.out.println(q1.solve());
        System.out.println(q2.solve());
        System.out.println(q3.fullProperties());
        System.out.println(q5.fullProperties());

        // Using ArrayList type to store in equations

        // Creates new arraylist
        ArrayList<QuadraticEquation> equations = new ArrayList<>();
        equations.add(q1);
        equations.add(q2);
        equations.add(q3);
        equations.add(q4);
        equations.add(q5);

        // Use sort method in collections by discriminants
        Collections.sort(equations);

        System.out.println("\nSorted by discriminant:");
        for (QuadraticEquation q : equations) {
            System.out.println(q + " -> Discriminant: " + q.getDiscriminant());

        }
    }
}
