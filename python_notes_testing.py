# Summary
    # Software testing:
        # The process of evaluating computer code to determine whether or not it does what you expect it to do.
    # Types of testing:
        # Automated testing
            # Example. Using a script that will run a function multiple times with differemnt arguments and see if there are any errors.
        # Unit tests
            # Used to verify that small, isolated parts of a program are correct. There is a Python module called 'unittest'. Use this module to test the units in your scripts.
        # Integration tests
        # Test-driven development:
            # Need to create a separate test environment.
    # Test cases:
        # Every different value passed through a function or code block we're testing is called a test case.
    # Edge cases:
        # Inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with.
    # White-box testing (clear-box or transparent testing):
        # Relies on the test creator's knowledge of the software being tested to construct the test cases.
    # Black-box testing:
        # Written with an awareness of what the program is supposed to do - its requirements or specifications - but not how it does it.
    # Test-driven development (TDD):
        # Creating the test before writing the code.
    # raise (Python keyword):
        # Check for faulty conditions that we expect to happen during normal execution of our code.
        # To raise a custom error. Example:
            # if minlen < 1:
                # raise ValueError('minlen must be at least 1')
    # assert (Python keyword):
        # Verify situations that aren't expected but that might cause our code to misbehave.
        # Tries to verify that a conditional expression is true, and if it's false, it raises an assertion error with the indicated message. Assertions will be ignored when the software is run with the -O (optimized) flag.
        # Example:
            # assert type(username) == str, "username must be a string"

def test_example():
    # https://docs.python.org/3/library/unittest.html
    import re
    import unittest

    def rearrange_name(name):
        result = re.search(r"^([\w .]*), ([\w .]*)$", name)
        if result is None:
            return ""
        return "{} {}".format(result[2], result[1])
    
    
    class TestRearrange(unittest.TestCase):
        def test_basic(self):
            testcase = "Lovelace, Ada"
            expected = "Ada Lovelace"
            self.assertEqual(rearrange_name(testcase), expected)
            
        def test_empty(self):
            testcase = ""
            expected = ""
            self.assertEqual(rearrange_name(testcase), expected)
            
    unittest.main()
test_example()