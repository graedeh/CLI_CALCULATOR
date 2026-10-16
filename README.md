# CLI Calculator and Expense Tracker

Two beginner-friendly Python command-line projects.

## Project files

-   `calculator.py` --- performs addition, subtraction, multiplication,
    and division.
-   `expense_tracker.py` --- records expense descriptions and positive
    amounts in naira, lists expenses, and calculates the total.
-   `README.md` --- instructions, limitations, and a test/demo
    checklist.

## Requirements

-   Python 3
-   No third-party packages are required.

Check Python is available:

``` bash
python3 --version
```

## Run the calculator

From the project folder:

``` bash
python3 calculator.py
```

Choose an operation from 1 to 4, enter two numbers, and read the result.
Choose `5` to exit.

### Calculator test checklist

Run these checks and record the actual results before submitting or
demonstrating:

  -----------------------------------------------------------------------
  Test              Input/action      Expected result   Actual result
  ----------------- ----------------- ----------------- -----------------
  Addition          Choose `1`; enter `Result: 10.0`    Not yet recorded
                    `8` and `2`                         

  Subtraction       Choose `2`; enter `Result: 6.0`     Not yet recorded
                    `8` and `2`                         

  Multiplication    Choose `3`; enter `Result: 16.0`    Not yet recorded
                    `8` and `2`                         

  Division          Choose `4`; enter `Result: 4.0`     Not yet recorded
                    `8` and `2`                         

  Divide by zero    Choose `4`; enter Shows a           Not yet recorded
                    `8` and `0`       divide-by-zero    
                                      error message     

  Invalid number    Enter text such   Shows an          Not yet recorded
                    as `hello` when   invalid-input     
                    asked for a       message and       
                    number            returns to the    
                                      menu              

  Invalid menu      Enter a choice    Shows an          Not yet recorded
  choice            such as `9`       invalid-choice    
                                      message           

  Exit              Choose `5`        Prints a          Not yet recorded
                                      thank-you message 
                                      and exits         
  -----------------------------------------------------------------------

## Run the expense tracker

From the project folder:

``` bash
python3 expense_tracker.py
```

Choose: - `1` to add an expense - `2` to view recorded expenses - `3` to
show the total - `q` to quit

### Example demonstration

1.  Choose `1`, enter description `Lunch`, and amount `1500`.
2.  Choose `1`, enter description `Transport`, and amount `800`.
3.  Choose `2` to view the two expenses.
4.  Choose `3`. The expected total is `₦2300.00`.
5.  Choose `q` to quit.

### Expense tracker test checklist

Run these checks and record the actual results before submitting or
demonstrating:

  ----------------------------------------------------------------------------------
  Test              Input/action      Expected result              Actual result
  ----------------- ----------------- ---------------------------- -----------------
  Add valid expense Description       Expense-added confirmation   Not yet recorded
                    `Lunch`, amount                                
                    `1500`                                         

  View expenses     Choose `2` after  Shows numbered expense and   Not yet recorded
                    adding an expense amount                       

  Calculate total   Add `1500` and    `Total expenses: ₦2300.00`   Not yet recorded
                    `800`, then                                    
                    choose `3`                                     

  Empty description Try to add an     Shows a description error;   Not yet recorded
                    expense with only expense is not added         
                    spaces as                                      
                    description                                    

  Invalid amount    Enter `hello` for Shows a valid-number error;  Not yet recorded
                    amount            expense is not added         

  Zero/negative     Enter `0` or a    Shows an amount error;       Not yet recorded
  amount            negative amount   expense is not added         

  Empty list        Start the program Says no expenses have been   Not yet recorded
                    and choose `2`    recorded                     
                    before adding                                  
                    anything                                       

  Invalid menu      Enter an          Shows an invalid-choice      Not yet recorded
  choice            unsupported menu  message                      
                    option                                         

  Quit              Choose `q`        Prints a thank-you message   Not yet recorded
                                      and exits                    
  ----------------------------------------------------------------------------------

## Current limitations

### Calculator

-   Results are printed in the terminal; there is no graphical
    interface.
-   It uses floating-point numbers, so some decimal calculations may
    show small precision differences.
-   It does not keep a history of calculations.

### Expense tracker

-   Expenses are stored in memory only.
-   All expenses are lost when the program exits.
-   There is no editing or deleting of an expense yet.
-   It does not save data to a file or database.
-   It is a single-user command-line program.

## Learning record

Topics practiced in these projects:

-   Defining and calling functions
-   Parameters and return values
-   Variables and data types
-   Lists and dictionaries
-   `input()` and converting input with `float()`
-   `if`, `elif`, and `else`
-   `while` loops
-   `break` and `continue`
-   `try` and `except ValueError`
-   Validating user input
-   Adding items to a list with `.append()`
-   Looping through data with `for`
-   Formatting amounts to two decimal places with `:.2f`

## Demonstration readiness

Before a live demonstration, practice these three things without asking
an AI to write the steps for you:

1.  **Normal case:** Run each program and complete one successful task.
2.  **A mistake:** In the calculator, enter text instead of a number. In
    the expense tracker, enter an invalid amount or an empty
    description. Explain how the program handles it.
3.  **One small live code change:** Make a small change yourself, such
    as changing a menu label or changing the expense success message.
    Run the program again to show the change works.

Be ready to explain: - What each function does. - Why the program uses a
loop. - Why input is converted to a number. - What `try` and
`except ValueError` do in the calculator and expense tracker. - Why the
expense tracker passes the same `expenses` list to its functions. - Why
expense data disappears after quitting.

## Test status

The tables above are **test checklists**, not claims that all tests have
passed. Run each test yourself and replace `Not yet recorded` with the
observed result (for example, `Passed` or a short note describing a
problem). Only report tests as passed after confirming their behavior.