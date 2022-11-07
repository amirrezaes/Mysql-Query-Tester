# Mysql-Query-Tester
A tool to automate generating and comparing mysql queries


You will be asked for database username and password on each run.

This script assums you have not changed the original file names and the script is in same folder as assignment files; has only been tested in unix enviroment.

The script will run the queris and compare the resulted output with the desired ones.

     python3 tester.py
     
     ENTER your username (Empty means root):
     Enter your password: 
     Test 01 passed!
     Test 02 passed!
     Test 03 passed!
     Test 04 passed!
     Test 05 passed!
     Test 06 passed!
     Test 07 passed!
     Test 08 passed!
     Test 09 passed!
     Test 10 passed!
     you messed up test: 11 try it whit this command:
     diff query11-result.tsv query11-your-result.tsv
     Test 12 passed!
     Test 13 passed!
     Test 14 passed!
     Test 15 passed!
