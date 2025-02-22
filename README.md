README file for your Steganography Tool project:


# Steganography Tool

A simple Python-based Steganography Tool that uses **Tkinter** for the graphical user interface (GUI) and **Pillow** (PIL) for image processing.
The tool allows users to hide and reveal messages within image files using **Least Significant Bit (LSB)** encoding technique.

## Features

- **Hide & Save**: Embed a message into an image and save it as a new image.
- **Show Data**: Extract and display a hidden message from an image.
- **Reset**: Reset the application to its initial state.

## Requirements

### System Requirements:
- **Operating System**: Works on Windows, macOS, and Linux.
- **Python Version**: Python 3.6 or higher.

### Software & Libraries:
You need the following libraries installed to run this project:

- **Tkinter**: The standard Python library for GUI development.
- **Pillow (PIL)**: For image handling and manipulation.
- **Stegano**: For implementing the steganography (message hiding) feature.

You can install the required libraries using the following commands:

## Installation

1. **Clone or download the project**:
   - You can either clone the repository or download the script manually.

2. **Install the required Python libraries**:
   - Open your command prompt or terminal and run:
   ```bash
   pip install Pillow stegano
   ```

3. **Prepare your images**:
   - Make sure you have a valid image file (either PNG or JPG) to hide or reveal the message.
   - You should also have an image file named `logo.jpg` (used as the logo in the GUI) in the same directory.

## Usage

1. **Running the Application**:
   - Simply run the Python script:
   python steganography_tool.py
   - This will open a window with the Steganography Tool.

2. **How to Use**:
   - **Open Image**: Click on the "Open Image" button to select an image file (PNG or JPG) from your system.
   - **Enter Secret Key**: Enter a secret key (default is `0000`).
   - **Hide & Save**: To hide a message, enter the text you want to hide in the text box, and click the "Hide & Save" button. The new image with the hidden message will be saved as `Secret_image.png`.
   - **Show Data**: To reveal the hidden message from an image, select an image and click the "Show Data" button. The extracted message will appear in the text box.
   - **Reset**: To reset the application, click the "Reset" button, which will clear all fields and selections.

## File Structure
/Steganography-Tool
    ├── steganography_tool.py  # Python script containing the code
    
    ├── logo.jpg               # Logo image used in the app (optional, can be replaced)
    
    ├── README.md              # This README file

## Acknowledgements

- **Tkinter**: Python's standard GUI library.
- **Pillow (PIL)**: Python Imaging Library (PIL) fork for handling images.
- **Stegano**: Python library for steganography (encoding and decoding hidden messages).
  
