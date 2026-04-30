public class P2J3 {

    public static void reverseAscendingSubarrays(int[] items){
        /*Rearrange elements of given array of integers in place 
        & don't create new array so that elements of every
        maximal strictly ascending subarray are reversed.
        
        Ex/ {5,7,10,4,2,7,8} 
        = {10,7,5,4,8,7,2}*/

        for(int i=0; i < items.length; i++){
            int start = i; 
        

            while(i+1 < items.length && items[i] < items[i+1]){

                i++;
            }

            int end = i;

            for(int left = start, right = end; left < right; left++, right--){

                int temp = items[left];
                items[left] = items[right];
                items[right] = temp;

            }
        }
    }

    public static String pancakeScramble(String text){
        /*Given a text string, construct a new string
        by reversing its first 2 characters, then reverse
        the first three character and so on */

        for(int i=2; i <= text.length(); i++){

            String ss = text.substring(0, i);

            String reversed = new StringBuilder(ss).reverse().toString();

            text = reversed + text.substring(i);
        
        }

        return text; 
    }

    public static String reverseVowels(String text){

        /*Given text string, create & return a new string of
        same length where all vowels have been reversed and all 
        other characters are kept as is. 
        
        Vowels = aeiouAEIOU
        */

        String vowels = "aeiouAEIOU"; 

        StringBuilder found = new StringBuilder();
        for(int i=0; i < text.length(); i++){

            if (vowels.indexOf(text.charAt(i)) != -1){

                found.append(text.charAt(i));
            }
        }

        found.reverse();

        StringBuilder result = new StringBuilder();

        int vIndex = 0;

        for (int i = 0; i < text.length(); i++){
            char c = text.charAt(i);

            if (vowels.indexOf(c) != -1) {

            //vVowel move forwardif current is vowel
            char newVowel = found.charAt(vIndex++);
            
            //Maintain capitalization pattern
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
}
