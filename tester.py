import subprocess
import os

MAIN_RESULT = "query{}-result.tsv"
YOUR_RESULT = "query{}-your-result.tsv"
SQL = "query{}.sql"
USER = input("ENTER your username (Empty means root): ") or "root"
PASSWORD = input("Enter your password: ")

for test_num in range(1, 16):
    test_num = str(test_num).zfill(2)

    if YOUR_RESULT.format(test_num) in subprocess.run(["ls"], capture_output=True, text=True).stdout:
        os.remove(YOUR_RESULT.format(test_num))
    run_queries = subprocess.run(f"sudo mysql -u {USER} -p{PASSWORD} counties < {SQL.format(test_num)} > {YOUR_RESULT.format(test_num)}", 
                    shell=True, capture_output=True)
    
    diff = subprocess.run(f"diff {MAIN_RESULT.format(test_num)} {YOUR_RESULT.format(test_num)}", 
                            capture_output=True, shell=True, text=True)

    if diff.stdout != "" and diff.stderr == "":
        print("you messed up test:", test_num, "try it whit this command:")
        print(f"diff {MAIN_RESULT.format(test_num)} {YOUR_RESULT.format(test_num)}")
    elif diff.stderr != "":
        print(diff.stderr)
    else:
        print(f"Test {test_num} passed!")
