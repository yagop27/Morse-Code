<h1>Morse Code Converter</h1>

A simple Python script that translates a string of text into Morse code. The script follows the standard Morse code alphabet, and currently, special characters like @, #, etc., are not supported.

<h2>Prerequisites:</h2>

  - Python 3.6 or higher installed on your system.

<h2>Running the application:</h2>

  1- Clone this repository or download the project files.

  2- Run the Python script to start the application.

      python Morse-Code.py
      
  3- Using the script:
  
   - Input the string you want to convert from text to Morse code (without special characters).
   - Press Enter, and the script will output the equivalent Morse code.

<h3>Example</h3>

    Type in the text you want to convert into morse code: hello world
    
Output:

    **** * *-** *-** --- / *-- --- *-* *-** -**

<h2>Code Structure:</h2>

  - `morse_alphabet` dictionary: Stores the mapping from text to Morse code.
  - `morse_converter` function:
    - Converts a string to Morse code using list comprehension.
    - Handles characters not in the dictionary via error handling (KeyError).
    - Returns the final Morse code string.
  - User Input: The script prompts the user for input and displays the Morse code output.

<h2>License</h2>

  This project is open-source and available under the MIT License.

<h2>Contact</h2>

  If you have any questions, feel free to reach out to me at yagopais@id.uff.br.
