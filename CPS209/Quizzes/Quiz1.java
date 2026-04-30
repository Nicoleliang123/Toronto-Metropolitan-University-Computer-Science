public class Quiz1 {

    public static void main(String args[]) {

        int a, b, c;

        //test case | initialize values
        a = 3;
        b = 4;
        c = 5;

        System.out.println(
            "Can integers: a: " + a + ", b: " + b + ", and c: " + c +
            " form a triangle? " + canBeTriangle(a, b, c)
        );

        //test case
        a = 1;
        b = 2;
        c = 3;

        System.out.println(
            "Can integers: a: " + a + ", b: " + b + ", and c: " + c +
            " form a triangle? " + canBeTriangle(a, b, c)
        );

        //------------------------------------------

        // Execute FizzBuzz function | test case
        fizzBuzz(101);
        fizzBuzz(0);
        fizzBuzz(20);
    }

    // canBeTriangle method | return value
    public static boolean canBeTriangle(int n1, int n2, int n3) {

        //triangle conditions
        if (n1 + n2 > n3 && n1 + n3 > n2 && n2 + n3 > n1) {

            // If all conditions are true
            return true;
        }

        // Otherwise false (outside of if loop)
        return false;
    }

    // fizzBuzz method (void, no return)
    public static void fizzBuzz(int num) {

        if (num < 1){
            System.out.println("N must be greater than 1");
            
        }

        if (num > 100){
            System.out.println("Too much work, no thanks");
        }

        if (num > 1 && num < 100){
            // Divisible by 3 & 5
            if (num % 3 == 0 && num % 5 == 0) {
                System.out.println("FizzBuzz");
            }

            // Divisible by 3
            else if (num % 3 == 0) {
                System.out.println("Fizz");
            }

            // Divisible by 5
            else if (num % 5 == 0) {
                System.out.println("Buzz");
            }

            // Else, print number
            else {
                System.out.println(num);
            }
        }
    }
}
