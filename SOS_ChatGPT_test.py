def test_minimum_board_size():
    from tkinter import Tk
    from SOS import gui

    # Set up the GUI
    display = Tk()
    app = gui(display)
    
    # Simulate entering the minimum board size
    app.board_size_entry.delete(0)
    app.board_size_entry.insert(0, '3')
    app.start_new_game()  # Trigger the game setup

    # Check if the board is generated correctly
    assert len(app.buttons) == 3  # 3 rows
    assert all(len(row) == 3 for row in app.buttons)  # 3 columns

def test_challenging_board_size():
    from tkinter import Tk
    from SOS import gui

    # Set up the GUI
    display = Tk()
    app = gui(display)
    
    # Simulate entering a challenging board size
    app.board_size_entry.delete(0, 'end')
    app.board_size_entry.insert(0, '7')
    app.start_new_game()  # Trigger the game setup

    # Check if the board is generated correctly
    assert len(app.buttons) == 7  # 7 rows
    assert all(len(row) == 7 for row in app.buttons)  # 7 columns

def test_invalid_board_size():
    from tkinter import Tk
    from SOS import gui
    from tkinter import messagebox

    # Set up the GUI
    display = Tk()
    app = gui(display)

    # Use a spy to monitor messagebox calls
    def mock_showerror(title, message):
        assert title == "Invalid Input"
        assert message == "Size in between 3 and 12."

    messagebox.showerror = mock_showerror

    # Simulate entering an invalid board size
    app.board_size_entry.delete(0, 'end')
    app.board_size_entry.insert(0, '2')  # Invalid size
    app.start_new_game()  # Trigger the game setup

def test_select_simple_game_mode():
    from tkinter import Tk
    from SOS import gui

    # Set up the GUI
    display = Tk()
    app = gui(display)

    # Simulate selecting the simple game mode
    app.game_mode.set("Simple")  # Set the mode
    app.board_size_entry.delete(0, 'end')
    app.board_size_entry.insert(0, '3')  # Set size
    app.start_new_game()  # Trigger the game setup

    # Check game mode is set correctly
    assert app.game_mode.get() == "Simple"
    # Further checks can be implemented as needed for game rulesa