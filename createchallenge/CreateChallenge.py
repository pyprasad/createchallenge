import random
import datetime
import argparse
from docx import Document


class FiveMinuteChallenge:
    def random_challenge_set_for_add_sub(self, operator, range_number_for_add_and_sub):
        global random_set
        random_set = []
        for x in range(100):
            random_set.append(str(random.randint(1, range_number_for_add_and_sub))+' '+operator+' '+str(random.randint(1, range_number_for_add_and_sub))+' = ')
        return random_set

    def random_challenge_for_div(self, range_number_for_div, div_flag=True):
        global division_set
        division_set = []
        while len(division_set) < 100:
            first_part = random.randint(2, range_number_for_div)
            second_part = random.randint(2, range_number_for_div)
            if div_flag:
                if first_part % second_part == 0\
                        and first_part != second_part\
                        and first_part > second_part:
                    division_set.append(str(first_part)+' ÷ '+str(second_part)+' = ')
            else:
                division_set.append(str(first_part)+' ÷ '+str(second_part)+' = ')
        return division_set

    def random_challenge_for_multi(self, first_part_of_operand, second_part_of_operand):
        global my_challenge_collection
        my_challenge_collection = []
        for first_operand in first_part_of_operand:
            for second_operand in second_part_of_operand:
                my_challenge_collection.append(str(first_operand)+' × '+str(second_operand)+' = ')
        random.shuffle(my_challenge_collection)
        return my_challenge_collection

    def put_challenge_in_table(self, challenge_set_to_table):
        global size_of_challenge
        document = Document()
        random.shuffle(challenge_set_to_table)
        size_of_challenge_set = len(challenge_set_to_table)
        shrink_challenge_set = len(challenge_set_to_table) % 4
        if size_of_challenge_set > 100:
            size_of_challenge = 100
        else:
            size_of_challenge = size_of_challenge_set-shrink_challenge_set
        table = document.add_table(rows=0, cols=4)
        for i in range(0, size_of_challenge, 4):
            row_cells = table.add_row().cells
            row_cells[0].text = challenge_set_to_table[i]
            row_cells[1].text = challenge_set_to_table[i + 1]
            row_cells[2].text = challenge_set_to_table[i + 2]
            row_cells[3].text = challenge_set_to_table[i + 3]
        file_name = datetime.datetime.now().isoformat()
        document.save(file_name+'.docx')
        print("Your 5 minute challenge: {0}", file_name+'.docx')

    def create_my_challenge_set_with_complexity(self, complexity):
        global my_challenge_set
        my_challenge_set = []
        if complexity == 0:
            my_challenge_set = self.random_challenge_set_for_add_sub('+', 50) + self.random_challenge_set_for_add_sub('-', 50) \
                               + self.random_challenge_for_multi(list(range(2, 6)), list(range(1, 10))) \
                               + self.random_challenge_for_div(10)
        elif complexity == 1:
            my_challenge_set = self.random_challenge_set_for_add_sub('+', 100) + self.random_challenge_set_for_add_sub('-', 100) \
                               + self.random_challenge_for_multi(list(range(2, 10)), list(range(1, 10))) \
                               + self.random_challenge_for_div(20)
        elif complexity == 2:
            my_challenge_set = self.random_challenge_set_for_add_sub('+', 200) + self.random_challenge_set_for_add_sub('-', 200) \
                               + self.random_challenge_for_multi(list(range(2, 15)), list(range(2, 15))) \
                               + self.random_challenge_for_div(25, False)
        else:
            my_challenge_set = self.random_challenge_set_for_add_sub('+', 500) + self.random_challenge_set_for_add_sub('-', 500) \
                               + self.random_challenge_for_multi(list(range(2, 20)), list(range(2, 20))) \
                               + self.random_challenge_for_div(50, False)
        self.put_challenge_in_table(my_challenge_set)

    def __init__(self):
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument("complexity", type=int,
                            help=('\n'
                                  '0: i) Additions up to 50\n'
                                  '   ii) Subtractions up to 50\n'
                                  '   iii) Multiplications up to table 6\n'
                                  '   iv) Divisions up to 10, \n'
                                  '1: i) Additions up to 100\n'
                                  '   ii) Subtractions up to 100\n'
                                  '   iii) Multiplications up to table 10\n'
                                  '   iv) Divisions up to 20\n'
                                  '2: i) Additions up to 200\n'
                                  '   ii) Subtractions up to 200\n'
                                  '   iii) Multiplications up to table 15\n'
                                  '   iv) Divisions up to 25,\n'
                                  'any_thing_else: \n'
                                  '   i) Additions up to 500\n'
                                  '   ii) Subtractions up to 500 \n'
                                  '   iii) Multiplications up to table 20\n'
                                  '   iv) Divisions up to 50\n'
                                  ''))
        args = parser.parse_args()
        self.create_my_challenge_set_with_complexity(args.complexity)