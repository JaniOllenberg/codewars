import re
def solution(s):
    new_string = ''
    new_string = re.sub(r'(?<=\w)([A-Z])', r' \1', s)
    return new_string

#breaks CamelCase with spaces