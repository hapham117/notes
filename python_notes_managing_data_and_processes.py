# Summary:
    # input(): A Python function that allows user input. Input function always returns a string.
    # I/O streams: The basic mechanism for performing input and output operations in your programs. Read more below
    # Redirection of I/O streams:
        # The process of sending a stream to a different destination. Read more below.
    # Shell: A command-line interface used to interact with the OS.
        # env: A shell command to see all the environment variables.
            # Values of variables can be read from Python scripts using os.environ.get()
            # New environment variables can be created:
                # FRUIT=Pineapple
            # These can be exported too:
                # export FRUIT=Pineapple
        # echo: To print out texts and values of environment variables. Use $ as prefix for variables.
            # echo $PATH
        # PATH:
            # The shell uses this environment variable to figure out where to look for executable files.
        # sys.argv:
            # The Python scripts that we call can take arguments through the shell command-line.
        # Exit status:
            # The value returned by a program to the shell. This value is called exit code.
        # who:
            # Prints the users currently logged into a computer.
        # Bash script:
            # Bash is an acronym for 'Bourne-Again SHell, a pun on Stepehn Bourne.
            # Example using who, ps, free and uptime commands. See below.
        # Pipes | :
            # Connect the output of one program to the input of another in order to pass data between programs. Read more below.
        # if:
            # Bash' if statement takes the exit code as argument and checks if the code is 0 (success). See more below.
        # test:
            # A command that evaluates the conditions received and exits with zero when they're true and with one when they're false. See more below.
        # while:
            # While loop in bash. See more below for example and syntax.
        # for:
            # For loop in bash. See more below for example and syntax.
        # basename:
            # Takes a filename and its extension and then returns the name without the extension. Read more below.            
        # cut:
            # Like split() in Python. Examples below.
    # Subprocess module (Python module):
        # Allows us to execute system commands within a Python script, using functions provided by the subprocess module.
    # Filtering log files with Regex. Read more below.
    # Signals:
        # Tokens delivered to running process to indicate a desired action. Read more below.
# End of summary



def input_output_error_streams():
    # I/O streams: The basic mechanism for performing input and output operations in your programs.
    # In other words, a way for the program to show and receive data.
    # Most OS supply three different I/O streams by default each with a different purpose:
        # STDIN: standard input stream
        # STDOUT: standard output stream
        # STDERR: standard error stream
    # When using the Python's input() function, we're using the STDIN stream.
    # STDOUT generally takes the form of text displayed in a terminal.
    # STDERR displays output like STDOUT, but is used specifally as a channel to show error messages and diagnostics from the program.
    
    # Redirection of I/O streams:
        # The process of sending a stream to a different destination.
        # For example, we can redirect the STDOUT of a Python script to a text file instead of echoing on the screen. We'll use the > :
            # Here are 2 examples:
                # ./stdout_example.py > new_file.txt
                # echo "These are the contents of the file" > my_file.txt
            # Everytime we do this, the content of new_file.txt will be overwritten.
        # To append an output to a text file that already has content, use the >>
            # ./stdout_example.py >> new_file.txt
        # We could also use the content of a file as STDIN. We do this with < :
            # ./streams_err.py < new_file.txt
        # STDERR can also be redirected. For this, we'll use 2> :
            # Example:
                # ./streams_err.py < new_file.txt 2> error_file.txt
            # The STDERR will now be redirected to the error_file.txt instead of the screen.
            # The number 2 in 2> represents the file descriptor of the STDERR stream. In this context you can think of a file descriptor as a kind of variable pointing to an I/O resource. In this case the STDERR stream.
            
        # Python example:
                # #!/usr/bin/env python3
                # import sys
                # for line in sys.stdin:
                    # words = line.strip().split()
                    # print(" ".join([word.capitalize() for word in words]))
            # Then we run this Python script like so:
                # cat story.txt | ./capitalize_words.py
    pass
# input_output_error_streams()

# Shell: A command-line interface used to interact with the OS.
    # The most commonly used shell on Linux is called Bash.
    # Other popular shells are Zsh and Fish
    # Python programs get executed inside a shell command-line environment.
    # The variables set in that environment (environment variables) are another source of information that we can use in our scripts.
    
    # env: A shell command to see all the environment variables.
        # The values of these variables can be read from a Python script.
        # This is done by using the environ.get() method from the os module:
            # print("HOME: " + os.environ.get("HOME", ""))
            # This get method is a dictionary method. It's a bit similar to how we've been accessing dictionary values up until now. The difference is what happens when the values isn't present. When we retrieve a value from a dictionary using the key as in OS.environ[HOME] and the key isn't present, we get an error. If we use a getMethod instead, we can specify what value should be returned if the key isn't present. The getMethod allows us to specify a default value when the key that we're looking for isn't in the dictionary.
        
        # To assign a value to a environment variable (note that there are no spaces):
            # FRUIT=Pineapple
        # If we want this value to be seen in the shell when we use any commands that we call, use:
            # export FRUIT=Pineapple
    
    # echo: To print out texts and values of environment variables. Use $ as prefix for variables.
        # echo $PATH
        
    # PATH:
        # The shell uses this environment variable to figure out where to look for executable files, and we call them while specifying a directory.
        # All those directories listed there are where the shell will look for programs.
        # Example: When we call Python 3 program, the shell checks each of the directories listed in the path variable in order, and when it finds a program called Python 3, it executes it.
        
    # sys.argv: The Python scripts that we call can take arguments through the shell command-line.
        # Example:
            # ./python_script.py arg1 arg2 arg3
            
        # In the Python script we can extract these arguments from the sys module using sys.argv:
            # import sys
            # print(type(sys.argv))
                # <class 'list'>
            # print(sys.argv)
                # ['python_script.py', 'arg1', 'arg2', 'arg3']
            # print(sys.argv[1])
                # arg1
                
    # Exit status:
        # The value returned by a program to the shell. This value is called exit code.
        # In all Unix-like OS the exit status of the process is zero when the process succeeds and different than zero if it fails. The actual number returned gives additional info on what kind of error the program encountered.
        
        # In the shell, to see exit status of the last executed program, we can use:
            # echo $?
            
    # who:
        # Prints the users currently logged into a computer.
    # ps:
        # List all current running processes.
    # free:
        # Amount of free secondary memory.
    # uptime:
        # Tells you how long the machine has been on.
    # globs:
        # Globs are characters that allow us to create list of files.
        # The * and ? are the most commong globs. Example:
            # echo *.py
            # This returns all files ending with .py
            # echo ?????.py
            # This returns all files where the file name is exactly 5 characters long.
        
    # Bash script:
        # Bash is an acronym for 'Bourne-Again SHell, a pun on Stepehn Bourne.
        # Save bash scripts with the .sh extension. Like this: 'my_bash_script.sh'.
        # Example using who, ps, free and uptime commands.
            # line="------------------------------"
            # #!/bin/bash
            # echo "Starting at: $(date)"; echo $line
            # echo "UPTIME"; uptime; echo $line
            # echo "FREE"; free; echo $line
            # echo "WHO"; who; echo $line
            # echo "Finishing at: $(date)""
        # Example 2 (Note that there are no spaces when creating a variable in bash scripting):
            # example=hello
            # echo $example
        
    # Pipes | :
        # Connect the output of one program to the input of another in order to pass data between programs.
        # Using pipes, you can connect multiple scripts, commands, or other programs together into a data processing pipeline.
        # Example 1:
            # ls -l | less
        # Example 2:
            # cat spider.txt | tr ' ' '\n' | sort \ uniq -c | sort -nr | head
        # Example 3:
            # https://i.gyazo.com/4d2d9a2d96fa34fd96d9e20b97e23bc5.png
            
    # if:
        # Bash' if statement takes the exit code as argument and checks if the code is 0 (success). Example: 
            # #!/bin/bash
            # if grep "127.0.0.1" /etc/hosts; then
                # echo "Everything ok"
            # else
                # echo "ERROR! 127.0.0.1 is not in /etc/hosts"
            # fi
        # To check whether a condition is true of false, use if in combination with 'test' or [ condition ].
        
    # test:
        # A command that evaluates the conditions received and exits with zero when they're true and with one when they're false.
        # Example 1:
            # if test -n "$PATH"; then echo "Your path is not empty"; fi
            # -n checks whether a string variable is empty or not.
        # Example 2:
            # if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
            # This is the same as example 1, but different syntax. Note that there has to be a space before the closing square bracket.
            
    # while:
        # While loop in bash.
        # Example, counting 1 to 5:
            # #!/bin/bash
            # while [ $n -le 5 ]; do
                # echo "Iteration number $n"
                # ((n+=1))
            # done
        # The double parentheses ((n+=1)) let's us do arithmetic operations with our variables.
        # Also note the -le. This means less or equeal, similar to <= in Python. Some other but not all equality operators are:
            # -eq (equal to)
            # -ne (not equal to)
            # -le (less or equal)
            # -lt (less than)
            # -ge (greater or equal)
            # -gt (less than)
            # -ot (older than)
            # -e (does file exist)
            # -f (is a file)
            # -d (is a directory)
        # https://blog.100tb.com/scripting-if-comparison-operators-in-bash
        
        # Example 2:
            # #!/bin/bash
            # n=0
            # command=$1
            # while ! $command && [ $n -le 5 ]; do
                # sleep $n
                # ((n=n+1))
                # echo "Retry #$n"
            # done;
        # Note the $ sign at 'command=$1'. We're getting the value of a command line argument using the $1. This is what we use in Bash to access the first command line argument. This is similar to Python's sys.argv[1]
        
    # for:
        # For loop in bash.
        # Example 1:
            # #!/bin/bash
            # for file in *.HTM; do
                # name=$(basename "$file" .HTML)
                # echo mv "$file" "$name.html"
            # done
        # Note that the variable "$file" is surrounded by double quotes. This allows the command to work even if the file has spaces in its name.
        # Also note that we write echo before the mv command. This is to test if there are any bugs in the script. If it works without any bugs, then remove this echo and just let the script run the mv command.
        # Example 2:
            # #!/bin/bash
            # for logfile in /var/log/*log; do
                # echo "Processing: $logfile"
                # cut -d ' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
            # done
        
    # basename:
        # Takes a filename and its extension and then returns the name without the extension.
        # Example:
            # basename index.HTM .HTM
                # index
                
    # cut:
        # https://www.geeksforgeeks.org/cut-command-linux-examples/
        # Like split() in Python.
        # Syntax:
            # cut OPTION... [FILE]...
        
        # Example 1:
            # cut -b 1,2,3 state.txt

        # Example 2:
            # tail /var/log/syslog | cut -d ' ' -f5-
        # -d is the delimeter.
        # ' ' is what we want to use to cut/split. This goes with -d.
        # -f5- print the 5th field number.
        
        # Example 3:
            # cut -d ' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head


def my_subprocess():
    # https://docs.python.org/3/library/subprocess.html
    # Subprocess module (Python module):
    # Allows us to execute (external) system commands within a Python script, using functions provided by the subprocess module.
    # To run the externam command, a secondary environmet is created for the child process or subprocess where the command is executed. While the parent process, which is or script, is waiting on the subprocess to finish, it's blocked, which means that the parent can't do any work until the child finishes. 
    
    # Run this code in an online Python ide
    import subprocess
    subprocess.run(['date'])
        # Fri Sep 25 21:12:29 UTC 2020
    subprocess.run(['sleep', '2'])
    print('Hi')
    
    subprocess.run(['ls', '../../..', '-la'])
    
    # capture_output=True: To get the standard output that this command returns.
    result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
    print(result.returncode)
    print(result.stdout)
    print(result.stdout.decode().split())
    print(result.stderr)
my_subprocess()

# Filtering log files with Regex:
    # Example:
        # import sys
        # logfile = sys.argv[1]
        # with open(logfile as f):
            # for line in f:
                # if "CRON" not in line:
                    # continue
                # print(line.strip())
                
# Signals:
    # Tokens delivered to running process to indicate a desired action.
    # Example:
        # ping google.nl
    # Then we press CTRL+C to stop this process. It'll stop and print some stats after it stopped.
        # Ping statistics for 2a00:1450:400e:805::2003:
            # Packets: Sent = 18, Received = 18, Lost = 0 (0% loss),
        # Approximate round trip times in milli-seconds:
            # Minimum = 7ms, Maximum = 17ms, Average = 10ms
        # Control-C
    # What's happening behind the scenes is the process received a signal indicating that we wanted it to stop. When that signal's received, the process does whatever it needs to finish cleanly.