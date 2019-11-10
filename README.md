# sitzfleisch

These files are meant to take a .csv export of nightly projections from https://www.linestarapp.com for the sports of basketball and hockey.

After the user downloads the raw .csv from linestar, these apps clean the data and format them into a new .csv which can then be easily manipulated in Excel

These scripts do a few things:
  1. Find standard deviations by subtracting projected cielings from projected floors.
  2. Find target scores based on salary for tournaments and cash games.
    a. hockey cash game target is 3 times the salary divided by 1000
    b. hockey tournament target is 5 times the salary divided by 1000
    c. basketball cash game target is 5 times the salary divided by 1000
    d. basketball tournament target is 7 times the salary divided by 1000
    
 Once this is done there will be a new .csv file created with the new values and column names.  
