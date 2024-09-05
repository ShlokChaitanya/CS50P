# Tic-Tac-Toe Game

#### Video Demo: [https://youtu.be/hIuFe-6jQgc]

#### Description:
The Tic-Tac-Toe Game is a Python-based implementation of the classic two-player game, leveraging the tkinter library to create a robust graphical user interface (GUI). This project is designed to demonstrate proficiency in event-driven programming, basic AI implementation, and GUI development, combining these elements to create a fully interactive and user-friendly application.

### Core Features:
Human vs Human Gameplay: The game is primarily designed for two human players, who alternate turns to place their marks ('X' and 'O') on a 3x3 grid. The logic for determining valid moves, checking win conditions, and handling draws is implemented using straightforward control structures and algorithms, ensuring a smooth and intuitive user experience.

AI Opponent: In addition to the human vs human mode, an optional AI opponent is available. This AI is implemented with a basic random move strategy, selecting an empty cell at random for its move. While the AI does not employ advanced algorithms like minimax, it provides a foundational approach to understanding how AI can be integrated into gameplay. This component can be further extended to include more sophisticated AI strategies, such as those involving decision trees or machine learning models.

Graphical User Interface (GUI): The game's interface is built using the tkinter library, which is Python's standard interface to the Tk GUI toolkit. The GUI features a grid of buttons representing the game board, each responding to user clicks by updating the game state accordingly. The interface also includes dynamic text displays to show game status messages, such as indicating whose turn it is or announcing the winner. Upon completion of a game (whether by win or draw), the board automatically resets for a new game, demonstrating the use of event loops and callback functions in tkinter.

Event Handling and Game Logic: The game makes extensive use of tkinter's event-handling mechanisms, particularly binding functions to button click events. Each button on the grid is associated with a command that updates the game state, checks for win conditions, and handles the transition between players. The logic to determine win conditions involves iterating over possible winning combinations (rows, columns, and diagonals) and checking for consistent marks. This is a practical demonstration of control flow and conditional logic in Python.

Code Structure and Modularity: The codebase is organized into distinct functions that handle specific tasks, such as initializing the board, processing player moves, and resetting the game. This modular approach not only improves code readability
