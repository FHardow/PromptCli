EXPERIMENTAL_SYSTEM_DEVELOPER_PROMPT = """
                        Sure, I can describe the process and provide an example.

The process usually involves the following steps:

Understand the Instructions: The first step is to thoroughly understand the instructions. This might involve asking 
clarifying questions to ensure that you fully understand what is being asked.

Analyze the Code: Next, you need to analyze the existing code snippet to understand what it does and how it works.
This might involve running the code to see its output, reading through the code line by line, and possibly doing some 
research to understand any unfamiliar concepts or functions.

Plan the Changes: Once you understand the instructions and the existing code, you can plan out the changes you need to 
make. This might involve writing pseudocode, drawing diagrams, or just thinking through the logic in your head.

Implement the Changes: After you have a plan, you can start to implement the changes in the code. This might involve 
adding new lines of code, modifying existing lines, or deleting lines that are no longer needed.

Test the Changes: Finally, you need to test the changes to make sure they work as expected. This might involve running 
the code with different inputs and checking the output, using a debugger to step through the code, or writing automated 
tests.

Here's an example:

Let's say the original Python code snippet is:

python
Copy code
def greet(name):
    print("Hello, " + name)

greet("Alice")
And the instruction is: "Modify the function to include a greeting based on the time of day. If it's morning, the 
function should say 'Good morning'. If it's afternoon, it should say 'Good afternoon'. Otherwise, it should just say 
'Hello'."

Here's how I would modify the code to implement these instructions:

python
Copy code
import datetime

def greet(name):
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Hello"
    print(f"{greeting}, {name}")

greet("Alice")
In this modified code, I first import the datetime module to get the current hour. Then, I modify the greet function to 
check the current hour and set the greeting accordingly. Finally, I use an f-string to print the greeting and the name.


Return the solution inside of a JSON object with the key "code" and the value being the code snippet.
Here is an example of the generated code above:
{
      "code": "import datetime

def greet(name):
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Hello"
    print(f"{greeting}, {name}")
"
}
"""


SYSTEM_PROMPT_DEVELOPER_PROMPT = """
    I will provide some specific instruction to a code snippet and you will change the code so
     that the instructions are meet.
    My instructions are placed in quotes and follow the string `instructions:` and the code is
     placed in quotes and follow the string `code:`. 
#    You are a system that only generates code. Do not describe or contextualize the code. Do not 
#    apply any formatting or syntax highlighting. Do not wrap the code in a code block.
    From now, your response must be in the format of {"code": code block}, no talking, no comments.
#    Do not describe or contextualize the code.Do not apply any formatting or synta
#    highlighting.Do not wrap the code in a code block.
#    Only return code! Do not say anything else, only return the changed code. 
    """
