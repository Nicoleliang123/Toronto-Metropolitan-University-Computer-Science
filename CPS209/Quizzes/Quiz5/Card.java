public class Card implements Comparable<Card> {

    //Given
    final int rank;
    final char suit;
    public Card(int r, char s){

        rank= r;
        suit = s;
    }

    //compareTo method
    @Override
    public int compareTo(Card other){

        //Check if this rank is not equal, return the difference
        //Positive = this card larger
        if(this.rank != other.rank){
            return this.rank - other.rank;
        }

        //If equal, break tie by suit order
        return suitValue(this.suit) - suitValue(other.suit);
    }

    //Convert suit chharacters to numeric values
    private int suitValue(char s){
        switch (s){

            //Smallest to largest
            case 'C': return 1;
            case 'D': return 2;
            case 'H': return 3;
            case 'S': return 4;
        }

        //Default return is invalid
        return 0;
    }

    @Override
    public boolean equals(Object obj){

        //If this is the object
        if(this == obj){
            return true;
        }

        //If obj is null or not a Card, false
        if(obj == null || !(obj instanceof Card)){

            return false;
        }

        //Casting 
        Card other = (Card) obj;

        //Cards are equal if both rank and suit match
        return this.rank == other.rank && this.suit == other.suit; 
    }

    //Numeric ranking for bigger then 10
    private String rankName(){

        //Check rank
        switch(rank){
            case 11: return "Jack";
            case 12: return "Queen";
            case 13: return "King";
            case 14: return "Ace";

            //numeric card(2-10)
            default: return String.valueOf(rank);
        }
    }

    //Conver suit letter to full name
    private String suitName(){

        //Check suit
        switch(suit){
            case 'C': return "Clubs";
            case 'D': return "Diamonds";
            case 'H': return "Hearts";
            case 'S': return "Spades";
        }

        return "";
    }

    @Override
    public String toString(){
        return rankName() + " of " + suitName();
    }

    //---------------------------------------------------------
    //Main method testing

    public static void main(String[] args){

        //To compare, equal and use order of suits and bypass of numeric (2-10)
        Card c1 = new Card(7,'H');
        Card c2 = new Card(11, 'S');
        Card c3 = new Card(7, 'H');
        Card c4 = new Card(7, 'C');

        //toString exp
        System.out.println("Card 1: " + c1); //7 of Hearts
        System.out.println("Card 2: " + c2); //Jack of Spades

        //equals exp
        System.out.println("\nEquals testing:");
        System.out.println("c1 equals c3: " + c1.equals(c3)); //TRUE
        System.out.println("c1 equals c2: " + c1.equals(c2)); //FALSE

        //compareTo exp
        System.out.println("\nComparing tests:");
        System.out.println("c1 vs c2:" + c1.compareTo(c2)); //-4
        System.out.println("c1 vs c4: " + c1.compareTo(c4)); //2
        System.out.println("c2 vs c1: " + c2.compareTo(c1)); //4
        
    }

}