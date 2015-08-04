# Exercise 1
#
# Improve the function ask_number() so that the function can be called with a step value. Make the default value of
# step 1.
#

def ask_number(question, low, high, step = 1):
  """
  Ask for a number within a range.
  :param question: Question to ask.
  :param low: Lowest number.
  :param high: Highest number.
  :param step: Step value
  :return: Number entered by the user.
  """
  response = None
  while response not in range(low, high, step):
    response = int(input(question))
  return response

print(ask_number("What is your number? ", 0, 10))