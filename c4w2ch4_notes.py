# Using threads to make things go faster:
    # https://www.coursera.org/learn/troubleshooting-debugging-techniques/lecture/JSjDh/using-threads-to-make-things-go-faster
    
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
    # 