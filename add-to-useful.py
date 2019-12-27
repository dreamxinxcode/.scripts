# I keep a file in my Documents where I store useful snippets.
# This script is to quickly add a snippet to that file.

import os

def main():
    description = input("Description: ")
    snippet = input("Snippet: ")
    home = os.environ["HOME"]
    with open(home + "/Documents/useful/useful", "a") as f:
        f.write("\n# " + description + "\n" + snippet)
        f.close
if (__name__ == "__main__"):
    main()
