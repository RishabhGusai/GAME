# Hand Gesture Controlled Game

A fun 2D game where you control a player character using hand gestures captured through your webcam. The game uses OpenCV and Mediapipe for hand gesture detection and Pygame for the game interface.

## Features

- Real-time hand gesture detection using your laptop's webcam
- Three different control gestures:
  - ✊ Fist: Make the player jump
  - ✋ Palm: Activate power mode (immunity to obstacles)
  - ✌ Peace sign: Boost forward speed
- Score tracking
- Obstacle avoidance gameplay
- Visual feedback of detected gestures

## Requirements

- Python 3.7 or higher
- Webcam
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```bash
   python game.py
   ```
2. Two windows will appear:
   - Webcam window showing hand tracking
   - Game window with the player and obstacles

3. Use these hand gestures to control the player:
   - Make a fist (✊) to jump
   - Show your palm (✋) to activate power mode
   - Make a peace sign (✌) to boost forward

4. Avoid obstacles to score points
5. Press ESC to quit the game

## Controls

- ✊ Fist: Jump (only works when on the ground)
- ✋ Palm: Activate power mode (makes you immune to obstacles)
- ✌ Peace Sign: Speed boost (moves player forward)
- ESC: Quit game

## Tips

- Ensure good lighting for better hand gesture detection
- Keep your hand within the webcam frame
- Make clear, distinct gestures for better recognition
- Use power mode strategically to pass through difficult obstacles

## Troubleshooting

If you experience issues:

1. Check if your webcam is properly connected and accessible
2. Ensure adequate lighting in your room
3. Try adjusting your distance from the webcam
4. Verify all required packages are installed correctly

## Credits

This game uses the following technologies:
- OpenCV for webcam capture and image processing
- Mediapipe for hand gesture detection
- Pygame for game graphics and mechanics