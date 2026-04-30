import java.awt.BasicStroke;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import javax.swing.JPanel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;

public class Head extends JPanel {

    private boolean eyesOpen;

    public Head() {
        setPreferredSize(new Dimension(500, 500));

        eyesOpen = false;

        // Mouse listener
        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                eyesOpen = true;
                repaint();
            }

            @Override
            public void mouseExited(MouseEvent e) {
                eyesOpen = false;
                repaint();
            }
        });
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D) g;

        // Smooth edges
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        // Head (circle)
        Ellipse2D head = new Ellipse2D.Double(100, 100, 300, 300);
        g2.draw(head);

        if (eyesOpen) {
            // Open eyes (filled circles)
            Ellipse2D leftEye = new Ellipse2D.Double(170, 200, 40, 40);
            Ellipse2D rightEye = new Ellipse2D.Double(290, 200, 40, 40);
            g2.fill(leftEye);
            g2.fill(rightEye);
        } else {
            // Closed eyes (lines)
            g2.setStroke(new BasicStroke(3));
            Line2D leftEye = new Line2D.Double(170, 220, 210, 220);
            Line2D rightEye = new Line2D.Double(290, 220, 330, 220);
            g2.draw(leftEye);
            g2.draw(rightEye);
        }

        // Mouth
        g2.drawArc(200, 300, 100, 50, 0, -180);
    }
}
