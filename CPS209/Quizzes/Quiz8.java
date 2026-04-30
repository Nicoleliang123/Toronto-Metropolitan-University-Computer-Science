import java.io.*;
import java.util.*;

public class Quiz8 {

    public static void separateWords(String inputFile, String wordFile, String doubleFile) {
        try {
            Scanner in = new Scanner(new File(inputFile));
            PrintWriter wordOut = new PrintWriter(new FileWriter(wordFile));
            PrintWriter doubleOut = new PrintWriter(new FileWriter(doubleFile));

            while (in.hasNext()) {
                String token = in.next();

                try {
                    // Try to parse as double
                    Double.parseDouble(token);
                    doubleOut.println(token);
                } catch (NumberFormatException e) {
                    // Not a double
                    wordOut.println(token);
                }
            }

            in.close();
            wordOut.close();
            doubleOut.close();

        } catch (IOException e) {
            System.out.println("File error: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Test
        separateWords("input.txt", "words.txt", "doubles.txt");
        System.out.println("Done!");
        
         // Run test with input1.txt
        separateWords("input1.txt", "words1.txt", "doubles1.txt");

        System.out.println("Test 1 complete. Check words1.txt and doubles1.txt");
    }
}