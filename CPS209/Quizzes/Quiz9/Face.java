import javax.swing.*;
import java.awt.*;

public class Face extends JPanel {
    
    public void paintComponent(Graphics g){

        //Clear screen
        super.paintComponent(g); 

        //Head
        g.drawOval(100, 100, 200, 200); 

        //Left eye
        g.fillOval(150,150,20,20);

        //Right eye
        g.fillOval(230,150,20,20);

        //Nose
        g.drawRect(190,180,20,30);

        //Mouth
        g.drawArc(150,210, 100, 50,0,-180);

        //Hat top
        g.drawRect(140,50,120,60);

        //Hat brim
        g.drawOval(120,100,160,30);

    }

    public static void main(String[] args){

        //Window
        JFrame frame = new JFrame("Face with Hat");

        //Panel
        Face panel = new Face();

        frame.add(panel);

        frame.setSize(400,400);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setVisible(true);
    }
}
