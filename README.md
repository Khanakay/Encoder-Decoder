# Encoder-Decoder

## Project Description

I have developed a software in Python that takes a password as input and converts it into a paragraph. This paragraph consists of random sentences related to daily life and Linux tasks, making it appear as a normal paragraph. The idea is to mask the encoded password within a seemingly ordinary paragraph, so that anyone viewing it will think it's just a regular paragraph and not something encoded.

To decode the paragraph back into the original password, it must be entered into the decode input box. This approach ensures that the encoded content does not appear suspicious, unlike typical encoding methods such as MD5 hashes, which are immediately recognizable as encoded data and prompt attempts to crack them.

Further improvements are planned for the future, such as converting the paragraph into different formats or words, etc.


## Screenshot
![Encoder Decoder](https://raw.githubusercontent.com/Khanakay/Encoder-Decoder/main/encoder_decoder_lime_black.jpg)


## Requirements

- Python 3.x
- Tkinter library (for the GUI version)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Khanakay/Encoder-Decoder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Encoder-Decoder
   ```
3. Install the required libraries:
   ```bash
   pip install tk
   ```

## Usage

1. Run the main script to start the application:
   ```bash
   python main.py
   ```
2. Enter your password in the input box and click the "Encode" button to convert it into a paragraph.
3. To decode, enter the encoded paragraph into the decode input box and click the "Decode" button.

## Future Improvements

- Adding options to convert the paragraph into different formats or words.
- Enhancing the randomness and variety of sentences used in the paragraphs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Site
You can Access this project directly on this website
https://charger8ub.pythonanywhere.com/

## License

This project is licensed under the MIT License.

---
