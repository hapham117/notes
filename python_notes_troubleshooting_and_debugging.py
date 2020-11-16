# Summary:
    # Troubleshooting
    # Debugging
    # Some tools for troubleshooting
        # To show ongoing network connections
        # To show the numbers and types of resources
        # To show system calls made by a program
        # To look at the library calls made by a program
        # To show the content of a very large file
    # Debugger
    # Reproduction case
    # Location of logs on 3 different OS
    # Intermittend issues
    # Searching techniques:
        # Linear search
        # Binary search
    # Bisecting
    # git bisect <subcommand> <options>
    # wc (UNIX command)
    ## Activity Monitor (MacOS)
    ## Resource Monitor and Performance Monitor (Windows)
    # Cache
    # Memory swapping
    # Memory leak
    # Garbage collector
    # Memory profiler
    # Profiler
    # Expensive actions
    # Data structures, and their pros and cons:
        # Lists
        # Dictionaries
    # Expensive loops and how to avoid them
    # time <executable script> (UNIX command)
    # Concurrency
    # Threads
    # Executor
    # Futures module
    # Wrapper
    # Watchdog
    # netstat (bash command)
    # Segmentation fault / General protection fault
    # Pointers
    # Debugging symbols
    # Undefined behavior
    # Valgrind
    # Dr. Memory
    # Traceback
    # PDB
    # logging (Python module)
    # Core files
    # backtrace (bash command)
    # next (bash command)
    # Latency
    # Bandwith
    # Traffic shaping
    # uxterm
    # Scroll buffer
    # guppy3 (Python module)
    # Eisenhower Decision Matrix
    
    
# Troubleshooting:
    # The process of identifying, analyzing, and solving problems.
    # Generally we say troubleshooting when we're fixing problems in the system running the application.
    
# Debugging:
    # The process of identifying, analyzing, and removing bugs in a system.
    # Generally we say debuggin when we're fixing the bugs in the actual code of the application.
    
# Some tools for troubleshooting:
    # ionice
    # rsync
        # rsync -bwlimit
    # Trickle (program to limit the bandwith being used)
    # nice (command):
        # When a process is started, it'll start with priority 0 (out of 19). 0 is the highest priority.
        # Using nice, we can start a process with a different priority number.
        # Reduce the priority of the process and accessing the CPU.
    # renice (command):
        # Changing the priority of a process that's already running.
    # locate <file name> (command):
        # Returns the path to the given file name. Locate is faster than the find command.
    # pidof <process name> (command):
        # Stands for "Process ID of ..."
        # Shows a list of PID of the given process name.
    # To show ongoing network connections:
        # tcpdump
        # Wireshark
    # To show the numbers and types of resources:
        # ps (shows a snapshot of the current processes)
        # top
        # free
        # iotop (shows the most disk IO usage)
        # iftop (shows the current traffic on the network interfaces)
    # Input/Output operations:
        # iostat
    # Virtual memory operations:
        # vmstat
    # To show system calls made by a program:
        # System call:
            # System call (or syscall) is the programmatic way in which a program requests a service from the kernel of the operating system on which it is executed.
            # Calls that the programs running on our computer make to the running kernel.
        # strace (pronounced s-trace)
            # strace -o <file> <something that produces an output>:
                # Store the output into a file and then browse the contents of that file.
                # Example:
                    # strace -o failure.strace ./purplebox.py
    # To look at the library calls made by a program:
        # ltrace (pronounced l-trace)
    # To show the content of a very large file:
        # less
            # Use the / to search for a keyword while using less.
    # ab (Apache Benchmark):
        # Server load tester
        # https://httpd.apache.org/docs/2.4/programs/ab.html
        # Example:
            # ab -n 500 https://www.parkeerwekker.nl
            # This creates 500 request to given link.

# Debugger:
    # Let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific conditino is met, and more.
    
# Reproduction case:
    # A clear description of how and when the problem appears.
    # An instruction showing how to reproduce the problem/bug.
    
# Location of logs on 3 different OS:
    # Linux:
        # System logs:
            # /var/log/syslog
        # user-specific logs like the .xsession-error:
            # ~/.xsession-errors
    # MacOS:
        # /Library/Logs
    # Windows:
        # Use the Event Viewer tool.

# Intermittent issues:
    # Issues that only happen now and then or a bug that comes and goes.
    # Inconsistent bug.
    # This happens mostly when resources are not handled correctly (memory, cpu usage, network etc)
    
    # Heisenbug:
        # Nicknamed in honor of Werner Heisenberg.
        # He's the scientist that first described the observer effect.
    
    # Observer effect:
        # Observing a phenomenon alters the phenomenon.
        
# Searching techniques:
    # Linear search:
        # One way to search for an element in a list.
        # The longer the list, the longer it'll take.
        # Example:
            # def linear_search(list, key):
            #     """If key is in the list returns its position in the list,
            #     otherwise returns -1."""
            #     for i, item in enumerate(list):
            #         if item == key:
            #             return i
            #     return -1

    # Binary search:
        # https://www.geeksforgeeks.org/binary-search/
        # If the list is sorted, we can make the decision about the position of the elements in the list.
        # The first thing we do is compare the name that we're looking for with the element in the middle of the list and check if it's equal, smaller, or bigger. If it's smaller, we know that the element we're looking for must be in the first half of the list. If it's bigger we know that it's in the second half of the list. And then keep doing the same thing again and again until we find the element.
        # Binary search is a lot faster than linear search when looking for an element in long lists.
        # But for this to work, the list needs to be sorted.
        # So the downside of binary search is that we have to sort the list first before we can use this technique, and sorting make take a lot of time.
        # Only use this teqchnique when you're planning to search in this same long list multiple times. For example, 2 elements. Otherwise, linear search is simpler and faster.
        # Example:
            # def binary_search(list, key):
            #     """Returns the position of key in the list if found, -1 otherwise.

            #     List must be sorted.
            #     """
            #     left = 0
            #     right = len(list) - 1
            #     while left <= right:
            #         middle = (left + right) // 2
                    
            #         if list[middle] == key:
            #             return middle
            #         if list[middle] > key:
            #             right = middle - 1
            #         if list[middle] < key:
            #             left = middle + 1
            #     return -1
            
# Bisecting:
    # A debug technique where you keep dividing the possible source of problems by 2.
    # Remember how I used to debug on my windows pc by unchecking half of the startup programs and then restarting the pc. And keep doing this until I narrow down what the source is.
    # Example:
        # wc -l contacts.csv
            # >> 100 contacts.csv
        # head -50 contacts.csv | ./import.py --server test
            # >> Import error
        # head -50 contacts.csv | head -25 | ./import.py --server test
            # >> Import successful
        # head -50 contacts.csv | tail -25 | ./import.py --server test
            # >> Import error
        # head -50 contacts.csv | tail -25 | head -13 | ./import.py --server test
            # >> Import successful
        # head -50 contacts.csv | tail -25 | tail -12 | head -6 | ./import.py --server test
            # >> Import error
        # head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3 | ./import.py --server test
            # >> Import error
        # head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3
            # >> Mechelle S. Fischer, "P.O. Box 548, 5515 In Avenue",Bulgaria,(766) 353-8154,836079-3486
            # >> Harding V. Berry,Ap #818-800 Elit. Avenue,Liberia,(182) 889-870,73573-1674
            # >> Rhona K, England,Ap #193-1392 Sit Road,"Virgin Islands, United States",(151) 405-5437,439017-6784
    
# git bisect <subcommand> <options>:
    # git-bisect - Use binary search to find the commit that introduced a bug
    # https://git-scm.com/docs/git-bisect
    
# wc (UNIX command):
    # wc stands for "word count".
    # The wc command in UNIX is a command line utility for printing newline, word and byte counts for files. It can return the number of lines in a file, the number of characters in a file and the number of words in a file. It can also be combine with pipes for general counting operations.
    # https://www.geeksforgeeks.org/wc-command-linux-examples/
    
# head -<number>:
    # Example:
        # head -15
            # Prints the first 15 lines in a file.
    # The same applies to the "tail" command.
    
# Cache:
    # Stores data in a form that's faster to access than its original form.
    
# Memory swapping:
    # Memory swapping is a memory reclamation method wherein memory contents not currently in use are swapped to a disk to make the memory available for other applications or processes. The exact state or "page" of memory is copied to the disk to make the data contiguous and easy to restore later.
    
# Memory leak:
    # Memory which is no longer needed is not getting released.
    # A chunk of memory that's no longer needed is not released.
    
# Garbage collector:
    # In charge of freeing the memory that's no longer in use.
    
# Memory profiler:
    # A tool to figure out how the memory is being used.
    
# Profiler:
    # A tool that measures the resources that our code is using, giving us a better understanding of what's going on.
    # Using tools like these, we can see which functions are called by our program, hwo many times each function was called and how much time are programs spent on each of them.
    # Examples:
        # cProfile (to analyze a Python program)
            # cProfile counts function calls.
        # gprof (to analyze a C program)
        # pprofile3 (to analyze a Python program)
        
# Expensive actions:
    # Those that can take a long time to complete.
    # Expensive operations include parsing a file, reading data over the network or iterating through a whole list.

# Data structures, and their pros and cons:
    # Lists:
        # Sequences of elements. We can add, remove, or modify elements in them, and we can iterate through the whole list to operate on each of the elements.
        # Different programming languages call them differently:
            # ArrayList in Java
            # Vector in C++
            # Array in Ruby and JavaScript
            # Slice in Go
        # All these names refer to the same data structure that's fast to add or remove elements at the end. But adding or removing elements in the middle can be slow because all the elements that follow need to be repositioned.
        # It's fast to access the element in a specific position in the list, but finding an element in an unknown poistion requires going through the whole list. This can be super slow if the list is long.
        
    # Dictionaries:
        # Store key-value pairs. We add data by associating a value to a key, and then we retrieve a value by looking up a specific key.
        # Different programming languages call them differently:
            # HashMap in Java
            # Unordered Map in C++
            # Hash in Ruby
            # Map in Go
        # The map part in those names comes from how we're creating a mapping between a key and a value.
        # The hash part comes from the fact that to make the structure efficient, a hashing function is used internally to decide how the elements will be stored.
        # The main characteristic of this structure is that it's super fast for looking up keys.
        # Once we have our data stored in a dictionary, we can find the value associated to a key in just one operation.
        
    # As a rule of thumb:
        # If you need to access elements by position, or will always iterate through all the elements, use a list to store them.
        # On the flip side, if we need to look up the elements using a key, we'll use a dictionary.
        
# Expensive loops and how to avoid them:
    # If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop.
    # Make sure that the list of elements that you're iterating through is only as long you really need it to be.
    # Another thing to remember about loops is to break out of the loop once you've found what you were looking for.
    
# time <executable script> (UNIX command):
    # Time prints the total duration to execute a file. It prints out 3 values:
        # real:
            # The amount of actual time that it took to execute the command.
            # This value is sometimes called wall-clock time because it's how much time a clock hanging on the wall would measure no matter what the computer's doing.
        # user:
            # The time spent doing operations in the user space.
        # sys:
            # The time spent diong system-level operations.
        
    # The values of user and sys won't necessarily add up to the value of 'real' because the computer might be busy with other processes.
    
# Concurrency:
    # Parallel execution. The ability of doing two or more things at the same time by splitting the work load to different cores of the cpu.
    
# Threads:
    # Let us run parallel tasks inside a process. This allows threats to share some of the memory with other threads in the same process. Since this isn't handled by the OS, we'll need to modify our code to create and handle the threats. For that, we'll need to look into how the programming language we're using implements threading.
    # In Python, we can use the Threading or AsyncIO modules to do this. These modules let us specify which parts of the code we want to run in separate threads or as separate asynchronous events, and how we want the result of each to be combined in the end.
    
# Executor:
    # The process that's in charge of distributing the work among the differen workers.
    
# Futures module:
    # Provides a couple of different executors; one for using threads and another for using processes.
    # ThreadPoolExecutor (module)
    # Example:
        # executor = futures.ThreadPoolExecutor() 
        # executor.submit(process_file, root, basename)
    
        # executor.shutdown()
        
        # executor = futures.ProcessPoolExecutor()
    
    # Threads use a bunch of safety features to avoid having two threads that try to write to the same variable. And this means that when using threads they may end up waiting for their turn to write to variables for a few miliseconds, adding up to the small difference between the two approaches (ProcessPoolExecutor() being the other approach).

# Wrapper:
    # A function or program that provides a compatibility layer between two functions or programs, so they can work well together.
    
# Watchdog:
    # A process that checks whether a program is running and, when it's not, starts the program again.
    
# netstat:
    # a useful tool for checking your network configuration and activity. It is in fact a collection of several tools lumped together.
    
# Segmentation fault / General protection fault:
    # A process trying to read or write to a memory address outside of the valid range.

# Pointers:
    # The variables that store memory addresses. Think of C and C++.
    
# Debugging symbols:
    # On top of the information that the computer uses to execute the program, the executable binary needs to include extra information needed for debugging, like the names of the variables and functions being used. These symbols are usually stripped away from the binaries that we run to make them smaller.
    
# Undefined behavior:
    # The code is doing something that's not valid in the programming language.
    
# Valgrind:
    # A very powerful tool that can tell us if the code is doing any invalid operations, no matter if it crashes or not.
    # This tool is available on Linux and MacOS.
    
# Dr. Memory:
    # Similar tool like Valgrind for Windows and Linux.
    
# Traceback:
    # Shows the lines of the different functions that were being executed when the problem happened.
    
# PDB and GDB:
    # Interactive debugger which lets us do all the typical debugging actions like executing lines of code one by one or looking at how the variables change values.
    # PDB is for Python scripts.
    
# logging (Python module):
    # https://realpython.com/python-logging/
    # A debugging module that let's you set how comprehensive you want your code to be.
    
# Core files:
    # Store all the information related to the crash so that we, or someone else, can debug what's going on.
    # It's like taking a snapshot of the crash when it happens to analyze it later.
    # We need to tell the OS that we want to generate those core files. We do that with the ulimit command.
    # Example:
        # ulimit -c unlimited
        
# backtrace (bash command):
    # Show the full backtrace of a crashed script/program.
    
# next (PDB command):
    # Runs each of the instructions in a file one by one.

# Latency:
    # The delay between sending a byte of data from one point and receiving it on the other.
    
# Bandwith:
    # How much data can be sent or received in a second.
    
# Traffic shaping:
    # A way of  marking the data packets sent over the network with different priorities to avoid having huge chunks of data use all of the bandwith.
    
# uxterm:

# Scroll buffer:
    # Feature that lets us scroll up and see the things that we executed and their output.
    
# guppy3 (Python module):
    # https://pypi.org/project/guppy3/
    # A Python Programming Environment & Heap analysis toolset.
    
# Eisenhower Decision Matrix:
    # Also referred to as Urgent-Important Matrix, helps you decide on and prioritize tasks by urgency and importance, sorting out less urgent and important tasks which you should either delegate or not do at all.
