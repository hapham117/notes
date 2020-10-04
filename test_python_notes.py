# Summary:
    # input(): A Python function that allows user input. Input function always returns a string.
    # I/O streams: The basic mechanism for performing input and output operations in your programs. Read more below
    # Redirection:
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
    # Subprocess module (Python module):
        # Allows us to execute system commands within a Python script, using functions provided by the subprocess module.
    # Filtering log files with Regex:
    # Pipes | :
        # Connect the output of one program to the input of another in order to pass data between programs.
        # Using pipes, you can connect multiple scripts, commands, or other programs together into a data processing pipeline. Example:
            # ls -l | less
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
    
    # Redirection:
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