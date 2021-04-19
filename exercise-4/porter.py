def tokenize(text):
  return text.split()

# call this using is_consonant(word, i)
def is_consonant(word, index):
	if word[index] in ['a', 'e', 'i', 'o', 'u']:
		return False
	if word[index] == 'y':
		if index == 0:
			return True
		else:
			return not is_consonant(word, index - 1)
	return True


def is_vowel(word, index):
	return not is_consonant(word, index)


def measure(word):
	cvs = ""
	for i in range(len(word)):
		if is_consonant(word, i):
			cvs = cvs + "c"
		else:
			cvs = cvs + "v"

	return cvs.count("vc")


def contains_vowel(word):
	for index in range(len(word)):
		if not is_consonant(word, index):
			return True
	return False


def ends_in_double_consonant(word):
	if len(word) >= 2 and is_consonant(word, len(word) - 1):
		if word[-1] == word[-2]:
			return True
	return False


def ends_in_cvc(word):
	if len(word) >= 3:
		if is_consonant(word, len(word) - 3) and not is_consonant(word, len(word) - 2) and is_consonant(word, len(word) - 1) and word[-1] not in ['w', 'x', 'y']:
			return True
	return False

def replace(word, suffix, replacement):
  return word[:-len(suffix)] + replacement

def ends(word, suffix):
  return word[-len(suffix):] == suffix


def step_1a(word):

  if word[-4:] == "sses":
    # remember, Porter algorithm matches
    # the longest suffix in each step
    # and then finishes the step
    # without checking the other rules
    return word[:-4] + "ss"

  # TODO: the rest is up to you!

  elif word[-3:] == "ies":
    return word[-3:] + "i"
  elif word[-2:] == "ss":
    return word[-2] + "ss"
  elif word[-1:] == "s":
    return word[:-1]
  else:
  # no rule matches
    return word

def step_1b(word):

  if ends(word, "eed"):
    if measure(word[:-3]) > 0:
      return replace(word, "eed", "ee")
    else:
      return word

  if ends(word, "ed"):
    if contains_vowel(word[:-2]):
      stem = replace(word, "ed", "")
      return step_1b_helper(stem)
    else:
      return word

  # TODO

  if ends(word, "ing"):
    if contains_vowel(word[:-3]):
      stem = replace(word, "ing", "")
      return step_1b_helper(stem)
    else:
      return word

def step_1b_helper(word):

  # notice how we're iterating through a list of lists here
  for suffix_pair in [ [ "at", "ate" ],
                       [ "bl", "ble" ],
                       [ "iz", "ize" ] ]:
    suffix = suffix_pair[0]
    replacement = suffix_pair[1]
    if ends(word, suffix):
      return replace(word, suffix, replacement)

  if ends_in_double_consonant(word) and word[len(word) - 1] not in ["l", "s", "z"]:
    return word[:-1]

  if measure(word) == 1 and ends_in_cvc(word):
    return word + "e"

  return word

def step_1c(word):
  # TODO
  if contains_vowel(word[:-1]) and word[-1] == "y":
    return replace(word, "y", "i")
  return word

def step_2(word):
  # TODO
  for suffix_pair in [ [ "ational", "ate" ],
                       [ "tional", "tion" ],
                       [ "enci", "ence" ],
                       [ "anci", "ance" ],
                       [ "izer", "ize" ],
                       [ "abli", "able" ],
                       [ "alli", "al" ],
                       [ "entli", "ent" ],
                       [ "eli", "e" ],
                       [ "ousli", "ous" ],
                       [ "ization", "ize" ],
                       [ "ation", "ate" ],
                       [ "ator", "ate" ],
                       [ "alism", "al" ],
                       [ "iveness", "ive" ],
                       [ "fulness", "ful" ],
                       [ "ousness", "ous" ],
                       [ "aliti", "al" ],
                       [ "iviti", "ive" ],
                       [ "biliti", "ble" ] ]:
    suffix = suffix_pair[0]
    replacement = suffix_pair[1]
    if measure(word) > 0 and ends(word, suffix):
      return replace(word, suffix, replacement)
  return word

def step_3(word):
  # TODO
  for suffix_pair in [ [ "icate", "ic" ],
                       [ "ative", "" ],
                       [ "alize", "al" ],
                       [ "iciti", "ic" ],
                       [ "ical", "ic" ],
                       [ "ful", "" ],
                       [ "ness", "" ] ]:
    suffix = suffix_pair[0]
    replacement = suffix_pair[1]
    if measure(word) > 0 and ends(word, suffix):
      return replace(word, suffix, replacement)
  return word

def step_4(word):
  # TODO
  for suffix_pair in [ [ "ational", "ate" ],
                       [ "tional", "tion" ],
                       [ "enci", "ence" ],
                       [ "anci", "ance" ],
                       [ "izer", "ize" ],
                       [ "abli", "able" ],
                       [ "alli", "al" ],
                       [ "entli", "ent" ],
                       [ "eli", "e" ],
                       [ "ousli", "ous" ],
                       [ "ization", "ize" ],
                       [ "ation", "ate" ],
                       [ "ator", "ate" ],
                       [ "alism", "al" ],
                       [ "iveness", "ive" ],
                       [ "fulness", "ful" ],
                       [ "ousness", "ous" ],
                       [ "aliti", "al" ],
                       [ "iviti", "ive" ],
                       [ "biliti", "ble" ] ]:
    suffix = suffix_pair[0]
    replacement = suffix_pair[1]
    if measure(word[:(len(word) - len(suffix))]) > 1 and ends(word, suffix):
      return replace(word, suffix, replacement)
    if measure(word[:(len(word) - len(suffix))]) > 1 and word[len(word) - 4] not in ["s", "t"] and ends(word, "ion"):
      return replace(word, "ion", "")
  return word

def step_5a(word):
  # TODO
  if measure(word[:-1]) > 1 and ends(word, "e"):
      return replace(word, "e", "")
  elif measure(word[:-1]) == 1 and not ends_in_cvc(word[:-1]) and ends(word, "e"):
    return replace(word, "e", "")
  return word

def step_5b(word):
  # TODO
  if measure(word) > 1 and ends_in_double_consonant(word) and ends(word, "l"):
    return replace(word, "l", "")
  return word

def stem(word):
  stem = step_1a(word)
  stem = step_1b(stem)
  stem = step_1c(stem)
  stem = step_2(stem)
  stem = step_3(stem)
  stem = step_4(stem)
  stem = step_5a(stem)
  stem = step_5b(stem)

  return stem

result = [ { word : stem(word) } for word in tokenize("I agreed with the greatest minds of my generalization destroyed by caresses")]
print(result)
