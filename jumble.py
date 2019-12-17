# jumble.py --------------------------------------------------------------

# libraries
import argparse
import re
import random


# function to perform the jumbling algorithm
def jumble(content):
    # remove punctuation and make lower case
    content = re.sub('[^\w\s]', '', content).lower()
    # split up the string based on spaces
    content_list = content.split()

    # initialize output string and use a for loop to update it
    new_content = ""
    for word in content_list:
        if len(word) > 3:
            # isolate first and last letters of the word
            first_letter = word[0]
            last_letter = word[-1]

            # extract the middle of the word and jumble it up!
            middle = word[1:-1]
            jumbled_middle = random.sample(middle, len(middle))

            # reassemble the parts of the jumbled word
            jumbled_word = first_letter + "".join(jumbled_middle) + last_letter
        else:
            # the word is too short to be jumbled
            jumbled_word = word
        # update the output
        new_content += jumbled_word + " "
    return new_content


def main():
    # parse the arguments from the command line
    parser = argparse.ArgumentParser(description='This is a program that jumbles text')
    parser.add_argument("-i", help="The name of the file with text to jumble", dest="input_file")
    parser.add_argument("-o", help="The name of the output file that containt the jumbled text", dest="output_file", default="output.txt")
    args = parser.parse_args()

    # extract args from arg parser
    input_file = args.input_file
    output_file = args.output_file

    # read in the text from a file
    with open(input_file) as f:
        text = f.read()

    # jumble the text from input_file
    output = jumble(text)

    # write the output to a new file
    with open(output_file, 'w') as f:
        f.write(output)

    # display message
    print("The text from {0} was jumbled and saved to {1}".format(input_file, output_file))
    return


if __name__ == "__main__":
    main()
