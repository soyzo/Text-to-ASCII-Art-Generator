# Install the pyfiglet library
!pip install pyfiglet

import pyfiglet

def text_to_ascii(text, font='slant'):
    """Converts input text to ASCII art using the specified font."""
    try:
        # Create ASCII art text
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except Exception as e:
        return f"Error generating ASCII art: {e}"

def show_font_examples():
    """Displays a one-letter example for each available font."""
    available_fonts = pyfiglet.FigletFont.getFonts()
    example_char = 'A'  # Character to display as an example

    print("\nFont Examples:")
    for font in available_fonts:
        try:
            # Generate and print ASCII art for the example character
            ascii_art = pyfiglet.figlet_format(example_char, font=font)
            print(f"Font: {font}")
            print(ascii_art)
            print("-" * 40)  # Separator for readability
        except Exception as e:
            print(f"Error with font {font}: {e}")

def main():
    # Input text from user
    user_text = input("Enter the text to convert to ASCII art: ")

    # Show font examples
    show_font_examples()

    # Input font from user
    font_choice = input("Enter the font you want to use (default 'slant'): ") or 'slant'
    
    # Generate and display ASCII art
    ascii_art = text_to_ascii(user_text, font=font_choice)
    print("Generated ASCII Art:")
    print(ascii_art)

# Run the main function
if __name__ == "__main__":
    main()
