## Overview

In this project, I developed an Anime Episode Tracker using Python. The program allows users to add anime, track episodes, search for titles, and generate statistics. This project helped me apply key programming concepts from the workshops, including command-line arguments, validation, file handling, and debugging.

---

## Workshop 7 – Command-Line Arguments and Program Structure

From Workshop 7, I learned how to use `sys.argv` to handle command-line arguments. This was a key part of my project, as my application runs entirely from the terminal.

For example, users can run commands such as:

python app.py add_anime "Naruto" Action 220 8.5

This directly uses the concept of `sys.argv`, where the program reads user input from the command line and processes it accordingly.

I also learned the importance of checking the number of arguments before using them. This helped me avoid errors such as accessing missing inputs and made my program more reliable.

---

## Workshop 8 – Validation, Testing, and File I/O

Workshop 8 helped me understand how to properly validate input, test functionality, and store data persistently.

### Validation

I applied validation techniques to ensure that user inputs are correct before being processed. For example:
- Checking that anime titles are valid
- Ensuring ratings are between 0 and 10
- Ensuring episode numbers are greater than 0

This improved the robustness of my program and prevented invalid data from being stored.

---

### File I/O (CSV Storage)

I used file handling techniques to store anime and episode data in CSV files. This was implemented through the `FileManager` class.

This ensures that:
- Data is saved even after the program stops running
- The program can reload saved data when it starts again

This directly reflects what I learned about file persistence and CSV handling.

---

### Testing and Debugging

Although I did not fully implement automated testing with pytest, I applied the testing mindset from the workshop by manually testing different commands.

For example:
- Testing adding anime
- Testing searching functionality
- Testing invalid inputs

This helped me identify and fix errors effectively.

---

## Challenges and Problem-Solving

During development, I encountered several issues:

### 1. Command Not Found
Initially, running `python app.py` did not work. I discovered that I needed to use `python3` instead. This helped me understand differences in environments.

### 2. Indentation Errors
I frequently encountered errors such as “unexpected indent”. This taught me how important indentation is in Python, especially within classes and functions.

### 3. Missing Imports
I faced issues such as:
- `is_valid_title not defined`
- `normalise_title not defined`

I resolved these by correctly importing functions from other modules, improving my understanding of modular programming.

### 4. File Naming Issues
I initially named a file incorrectly (`file.io.py`), which caused import errors. Renaming it to `file_io.py` fixed the issue and helped me understand Python file naming conventions.

---

## What I Learned

Through this project, I developed a stronger understanding of:
- Object-Oriented Programming (OOP)
- Command-line applications using `sys.argv`
- File handling with CSV
- Input validation
- Debugging and error handling

---

## Conclusion

Overall, this project allowed me to apply concepts from both workshops in a practical way. I improved my problem-solving skills and gained confidence in building structured Python applications.
