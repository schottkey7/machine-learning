'''
Recall Bayes Rule:

P(A|B) = P(B|A)*P(A)/P(B)

Or in our case

P(a certain word|surrounding words) = P(surrounding words|a certain word) *
P(a certain word) / P(surrounding words)
'''
text = "So if you could just go ahead and pack up your stuff and move it \
down there, that would be terrific OK"

# Question 1: Finding the word "you" after the word "if"
# P(you | if) = P(if | you) * P(you) / P(if)
p = (1.0 * 1/22.) / (1/22.)
