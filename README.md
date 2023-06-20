# mcdonalds-food-for-thought

McDonalds Food for Thought is a Python program that automates the process of filling out a McDonald's Food for Thoughts survey using Selenium WebDriver. The program takes in two inputs: the entry code found on the receipt and the amount spent during the transaction. The program then fills out the survey using the provided information.

## Getting Started
These instructions will help you set up and run the program on your local machine.

## Prerequisites
1. Python 3.x installed on your system.
2. Firefox web browser installed on your system.

## Installation
1. Clone the repository to your local machine.
```
git clone https://github.com/yourusername/receipt-reader.git
```
2. Change the directory to the cloned repository.
```
cd receipt-reader
```
3. Install the required Python packages.
```
pip install -r requirements.txt
```
4. Update config.py with your email address and the path to the geckodriver executable.
```python
geckodriver_path = "/path/to/geckodriver"

# Change this to your email address
email = "your@email.com"
```

## Usage
1. Run the main.py script.
```
python main.py
```
2. Enter the entry code and amount spent in the GUI that appears.
3. The program will fill out the survey using the provided information and print the time taken in seconds.

## Contributing
Please submit any bug reports, feature requests, or improvements as issues on the GitHub repository. You can also submit pull requests for any changes you'd like to see incorporated into the project.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.