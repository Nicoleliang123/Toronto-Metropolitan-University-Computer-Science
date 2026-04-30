import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

//Main application window for Mini Paint App
public class MiniPaintApp extends JFrame {

    private DrawPanel canvas; // Drawing Area
    private JComboBox<String> shapeSelector; // Dropdown for shape choice
    private JButton clearButton; // Button to clear canvas
    private JButton colorButton; // Button to pick color
    private Color currentColor = Color.BLACK; // Default drawing color

    // Constructer to setup GUIs
    public MiniPaintApp() {

        // Window basic needs
        setTitle("Mini Paint App");
        setSize(600, 600);

        // Closes app on exit
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Layout manager
        setLayout(new BorderLayout());

        // Creates drawing panel to import buttons & dropdowns
        canvas = new DrawPanel();
        add(canvas, BorderLayout.CENTER); // add canvas to center

        // Create control panel for buttons & dropdown
        JPanel controlPanel = new JPanel();

        // Create dropdown menu for shap selections
        shapeSelector = new JComboBox<>(new String[] { "Circle", "Rectangle", "Line" });
        controlPanel.add(new JLabel("Shape:")); // Label text
        controlPanel.add(shapeSelector); // Add dropdown

        // Button to pick color
        colorButton = new JButton("Pick Color");
        controlPanel.add(colorButton);

        // Button to clear canvas
        clearButton = new JButton("Clear");
        controlPanel.add(clearButton);

        // Adding controls to top
        add(controlPanel, BorderLayout.NORTH);

        // Action listener for clear button
        clearButton.addActionListener(e -> {
            canvas.clearShapes(); // Remove all shapes
        });

        // Action listener for color picker
        colorButton.addActionListener(e -> {
            // Open color chooser dialog
            Color newColor = JColorChooser.showDialog(this, "Choose Color", currentColor);

            // If user selected a color
            if (newColor != null) {

                // Update the current color
                currentColor = newColor;
            }
        });

        // Show window
        setVisible(true);
    }

    // Innerclass for panel that allows drawing to occur
    class DrawPanel extends JPanel {

        // Store all shapes
        private ArrayList<Shape> shapes = new ArrayList<>();
        // Coordinates for mouse (starting position)
        private int startX, startY;

        // Constructer to set background and mouse listeners
        public DrawPanel() {

            // Canvas color
            setBackground(Color.WHITE);

            // When mouse is pressed
            addMouseListener(new MouseAdapter() {
                public void mousePressed(MouseEvent e) {

                    // Store starting X & Y
                    startX = e.getX();
                    startY = e.getY();
                }

                // When mouse is released
                public void mouseReleased(MouseEvent e) {

                    // Ending X & Y
                    int endX = e.getX();
                    int endY = e.getY();

                    // Get selected shape type
                    String selectedShape = (String) shapeSelector.getSelectedItem();

                    // Create correct shape based on users' selection
                    // Conditions:
                    if (selectedShape.equals("Circle")) {
                        shapes.add(new Circle(startX, startY, endX, endY, currentColor));
                    } else if (selectedShape.equals("Rectangle")) {
                        shapes.add(new RectangleShape(startX, startY, endX, endY, currentColor));
                    } else if (selectedShape.equals("Line")) {
                        shapes.add(new Line(startX, startY, endX, endY, currentColor));
                    }

                    // Redraw panel
                    repaint();
                }
            });
        }

        // Clears all shapes from canvas
        public void clearShapes() {

            // Remove all shapes
            shapes.clear();

            // Redraw to refresh display
            repaint();
        }

        // Draw all shapes onto panel
        protected void paintComponent(Graphics g) {
            // Clear screen
            super.paintComponent(g);

            // Loop through shapes & draw each one by one
            for (Shape s : shapes) {
                s.draw(g);
            }
        }
    }

    // Abstract base class for all shapes
    abstract class Shape {

        // Initialize coordinates & shape color
        int x1, y1, x2, y2;
        Color color;

        // Constructor to initialize shape properties
        public Shape(int x1, int y1, int x2, int y2, Color color) {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
            this.color = color;
        }

        // Abstract method each shape that needs to be implemented
        abstract void draw(Graphics g);
    }

    // Circle shape class
    class Circle extends Shape {

        public Circle(int x1, int y1, int x2, int y2, Color color) {
            super(x1, y1, x2, y2, color); // Calling parent constructor
        }

        public void draw(Graphics g) {

            // Set drawing color
            g.setColor(color);

            // Width & heigh of circle
            int width = Math.abs(x2 - x1);
            int height = Math.abs(y2 - y1);

            // Draw oval using top-left corner & size
            g.drawOval(Math.min(x1, x2), Math.min(y1, y2), width, height);
        }
    }

    // Rectangle shape class
    class RectangleShape extends Shape {

        public RectangleShape(int x1, int y1, int x2, int y2, Color color) {
            super(x1, y1, x2, y2, color);
        }

        public void draw(Graphics g) {

            // Set color
            g.setColor(color);

            // Width & Height
            int width = Math.abs(x2 - x1);
            int height = Math.abs(y2 - y1);

            // Draw rectangle
            g.drawRect(Math.min(x1, x2), Math.min(y1, y2), width, height);
        }
    }

    // Line shape class
    class Line extends Shape {

        public Line(int x1, int y1, int x2, int y2, Color color) {
            super(x1, y1, x2, y2, color);
        }

        public void draw(Graphics g) {

            // Set color
            g.setColor(color);

            // Draw line between two points
            g.drawLine(x1, y1, x2, y2);
        }
    }
}