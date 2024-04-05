# Built-in imports
def reverse(text):
    """
    Takes in a string and returns the reverse of the string

    Parameters
    -----------
    text: string

    Returns
    -----------
    string
    """
    if len(text) == 0:
        return ""
    else:
        return reverse(text[1:]) + text[0]


def is_palindrome(text):
    """
    Takes in a string and checks if it is a palindrome

    Parameters
    ------------
    text: string

    Returns
    ------------
    boolean
    """
    text = text.lower().replace(' ', '').replace(',', '')
    if len(text) == 0:
        return True
    else:
        if text[0] == text[-1]:
            return is_palindrome(text[1:-1])
        else:
            return False