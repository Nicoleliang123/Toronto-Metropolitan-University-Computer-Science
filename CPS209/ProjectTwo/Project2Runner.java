/**
 * Project 2: Mini Paint App
 * Apr. 5th 2026
 * 
 * Description:
 * This program is an interactive mini paint drawing application built using
 * Java Swing.
 * It allows users to draw circles, rectangles, and lines on a canvas using
 * mouse input. Users can select the type of shape and color using color picker.
 * Canvas can be cleared through button, shape selection through dropdowns and
 * Color picker, prompting to a new panel.
 *
 * Swing Components:
 * - JFrame: Main window
 * - JPanel: Drawing canvas
 * - JButton: Clear button and color picker button
 * - JComboBox: Shape selector dropdown
 *
 * 2D Graphics:
 * Shapes are drawn using Graphics methods such as drawOval(), drawRect(),
 * and drawLine(), stored in an ArrayList and rendered in paintComponent()
 * method.
 *
 * Event Listeners:
 * - ActionListener: Used for clear button and color picker button
 * - MouseListener: Used to detect mouse press and allow users to draw shapes
 * accordingly
 *
 * Brief Instructions:
 * 1. Select a shape from the dropdown menu.
 * 2. Click and drag on the canvas to draw.
 * 3. Click "Pick Color" to change drawing color.
 * 4. Click "Clear" to erase all shapes and refresh canvas panel.
 */

public class Project2Runner {

    public static void main(String[] args) {
        new MiniPaintApp();
    }
}