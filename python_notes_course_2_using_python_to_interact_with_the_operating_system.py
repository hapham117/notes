# Python notes 2

# Summary:
    # What is an Operating System (OS)
    # Linux
    # PyPi (Python Package Index)
    # Compiled vs Interpreted language
    # shebang
        # #!/usr/bin/env python
        # This line will be written as the first line of a python script to tell the OS what command we want to use to execute the script.
    # Creating your own modules and submodules
    # Scalability
        # When more work is added to a system, the system can do whatever it needs to complete the work.
    # Bit-rot:
        # The process of software falling out of step with the environment.
    # Virtual Machine (VM):
        # A computer simulated through software. Simulated hardware.
    # Parsing:
        # Analyzing a file's content to correctly structure the data.
        # Using rules to understand a file or datastream as structured data.
    # CSV (Comma Separated Values)
    # File descriptor and file objects
    # Looping through a file
    # Writing a file
    # os module methods
# End of summary


# What is an Operating System (OS):
    # An OS consists of kernel and User Space.
    # The kernel is the main core of an operating system. It talks directly to the hardware and manages the system resources (network, memory, disk).
    # Users don't interact with the kernel directly, instead we interact with the User Space. The User Space is everything outside the kernel.

# Linux:
    # Linux is actually the name of the kernel (not the OS) originally developed by Linus Torvalds.
    # Linux is based on an OS developed in 1970 called Unix.
    # A lot of the tools that we interact with the Linux OS are open source versions of those originally developed for Unix.
    # This is why these tools in operating principles are usually referred to as Unix. Even though the OS we're using is called Linux.
    # Since Linux is open source, a lot of different organizations package their own versions of it.
    # These different flavors of Linux are called "distributions".
    # Some common open source Linux distributions are:
        # Ubuntu
        # Debian
        # Red Hat
        # Android (Linux based OS for mobile touchscreens)
        # Chrome OS (Unlike other distributions, Chrome OS is considered an OS in its own right.)
        
    # The Mac OS kernel and some of its user space are also based on a kernel and User space tools from the Unix family known as BSD.
    
# PyPi (Python Package Index):
    # We can browse as repository of Python modules to find the module we need.
    # It includes thousands of projects which are classified by different categories, like topic, development studies, and intended audience.
    # Use pip to install and uninstall modules in/from your machine.
    
# Compiled vs Interpreted language:
    # Compiled language:
        # A compiled language needs to be compiled by a compiler (a software) before the code can be read and understood by the machine. Compiled languages run faster than interpreted languages, but the compiling process may take some time.
        # Some compiled languages are:
            # C
            # C++
            # Go
            # Rust
    # Interpreted language:
        # Programs in interpreted language generally rely on an intermediary program called an interpreter.
        # These programs use interpreters to execute the instructions specified in the code, rather than running them through a compiler first.
        # This makes the development cycle for a program written in an interpreted language much faster, because its developer doesn't need to wait for the code to be compiled to execute it.
        # Also the same code can be read by interpreters running on different operation systems without needing to make any additional changes.
        # The downside of interpreted languages is that it generally run slower than compiled ones.
        # Some interpreted languages are:
            # Python
            # Ruby
            # JavaScript
            # Bash
            # PowerShell
    # Mixed approach, using both a compiler and an interpreter:
        # Java and C# code needs to be compiled first, but it gets compiled into intermediate code. This means that instead of getting compiled into machine language that's specific for the current operating system, it gets compiled in supportable code that can execute on different platforms.
        # We execute this code using a program that's OS specific:
            # Java: Java virtual machine
            # C#: Common language runtime
            
# shebang:
    # #!/usr/bin/env python
    # This line will be written as the first line of a python script to tell the OS what command we want to use to execute the script.

# Creating your own modules and submodules:
    # __init__.py file: You can create submodules by creating these submodules in a folder. This folder needs to have an __init__.py file in it so the interpreter recognize the folder as a module. 
    
# Scalability:
    # When more work is added to a system, the system can do whatever it needs to complete the work.
    
# Bit-rot:
    # The process of software falling out of step with the environment.
    
# Virtual Machine (VM):
    # A computer simulated through software. Simulated hardware.
    
# Parsing:
    # Analyzing a file's content to correctly structure the data.
    # Using rules to understand a file or datastream as structured data.

def csv_examples():
    # CSV (Comma Separated Values):
        # A common data format used to store data as segment of text separated by commas.
        # A lot of programs are capable of exporting data as CSV files, such as spreadsheet applications like Microsoft Excel or Google Sheets.
        # Think of a CSV file like it's a spreadsheet where each line corresponds to a row and each comma separated field corresponds to a column.
        # Each line in a CSV file generally represents a single data record. Each field in that record is separatted by a comma, with the contents of the field stored between the commas.
        # Example of how a CSV might look like:
            # Sabrina Green,802-867-5309,System Administrator
            # Eli Jones,684-3481127,IT specialist
            # Melody Daniels,846-687-7436,Programmer
            # Charlie Rivera,698-745-3357,Web Developer

    import csv
    
    def csv_list_writer():
        hosts = [['workstation.local', '192.168.25.46'], ['webserver.cloud', '10.2.5.6']]
        with open('hosts.csv', 'w', newline='') as hosts_csv:
            writer = csv.writer(hosts_csv)
            writer.writerows(hosts)
    # csv_list_writer()
    
    def csv_reader():
        with open('csv_file.txt') as file:
            csv_f = csv.reader(file)
            for row in csv_f:
                name, phone, role = row
                print(f'Name: {name}, Phone: {phone}, Role: {role}')
                    # Name: Sabrina Green, Phone: 802-867-5309, Role: System Administrator
                    # Name: Eli Jones, Phone: 684-3481127, Role: IT specialist
                    # Name: Melody Daniels, Phone: 846-687-7436, Role: Programmer
                    # Name: Charlie Rivera, Phone: 698-745-3357, Role: Web Developer
    # csv_reader()
    
    def csv_dictwriter():
        users = [
            {'name': 'Sol Mansi', 'username': 'solm', 'department': 'IT infrastructure'},
            {'name': 'Lio Nelson', 'username': 'lion', 'department': 'User Experience Research'},
            {'name': 'Charlie Grey', 'username': 'greyc', 'department': 'Development'}
        ]
        keys = ['name', 'username', 'department']
        with open('by_department.csv', 'w', newline='') as by_department:
            writer = csv.DictWriter(by_department, fieldnames=keys) # fieldnames is required
            writer.writeheader() # This will create the first line of the CSV based on keys that we passed
            writer.writerows(users) # This will turn the list of dicts into lines in that file.
    csv_dictwriter()
    
    def csv_dictreader():
        with open('by_department.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(('Name: {}, Username: {}'.format(row['name'], row['username'])))
    csv_dictreader()
# csv_examples()
      
def file_object():
    # File descriptor and file objects:
    # A token, generated by the OS, that allows programs to do more operations with the file.
    # In Python, this file descriptor is stored as an attribute of the files object.
    # Example:
    file = open('spider.txt')
    print(file.readline()) # This reads the current line.
        # Itsy bitsy spider climed up the water spout
    print(file.readline())
        # Down came the rain and washed the spider out
    print(file.read()) # This reads the current line until the last line.
        # Out came the sun and dried up all the rain
        # And the itsy bitsy spider climed up the spout again
        # The itsy bitsy spider climed down to my head
        # Along cane the wind and blew him to a shed
        # The pigssaid oh no you don't belong in here
        # And the itsy bitsy spider cried alittle tear
        # The itsy bitsy spider went searching for a home
        # He was very sad and felt all alone
        # Along came the wind and blew him near the hens
        # And the itsy bitsy spider made some new friends
    file.close()
    
    # The 'with' keyword automatically closes a file after you've opened it.
    with open('spider.txt') as file:
        print(file.readline())
        print(file.readline())
        print(file.read())
        
    # The downside of the 'with' keyword is that you can't work with the file in other places in our code,
    # since the file immediately closes after we're done with it.
# file_object()

def loop_through_file():
    # Looping through a file:
    def print_all_lines():
        with open('spider.txt') as file:
            for line in file:
                # The empty line character '\n' is read by readline(), hence the space.
                print(line.upper())
                    # ITSY BITSY SPIDER CLIMED UP THE WATER SPOUT

                    # DOWN CAME THE RAIN AND WASHED THE SPIDER OUT       

                    # OUT CAME THE SUN AND DRIED UP ALL THE RAIN

                    # AND THE ITSY BITSY SPIDER CLIMED UP THE SPOUT AGAIN

                    # THE ITSY BITSY SPIDER CLIMED DOWN TO MY HEAD

                    # ALONG CANE THE WIND AND BLEW HIM TO A SHED

                    # THE PIGSSAID OH NO YOU DON'T BELONG IN HERE

                    # AND THE ITSY BITSY SPIDER CRIED ALITTLE TEAR

                    # THE ITSY BITSY SPIDER WENT SEARCHING FOR A HOME

                    # HE WAS VERY SAD AND FELT ALL ALONE

                    # ALONG CAME THE WIND AND BLEW HIM NEAR THE HENS

                    # AND THE ITSY BITSY SPIDER MADE SOME NEW FRIENDS
    print_all_lines()
         
    def print_stripped_lines():
        with open('spider.txt') as file:
            for line in file:
                # strip() removes all the white spaces around a string.
                print(line.strip().upper())
                    # AND THE ITSY BITSY SPIDER MADE SOME NEW FRIENDS
                    # ITSY BITSY SPIDER CLIMED UP THE WATER SPOUT
                    # DOWN CAME THE RAIN AND WASHED THE SPIDER OUT
                    # OUT CAME THE SUN AND DRIED UP ALL THE RAIN
                    # AND THE ITSY BITSY SPIDER CLIMED UP THE SPOUT AGAIN
                    # THE ITSY BITSY SPIDER CLIMED DOWN TO MY HEAD
                    # ALONG CANE THE WIND AND BLEW HIM TO A SHED
                    # THE PIGSSAID OH NO YOU DON'T BELONG IN HERE
                    # AND THE ITSY BITSY SPIDER CRIED ALITTLE TEAR
                    # THE ITSY BITSY SPIDER WENT SEARCHING FOR A HOME
                    # HE WAS VERY SAD AND FELT ALL ALONE
                    # ALONG CAME THE WIND AND BLEW HIM NEAR THE HENS
                    # AND THE ITSY BITSY SPIDER MADE SOME NEW FRIENDS
    print_stripped_lines()
    
    def read_line_as_list():
        file = open('spider.txt')
        print('type(file):', type(file))
            # type(file): <class '_io.TextIOWrapper'>
            # readlines() is a method that returns a list with all the lines as items.
        lines = file.readlines()
        file.close()
        print(lines)
            # ['Itsy bitsy spider climed up the water spout\n', 'Down came the rain and washed the spider out\n', 'Out came the sun and dried up all the rain\n', 'And the itsy bitsy spider climed up the spout again\n', 'The itsy bitsy spider climed down to my head\n', 'Along cane the wind and blew him to a shed\n', "The pigssaid oh no you don't belong in here\n", 'And the itsy bitsy spider cried alittle tear\n', 'The itsy bitsy spider went searching for a home\n', 'He was very sad and felt all alone\n', 'Along came the wind and blew him near the hens\n', 'And the itsy bitsy spider made some new friends']
        lines.sort()
        print(lines)
            # ['Along came the wind and blew him near the hens\n', 'Along cane the wind and blew him to a shed\n', 'And the itsy bitsy spider climed up the spout again\n', 'And the itsy bitsy spider cried alittle tear\n', 'And the itsy bitsy spider made some new friends', 'Down came the rain and washed the spider out\n', 'He was very sad and felt all alone\n', 'Itsy bitsy spider climed up the water spout\n', 'Out came the sun and dried up all the rain\n', 'The itsy bitsy spider climed down to my head\n', 'The itsy bitsy spider went searching for a home\n', "The pigssaid oh no you don't belong in here\n"]
    read_line_as_list()
    
    # Important note regarding assigning return values of read functions to variables. Only do this for smaller files. For bigger files, do this line by line.
# loop_through_file()

def file_write():
    # Writing a file:
    # https://docs.python.org/3/library/functions.html#open
    # File objects can be opened in several different modes. A mode is similar to a file permission.
    # It governs what you can do with the file you've just opened.
    # By default, the open function uses the 'r' mode, which stands for read only.
    # 'w' mode gives permission to overwrite. Write mode will delete the old content the moment the file opens.
    # It's important to remember that when opening a file in write only mode, you can't read its contents.
    # 'a' mode gives permssion to append. Doesn't overwrite the file that already exists, instead appends the new text to the old content.
    # 'r+' mode is read-write mode.
    # 'w+' mode is read-write mode.
    with open('novel.txt', 'w') as file:
        file.write('It was a dark and stormy night')
# file_write()

def os_methods():
    # os module methods:
    # https://docs.python.org/3/library/os.html
    # https://docs.python.org/3/library/os.path.html
    import os
    import datetime
    def create_rename_remove_file():
        if not os.path.exists('novel.txt'):
            with open('novel.txt', 'w') as file:
                print("\nnovel.txt created")
        
        if os.path.exists('novel.txt') and not os.path.exists('renamed_novel.txt'):
            os.rename('novel.txt', 'renamed_novel.txt')
            print("novel.txt renamed to renamed_novel.txt")
        
        if os.path.exists('novel.txt'):
            os.remove('novel.txt')
            print("novel.txt is removed")
        else: print("novel.txt doesn't exist")
            
        if os.path.exists('renamed_novel.txt'):
            os.remove('renamed_novel.txt')
            print("renamed_novel.txt is removed")
        else:  print("renamed_novel.txt is removed")
    # create_rename_remove_file()
        
    def get_filesize():
        with open('file_with_content.txt', 'w') as file:
            text = 'Lorem ipsummm'
            file.write(text)
                
        if os.path.exists('file_with_content.txt'):
            print('\nfilesize:', os.path.getsize('file_with_content.txt'))
                # filesize: 11
    get_filesize()
    
    def get_unix_timestamp():
        if not os.path.exists('test_file.txt'):
            with open('test_file.txt', 'w'):
                pass
        
        if os.path.exists('test_file.txt'):
            timestamp = os.path.getmtime('test_file.txt')
            print('\ntimestamp:', timestamp)
            print('get_datetime:', datetime.datetime.fromtimestamp(timestamp))
    # get_unix_timestamp()
    
    # Get absolute path of a file:
    print('\nAbsolute path:', os.path.abspath('python_notes.py'))
        # Absolute path: C:\Users\ha_ph\Documents\python_notes\python_notes.py
    
    # getcwd, get current working directory:
    print('\nCurrent working directory:', os.getcwd())
        # Current working directory: C:\Users\ha_ph\Documents\python_notes
    
    # Create, change and remove directories:
    def create_change_remove_directories():
        print('\ncreate_change_remove_directories:')
        # mkdir, make directory:
        if not os.path.isdir('new_dir'):
            os.mkdir('new_dir')
            print('Directory created')
            os.chdir('new_dir')
            print('Changed directory')
            print('Current working directory:', os.getcwd())
        else:
            try:
                os.rmdir('new_dir')
                print('Directory removed')
            except Exception as e: print('\nError:\n', e)
    # create_change_remove_directories()
    
    # list of files in a directory:
    def listing_files_in_dir():
        path = 'c:/Users/ha_ph/Documents/python_notes/'
        list = os.listdir(path)
        for name in list:
            fullname = os.path.join(path, name)
            if os.path.isdir(fullname):
                print(f"{fullname} is a directory")
            else:
                print(f"{fullname} is a file")
    # listing_files_in_dir()
# os_methods()
