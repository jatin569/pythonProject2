# to add a prefix text to all of the lines in a string
import textwrap
s='''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''

text_without_Indentation = textwrap.dedent(s)
wrapped = textwrap.fill(text_without_Indentation, width=10)
final_result = textwrap.indent(wrapped, '> ')

print(final_result)




