# Random Programming Problems
Grabs a random programming problem from one of 6 websites and opens it on your default browser

## Requirements
- **Python 3.6**
- **bs4**
- **requests**
- **argparse**
- **webbrowser**
- **tdqm**

## Getting started
### Prerequisites
To install the needed libraries, enter
```
pip install bs4
pip install argparse
pip install webbrowser
pip install requests
pip install tqdm
```
in your command line. This script requests python 3.6+.

### Installing
RandomProgrammingProblem can be installed by entering ```git clone https://github.com/TSharvananthan/RandomProgrammingProblem``` in your command line. If you don't have Git, feel free to clone it.

### Running the program
#### First time?
```
cd RandomProgrammingProblem
python main.py
```
#### Command Line Arguments
```
python main.py --problems [number of problems that you want]
               --update [set to True to update the list of links you can use]
```

### Examples
```
cd RandomProgrammingProblem
python main.py --problems 5 --update True
```

- Updates the list of links
- Loads 5 random problems

```
cd RandomProgrammingProblem
python main.py --problems 100000
```

- Loads 100000 problems
- Note that your browser would run slower because... who asks for 100,000 random problems
