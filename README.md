# create-a-python-application-1
Add a docstring that describes the program's function.
    In the editor, type the docstring as shown.
    As you type the three opening double quotes, PyCharm automatically provides the closing double quotes.
    You can press Enter to force a new line for formatting of your code, but the line break will not be considered to be part of the actual string.
Write code to take a user's input, then print it back to them.
    Press Ctrl+End to move to the end of the code, and press Enter until the insertion point is on line 5 as shown.
    Starting on line 5, add the following code.
    When the program runs, the user will type the name of the file to be analyzed. This statement assigns the variable user_input to whatever the user types in.
Add a print statement with a comment to explain the statement's purpose.
    Press Enter to advance to line 9, and enter the two lines shown.
    The first line, a comment, explains what the second line does.
    The second line prints the user's input to the console.
Run your Python script.
    Within the wordcount.py code window, right-click and select Run 'wordcount'.
    Note: You don't need to manually save the source code yourself. PyCharm automatically does this after any change.
    PyCharm opens the Run tool window at the bottom of the screen.
    Examine the Run window.
    Note: Many of the screen shots for this course were captured with PyCharm's Soft-Wrap setting enabled, to avoid truncating text. In this activity and others in this course, if text in the Run window is truncated on the right side of the screen, you might find it helpful to select the Soft-Wrap button to enable lines of output to wrap around automatically.
    In the Run window, you can see the command that PyCharm issued behind the scenes to run the Python interpreter (python.exe). The program file that you wanted to run (wordcount.py) was passed to Python.exe as a command-line parameter.
    Based on the source code you wrote, the Python interpreter created an executable program and ran it, and the running program has produced output in the Run         window.
    The prompt you produced using the input( ) function is displayed in the Run window.
    Click in the Run window to select it for typing. Then type Testing input and press Enter.
    Verify that Python returned your input back to you.
    Note: Process finished with exit code 0 means that Python was able to exit the program without any errors. Other exit codes like 1 or -1 would indicate errors.
Create and run multiple, consecutive input statements.
        In the editor pane, enter additional input and print statements in lines 12 through 18 as shown.
        In the Run window, select the Rerun 'wordcount' button.
        The text in the Run window is cleared, and the new version of the program runs.
Test out the program.
        At the first prompt, enter Testing input
        As before, the input is sent back to you. However, a new input prompt opens up directly after.
        At the second prompt, enter Y
        At the third prompt, enter N
        Verify that the program finishes with an exit code of zero.
        In the Run window, close the wordcount tab.
        Close the wordcount.py editor tab.
        The editor for that file is closed, but the WordCount project remains open.
Examine the directory that contains the Python source code file.
        In the Project pane, right-click wordcount.py, and select Show in Explorer.
        This command launches the Windows File Explorer program, and highlights the wordcount.py file within the project folder that you created.
Examine the contents of the project folder.
        In addition to the Python file that contains your source code, the PyCharm editor automatically created a folder named .idea, which contains the project            settings.
        Note: Normally, you would not need to directly edit the files in the .idea folder, which are maintained automatically by the IDE.
        In the File Explorer window, right-click wordcount.py and select Properties.
        This is the Python script you were just working on, saved as an individual file.
        It has the typical properties of a file, including the size, the creation date, and the default program it opens with.
        Close the wordcount.py Properties window.
Examine the project files from the command line.
        In the File Explorer address bar, select the folder icon.
        This selects the entire directory path.
        Type cmd and press Enter.
        T his will run a Windows command prompt from the current directory location.
        Examine the current directory in the command console.
        Enter the dir command.
        The wordcount.py file is shown in the list. If you were working outside of an editor like PyCharm, you might view the Python project files from the command         line, like this.
Run the program directly from the command line.
        Enter the python wordcount.py command.
        This command uses the Python interpreter directly to run your script. The script runs, and the first prompt is displayed in the command console.
        Note: When Python was installed, the directory path for the Python installation was added to the computer's environment variables so you don't have to type         the complete path every time you run a Python command.
        At the various prompts, enter input as shown.
        The program completes, and you are returned to the command line.
        Note: When running from the command line like this, the return code is not shown.
        Enter the exit command to quit the command console.
        Close the File Explorer window and return to the PyCharm IDE.

