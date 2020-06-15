# helper functions
def convert_str_to_int(text = ""):
    """convert string to number, when the int() function does not work
    Some numbers in the website are like 3,589 which will not be converted
    to 3589 when using int() to the string. This function will help to do
    that.

    Args:
        text (str): a string of number

    Returns:
        number (int)

    Example:
        >>> convert_str_to_int(58)
        58
        >>> convert_str_to_int(3,597)
        3597
        >>> convert_str_to_int(1,000,000)
        1000000
    """
    l = list(reversed(text.split(",")))
    number = 0
    if len(l) == 0:
        return 0
    for i in range(len(l)):
        number += (10**(3*i))*int(l[i]) # the numbers were splitted to 3 digits
    return number


def merge_years_for_two_list(l1, l2):
    """a private method to merge two list of list where the last element of first list is equal to
    first element of the second list

    Args:
        l1 (list): first list
        l2 (list): second list

    Returns:
        l (list): merged list of l1 and l2

    Example:
            >>> merge_years_for_two_list(['2013', '2014', '2015'],['2015', '2016', '2019'])
            ['2013', '2014', '2015', '2016', '2019']
    """
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1

    if l1[-1] == l2[0]:
        l = l1 + l2[1:]
    else:
        l = l1 + [''] +  l2
    return l

def merge_years_for_lists_of_list(list_of_lists):
    """merge list of lists when last element of each list matches with the
    fist element of the next list

    Args:
        list_of_lists (list): a list of lists which will be merged

    Returns:
        l (list): a merged list of elements in lists of the list

    Example:
        >>> merge_years_for_lists_of_list([["2010", "2012"], ["2012", "2014"], ["2014", "2020"]])
        ["2010", "2012", "2014", "2020"]
    """
    if len(list_of_lists) < 2:
        return list_of_lists[0]
    l = []
    for i in range(len(list_of_lists)):
        l = merge_years_for_two_list(l, list_of_lists[i])
    return l

def separate_affiliations_from_pos(text):
    """A function to find affiliation position from a special type of string

    Args:
        text (str): a text which has forms of POSTION,AFFILIATION or AFFILIATION

    Returns:
        pos (str)
    """
    pos = text.split(",")[0].upper()
    if pos in AFFILIATIONS_POSITIONS:
        return pos
    else:
        return ''
