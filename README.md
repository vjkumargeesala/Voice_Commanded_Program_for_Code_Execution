# 🎤 Voice Commanded Program for Basic Code Execution 🤖

This project, created in 🗓️ 2020, is a Python 🐍-based application that uses speech 🗣️ recognition technology to execute a variety of basic programming tasks. These tasks include checking for prime numbers 🔢, identifying even ➗ and odd numbers, determining Armstrong numbers 💡, and much more, all powered by voice commands 🎙️. It serves as an excellent example of integrating natural language 🧠 processing with computational logic to create an interactive 📱 and user-friendly program.

## ✨ Features

- **Speech Recognition 🗣️**: Captures user input 🎧 via a microphone 🎤 and uses Google's Speech Recognition API 🌐 to convert spoken words 🔊 into text, ensuring seamless interaction.
- **Command Execution 🛠️**: Performs a wide range of programming tasks 🧮, categorized as follows:
  - **Mathematical Checks 🧑‍🏫**:
    - Verify if a number is prime 🔢 (`isprime`).
    - Determine if a number is even ➗ (`is_even`) or odd ➕ (`is_odd`).
    - Check if a number is an Armstrong number 💡 (`is_armstrong`).
    - Assess whether a number is a palindrome 🔁 (`is_palin`).
  - **Factorial and Factors 🔢**:
    - Compute the factorial of a given number (`get_factorial`).
    - Retrieve all factors of a specified number (`get_factors`).
  - **Sequence Generation 🔄**:
    - Generate a Fibonacci sequence ♾️ (`get_fibonacci`).
  - **Year Validation 📆**:
    - Validate whether the input corresponds to a legitimate year (`is_year`).
  - **Alphabet and Number Processing 🔠🔢**:
    - Extract or manipulate alphabetic characters (`get_alphabet`).
    - Handle numeric data for specific operations (`get_num`).
  - **Geometric Outputs 📐**:
    - Create visual representations such as a triangle 🔺 (`get_triangle`), a right-aligned triangle 🔻 (`get_right`), and a left-aligned triangle 🔺 (`get_left`).
  - **Miscellaneous 🌟**:
    - Detect Armstrong numbers 💡 within a range (`get_armstrong`).
    - Identify palindrome strings or numbers 🔁 (`get_palin`).

## 🛠️ Technologies Used

- **Python 3.x 🐍**: The core programming language.
- **[SpeechRecognition Library 🌐](https://pypi.org/project/SpeechRecognition/)**: Facilitates speech-to-text conversion.

## ⚙️ Setup and Installation

1. **Clone the Repository 📂**:
   Begin by cloning the repository to your local machine 💻:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Libraries 📦**:
   Use pip to install dependencies:
   ```bash
   pip install SpeechRecognition
   ```

3. **Set Up Microphone Access 🎤**:
   Ensure your system’s microphone is functional 🎧 and accessible to the application.

4. **Run the Program ▶️**:
   Execute the script to start interacting:
   ```bash
   python Voice_Commands.py
   ```

## 📝 Usage Instructions

1. Launch the program 🚀 as outlined in the setup instructions.
2. Clearly speak 🎙️ a command when prompted. Examples:
   - "Check if 7 is prime 🔢."
   - "Is 12 an even number ➗?"
   - "Tell me if 153 is an Armstrong number 💡."
   - "Generate the Fibonacci sequence ♾️ up to 10."
3. The program processes your spoken input 🎧 and returns results 📊 in the console.

## 💡 Example Output

```
Say what you want regarding Basic Programs 🎤
Processing your input...
"Check if 7 is prime."
Result: 7 is a prime number 🔢.
```

## ⚠️ Limitations

While functional ✅, the program has a few constraints:

- **Internet Dependency 🌐**: A stable connection is required for the Google Speech Recognition API.
- **Pronunciation Accuracy 🎙️**: Clear pronunciation is necessary for accurate results.
- **Complex Commands 🌀**: Overly complex or ambiguous instructions may not be processed effectively.

## 🚀 Future Enhancements

To make this project more versatile 🛠️:

- **Advanced Tasks 🤓**: Expanding support for sophisticated operations.
- **GUI Development 🖥️**: Replacing console-based interaction with a graphical user interface.
- **Enhanced NLP 🧠**: Improving natural language understanding for diverse commands.
- **Offline Mode 🔌**: Incorporating offline speech recognition capabilities.

## 🤝 Contribution

Contributions are welcome 🙌! Fork the repository 🍴, implement changes 🔄, and submit a pull request 📬 to improve this project.

## 📜 License

This project is distributed under the MIT License 📄. Refer to the LICENSE file for details.

