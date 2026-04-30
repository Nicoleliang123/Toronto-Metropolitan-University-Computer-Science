public class AdvancedQuadraticEquation extends QuadraticEquation {

    /* AdvancedQuadraticEquation is the subclass(extension)
    of the superclass QuadraticEquation.

    Contains description, root classifying, vertex &
    axis of symmetry calculations
     */

    //Initalize variables private out of superclass
    private String description;

    //Constructor
    public AdvancedQuadraticEquation(double a, double b, double c, String description){

        //Call variables a,b,c through superclass QuadraticEquation
        super(a,b,c);

        //Initialize
        this.description = description; 

    }

    //Default description (constructor overload)
    public AdvancedQuadraticEquation(double a, double b, double c){
        this(a,b,c, "Advanced Quadratic"); 
    }

    //Getter/Setter for description
    public String getDescription(){

        //Return description so when getting returns it
        return description;
    }
    public void setDescription(String description){

        //Initialize this is equal to description
        this.description = description; 
    }

    //Override toString
    @Override
    public String toString(){

        //Include description and call on toString from
        //superclass QuadraticEquation
        return description + ": " + super.toString();
    }

    //Override solve to include discriminat
    @Override
    public String solve(){

        //Through getters, get discriminant value and set to new variable temporary
        double d = getDiscriminant();
        
        //Take superclass QuadraticEquation of solve
        return super.solve() + " [Discriminant = " + d + "]";
    }

    //Classify Roots method - according the discriminat earlier,
    //Return the type of root
    public String classifyRoots(){

        //Through getters, get discriminant value
        double d = getDiscriminant();
        if(d > 0){
            return "Two distinct real roots";
        }else if (d==0){
            return "One repeated real root";

        }else{
            return "Complex roots, no solution";
        }
    }

    //Vertex X/Y-coordinate method - calculates the vertex
    public double getVertexX(){
        return - getB() / (2* getA()); 
    }

    public double getVertexY(){

        double h = getVertexX();

        //formula for y-vertex coordinate
        //Using getters to reach from superclass for abc varables
        return getA() * h * h + getB() + h + getC();
    }

    //Axis of symmetry method
    public String getAxisofSymmetry(){
        return "x = " + getVertexX();
    }

    //Printing results
    public String fullProperties(){

        //Putting it all together by getting all values and indicate which is which
        return "Equation " + toString() + "\n" +
                "Solution " + solve() + "\n" +
                "Root Type: " + classifyRoots() + "\n" +
                "Vertex: (" + getVertexX() + ", " + getVertexY() + ")\n" +
                "Axis of Symmetry: " + getAxisofSymmetry(); 
    }
}
