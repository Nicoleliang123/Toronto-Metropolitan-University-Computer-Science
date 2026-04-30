public class LabThreeComments {

    public static String reverseVowels(String text) {
        String vowels = "aeiouAEIOU";

        // Collect vowels
        StringBuilder found = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {

            // Checks if vowel
            if (vowels.indexOf(text.charAt(i)) != -1) {

                // Add to found if vowel
                found.append(text.charAt(i));
            }
        }

        // Reverse the collected vowels
        found.reverse();

        // Build result
        StringBuilder result = new StringBuilder();

        // tracks reversedlist vowel index
        int vIndex = 0;

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);

            if (vowels.indexOf(c) != -1) {

                // vVowel move forwardif current is vowel
                char newVowel = found.charAt(vIndex++);

                // Maintain capitalization pattern
                if (Character.isUpperCase(c)) {
                    newVowel = Character.toUpperCase(newVowel);
                } else {
                    newVowel = Character.toLowerCase(newVowel);
                }

                result.append(newVowel);
            } else {
                result.append(c);
            }
        }

        return result.toString();
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
     * javac -cp junit-1.11.0-M2.jar LabThree.java LabThreeTest.java
     *
     * Run tests)
     * java -jar junit-1.11.0-M2.jar execute -cp . -c LabThreeTest
     *
     * When all test report a pass, you're good to go.
     * 
     */
}
