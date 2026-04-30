public class P2J1 {
    
    public static long fallingPower(int n, int k){
    
        /*Ex: falling power 8^3 = 8 x 7 x 6 = 336
         *returns integer 336
         *Goes for the same when bases are negative
         *n^0 = 1 for any nonzero integer n

         *Return the falling power n^k where base n can
         *any integer(pos or neg or 0) & exponent k can
         *be any nonnegative integer (not 0).

         *Note: avoid overflows
         */

         long result = 1;

         for(int i=1; i <= k; i++){

            result *= n;
            n--;
         }

         return result;
    }

    public static int[] everyOther(int[] arr){

        /*Given integer array arr, create & return new array
        that contains precisely the element in the
        even-numbered positions in the array arr.
        
        Ex/ {5,2,3,10,2} will return {5,3,2}
        
        Note: method should work for arrays of both odd/even length.
        Empty & Singleton arrays with one element.*/

        int[] result = new int[((arr.length+1)/2)];
        int j = 0;

        for(int i=0; i < arr.length; i++){

            if(i%2==0){

                result[j] = arr[i];
                j++;
            }
        }

        return result;
    }

    public static int[][] createZigZag(int rows, int cols, int start){

        /*Creates & returns new 2d-integer array. Returned array must
        have the correct number of rows that each have exactly cols columns
        Array must contain the numbers:
        start, start+1, ..., start + (rows*cols-1) in its rows in 
        sorted order, except elements in odd-numbered row must be listed
        in descending order.
        
        Ex/ rols=4, cols=5, start=4. Method should create and return
        2d array of the content:
        4 5 6 7 8
        13 12 11 10 9
        14 15 16 17 18
        23 22 21 20 19
        */

        int[][] result = new int[rows][cols];

        for(int r=0; r < rows; r++){

            if(r%2 == 0){

                for(int c=0; c < cols; c++){

                    result[r][c] = start;
                    start++;
                }

            }else{

                for(int c=cols-1; c >= 0; c--){

                    result[r][c] = start;
                    start++;
                }
            }
        }

        return result;

    }

    public static int countInversions(int[] arr){

        /*Inside an array, inversion is a pair of 2 positions i<j
        so that arr[i] > arr[j]. If an array is sorted in ascending order,
        it has zero inversions, whereas an n-element array sorted
        in reverse order has n(n-1)/2 inversions, the largest number possible.
        
        Method should count inversions inside given arr & return count.
        
        Note: should work for arrays of all length including 0 & 1.
        
        */

        int count = 0;

        for(int i=0; i< arr.length; i++){

            for(int j=i+1; j<arr.length; j++){

                if (arr[i] > arr[j]){

                    count++;
                }
            }
        }

        return count; 
    }
}
