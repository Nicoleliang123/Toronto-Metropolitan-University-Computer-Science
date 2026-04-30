public class P2J2 {

    public static String removeDuplicates(String text){

        /* Given text string, create & return brand new string that is
        otherwise the same as text except that every run of equal
        consecutive characters has been turned into a single character.

        Ex/ "Kokkarinen" and "aaaabbxxxxaaxa", would return
        "Kokarinen" and "abxaxa". 

        Only consecutive duplicate occurences of the same character 
        are elimited, but late of same remains in result.

        Uppercase & lowercase are considered different
        "AaabbBBBCc" return "AabBCc"
         */

        if (text.length()==0){
            return text;
        }

        String result = "";
        result += text.charAt(0);

        for(int i=1; i < text.length(); i++){

            if(text.charAt(i) != text.charAt(i-1)){
                result += text.charAt(i);
            }
        }

        return result;
    }

    public static String uniqueCharacters(String text){

        /*Create & return new string that contains each character
        of text only once regarless of its apperance count, these 
        characters listed in order that they appear in original string.
        
        Ex/ "Kokkarinen" = "Kokarine"
            "aaaabbxxAxxaaxa" = "abxA" 
        
        Uppercase & lowercase are considered different
        */

        if (text.length() == 0){
            return text;
        }

        String result = "";
        result += text.charAt(0);

        for(int i=1; i < text.length(); i++){

            char current = text.charAt(i);

            //if indexOf that ch letter doesn't appear
            //returns -1
            if(result.indexOf(current) == -1){

                //add current into result
                result += current;
            }
        }

        return result;
    }

}
