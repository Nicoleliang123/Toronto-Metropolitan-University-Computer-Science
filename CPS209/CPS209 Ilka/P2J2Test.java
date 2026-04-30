import org.junit.Test;

import java.io.UnsupportedEncodingException;
import java.util.LinkedList;
import java.util.Random;
import java.util.zip.CRC32;
import static org.junit.Assert.assertEquals;

public class P2J2Test {

    private static final int RUNS = 100000;
    private static final int SEED = 12345;
    
    @Test public void testRemoveDuplicates() {
        // Explicit test cases
        assertEquals("", P2J2.removeDuplicates(""));
        assertEquals("ilka", P2J2.removeDuplicates("ilkka"));
        assertEquals("aba", P2J2.removeDuplicates("aaaaaaaabaaaaaaa"));
        assertEquals("cdcdc", P2J2.removeDuplicates("ccccddccccdcccccc"));
        assertEquals("x", P2J2.removeDuplicates("x"));
        assertEquals("x", P2J2.removeDuplicates("xxxxxxxxxxxxx"));
        assertEquals("abcdefgh", P2J2.removeDuplicates("abcdefgh"));
        // Uppercase and lowercase versions of the same character are different.
        assertEquals("AabBCcdD", P2J2.removeDuplicates("AabBCcdD"));
        assertEquals("\u1234\u5678\u6666", P2J2.removeDuplicates(
        "\u1234\u5678\u5678\u5678\u5678\u5678\u5678\u6666"
        ));
        
        // Pseudorandom fuzz tester
        Random rng = new Random(SEED);
        CRC32 check = new CRC32();        
        for(int i = 0; i < RUNS; i++) {
            StringBuilder sb = new StringBuilder();
            int len = rng.nextInt(500);
            for(int j = 0; j < len; j++) {
                char c = (char)(1 + rng.nextInt(10000));
                int rep = rng.nextInt(10) + 1;
                for(int k = 0; k < rep; k++) {
                    sb.append(c);
                }
            }
            try {
                check.update(P2J2.removeDuplicates(sb.toString()).getBytes("UTF-8"));
            } catch(UnsupportedEncodingException ignored) {}
        }
        assertEquals(2596651304L, check.getValue());
    }
    
    private char randomChar(Random rng) {
        return (char)(rng.nextInt(200) + 97);
    }
    
    private String buildString(Random rng, int len) {
        StringBuilder sb = new StringBuilder();
        for(int j = 0; j < len; j++) {
            sb.append(randomChar(rng));
        }
        return sb.toString();
    }
    
    @Test public void testUniqueCharacters() {
        // Explicit test cases
        assertEquals("abc", P2J2.uniqueCharacters("aaaaaabaaabbbaaababbbabbcbabababa"));
        assertEquals("ilka orne", P2J2.uniqueCharacters("ilkka kokkarinen"));
        assertEquals("", P2J2.uniqueCharacters(""));
        assertEquals("\u4444", P2J2.uniqueCharacters("\u4444\u4444\u4444"));
        assertEquals("aABbcCDd", P2J2.uniqueCharacters("aABbcCDd"));
        
        // Pseudorandom fuzz tester
        Random rng = new Random(SEED);
        CRC32 check = new CRC32(); 
        for(int i = 0; i < RUNS; i++) {
            int len = rng.nextInt(100) + (2 << rng.nextInt(5));
            String s = buildString(rng, len);
            String res = P2J2.uniqueCharacters(s);
            check.update(res.getBytes());
        }    
        assertEquals(3756363171L, check.getValue());
    }
    
}