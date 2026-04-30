//Import
import java.util.ArrayList;

public class Quiz2 {

    //Main method (testing)
    public static void main(String[] args) {

        //divisors method
        int[] d = divisors(12);
        for (int num : d) {
            System.out.print(num + " ");
        }

        System.out.println();

        //parseInt method
        int value = parseInt("a5b4c3");
        System.out.println(value);
    }

    //Accepts integer
    //Returns array of integer's divisors
    //Ascending order
    public static int[] divisors(int n) {

        //Create and initialize list holding integers
        ArrayList<Integer> list = new ArrayList<>();

        //For loop start at 1(divisor for all), to n value
        for (int i = 1; i <= n; i++) {

            //If number is divisible by i = divisor
            if (n % i == 0) {

                //arraylist add current index
                list.add(i);
            }
        }

        //ArrayList to int[]

        //Create result list according to ArrayList size
        int[] result = new int[list.size()];

        //For loop for index to ArrayList size
        for (int i = 0; i < list.size(); i++) {

            //Value of current index = ArrayList get value at that index
            result[i] = list.get(i);
        }

        return result;
    }

    //Accepts string, MIGHT contain digit characters (must be extracted and return as integer)
    public static int parseInt(String s) {

        //Create a result for extracted digits 
        String digits = "";

        for (int i = 0; i < s.length(); i++) {

            char c = s.charAt(i);

            //Checks if c at string index is an digit
            if (Character.isDigit(c)) {

                //Add digit into result string
                digits += c;
            }
        }

        //Convert the digit string to an integer
        return Integer.parseInt(digits);
    }

}