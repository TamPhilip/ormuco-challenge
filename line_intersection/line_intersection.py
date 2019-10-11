
# QA: Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

# Implementing a singleton (for fun tbh)
# Personal Goal: Create a robust line intersection program
class Overlap:

    __instance = None

    @staticmethod
    def get_instance():
        if Overlap.__instance == None:
            Overlap()
        return Overlap.__instance

    def __init__(self):
        if Overlap.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Overlap.__instance = self

    # Assuming that a line has to be a tuple
    # Assume that an intersection of lines means that both lines are on top of each other
    # If two lines have a same point then they overlap too
    @staticmethod
    def lines(l1, l2):
        """
        Returns a boolean depending on if both the lines have an intersection

        :param l1: tuple
            Line 1
        :param l2: tuple
            Line 2
        :return: boolean
            returns both the lines have an intersection

        Raises
        -----

        NotImplementedError
            If l1 or l2 is None, not a tuple, or incorrect length (not equal to 2)

        """

        # Checks if lines are in correct format
        if not Overlap.__is_line(l1) or not Overlap.__is_line(l2):
            raise NotImplementedError("Incorrect line format")

        # Sorts the values of a line to simplify where x_1 < x_2 and x_3 < x_4
        x_1, x_2 = Overlap.__set__line(l1)
        x_3, x_4 = Overlap.__set__line(l2)

        # if x_3 is before x_1
        # check if x_4 comes after or is on top of x_1
        if x_4 >= x_1 > x_3:
            return True

        # if x_1 is before x_3
        # check if x_2 comes after or is on top of x_3
        if x_2 >= x_3 > x_1:
            return True

        # If x_1 start at the same point as x_3 then overlap
        if x_1 == x_3:
            return True

        return False

    @staticmethod
    def __set__line(l):
        """
        Sorts the values of the line to be ascending

        :param l: tuple
            Line
        :return: tuple

        """
        x_1, x_2 = l
        if x_1 > x_2:
            return x_2, x_1
        return x_1, x_2

    @staticmethod
    def __is_line(l):
        """
        Determines if the line is a tuple of length 2

        :param l: tuple
            Line
        :return: boolean
            returns a boolean depending on if the line is in a correct format

        """
        if l is not None and type(l) is tuple and len(l) == 2:
            return True
        return False

print(Overlap.lines(l1=(1,3), l2=(3,6)))
