import unittest


def lookup_word(my_dict, search):
  if search in my_dict:
    return my_dict[search]
  else:
    return('N/A')

def add_word_to_dict(my_dict, add, addinfo):
  if add in my_dict:
    my_dict[add + '(2)'] = addinfo
    return my_dict
  else:
    my_dict[add] = addinfo
    return my_dict

def delete_in_dict(my_dict, remove):
  if remove in my_dict:
    del my_dict[remove]
    return my_dict
  else:
    return my_dict

def main():

# initial dictionnary
  my_dict = {
    "Variable":
    "a quantity or function that may assume any given value or set of values.",
    "Array":
    "an arrangement of a series of terms according to value, as from largest to smallest.",
    "Function":
    "a set of ordered pairs in which none of the first elements of the pairs appears twice."
  }
# your code here 
  print("\n\t*** dictionary ***\n")
  print("Welcome to My Dictionary! What can I do for you?\n")
  print("1. Search for a word\n2. Add a new word\n3. Remove a word\n")

  dict_choice = int(input("Please type your choice number: "))

  if dict_choice == 1:
    search = input("Enter the word you want to look up: ")
    searchresult = lookup_word(my_dict, search)
    print(search, ':', searchresult)
    print("\nThanks for using MyDictionary.")

  if dict_choice == 2:
    add = input("Enter the word you want to add: ")
    addinfo = input("Please add a definition for your word: ")
    addresult = add_word_to_dict(my_dict, add, addinfo)
    print(addresult)
      
  if dict_choice == 3:
    remove = input("Enter the word you want to remove ")
    removeresult = delete_in_dict(my_dict, remove)
    print(removeresult)


# Testing code
class TestDictFunctions(unittest.TestCase):

  def test_search_word_success(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = test_dict["Variable"]
    expected = lookup_word(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_search_word_no_result(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = "N/A"
    expected = lookup_word(test_dict, "Array")
    self.assertEqual(actual, expected)

  def test_add_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Array":
      "an arrangement of a series of terms according to value, as from largest to smallest.",
    }
    expected = add_word_to_dict(
      test_dict, "Array",
      "an arrangement of a series of terms according to value, as from largest to smallest."
    )

    self.assertEqual(actual, expected)

  def test_add_word_duplicate(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Variable(2)": "temporary value assignment"
    }
    expected = add_word_to_dict(test_dict, "Variable",
                                "temporary value assignment")
    self.assertEqual(actual, expected)

  def test_delete_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    expected = {}
    actual = delete_in_dict(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self)
    test_dict = {
      "Variable"
      "a quantity or function that may assume any given value or set of values."
    }
    expected = test_dict
    actual = delete_in_dict(test_dict, "Array")
    self.assertEqual(actual, expected)


#uncomment to run tests
unittest.main()

main()
