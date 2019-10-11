# QB: The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

# import regex
import re

# Version numbers are assumed to be in the format MAJOR.MINOR.PATCH
# Simplified strings without -hyphens currently
class VersionCheck:

    def __init__(self):
        print()

    @staticmethod
    def compare_version(v1, v2):
        """
                Returns a string indicating which version is higher or lower

                :param v1: string
                    version string 1
                :param v2: string
                    version string 2
                :return: string
                    returns a message indicating which version

                Raises
                -----

                NotImplementedError
                    If v1 or v2 is None, not a string

                """

        # Checks if lines are in correct format
        if not VersionCheck.__check_format(v1) or not VersionCheck.__check_format(v2):
            raise NotImplementedError("Incorrect version format")

        # splits the string with . into a list of strings
        v_list_1 = re.split("\.", v1)
        v_list_2 = re.split("\.", v2)

        # loop while list is not empty
        while 0 < len(v_list_1) and 0 < len(v_list_2):

            # remove the first value from lists
            substring_1 = v_list_1.pop(0)
            substring_2 = v_list_2.pop(0)

            # check for last letter
            substring_1, letter_1 = VersionCheck.__check_letter(v_list=v_list_1, substring=substring_1)
            substring_2, letter_2 = VersionCheck.__check_letter(v_list=v_list_2, substring=substring_2)

            # version number to integer
            s1 = int(substring_1)
            s2 = int(substring_2)

            # Check which version number is larger
            if s1 > s2:
                return "{} is greater than {}".format(v1, v2)
            elif s2 > s1:
                return "{} is greater than {}".format(v2, v1)

            # check for final letter if one of the v_list has no more letters
            elif letter_1 is not None or letter_2 is not None:
                return VersionCheck.__compare_letter_version(v1=v1, v2=v2, letter_1=letter_1,letter_2=letter_2)

            # if one of the lists are empty check
            if len(v_list_1) == 0 or len(v_list_2) == 0:
                return VersionCheck.__compare_last(v1=v1, v2=v2, list_length_1=len(v_list_1), list_length_2=len(v_list_2))

    @staticmethod
    def __check_letter(v_list, substring):
        """

        :param v_list:
        :param substring:
        :return:
        """
        if len(v_list) == 0:
            if re.search("[a-z]", substring):
                return substring[:-1], substring[-1:]
        return substring, None

    @staticmethod
    def __compare_last(v1, v2, list_length_1, list_length_2):
        """

        :param v1:
        :param v2:
        :param list_length_1:
        :param list_length_2:
        :return:
        """
        if list_length_1 > 0:
            return "{} is greater than {}".format(v1, v2)
        elif list_length_2 > 0:
            return "{} is greater than {}".format(v2, v1)
        else:
            return "{} is equal to {}".format(v2, v1)

    @staticmethod
    def __compare_letter_version(v1, v2, letter_1=None, letter_2 = None):
        """

        :param v1:
        :param v2:
        :param letter_1:
        :param letter_2:
        :return:
        """
        if letter_1 is not None and letter_2 is not None:
            if letter_1 > letter_2:
                return "{} is greater than {}".format(v1, v2)
            if letter_2 > letter_1:
                return "{} is greater than {}".format(v2, v1)
            if letter_1 == letter_2:
                return "{} is equal to {}".format(v2, v1)
        if letter_1 is not None:
            return "{} is greater than {}".format(v1, v2)
        if letter_2 is not None:
            return "{} is greater than {}".format(v2, v1)

    @staticmethod
    def __check_format(v):
        """

        :param v:
        :return:
        """
        if v is not None and type(v) is str:
            if re.search("^v?(\d+\.\d+(\.\d+)*[a-z]?)$", v):
                return True
        return False

print(VersionCheck.compare_version(v1="1.10.1c", v2="1.10.1"))
