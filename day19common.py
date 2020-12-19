def is_valid(rules, message, patterns):
    if len(message) == 0 and any([len(pattern) == 0 for pattern in patterns]):
        return True
    if len(message) > 0 and all([len(pattern) == 0 for pattern in patterns]):
        return False
    if len(message) == 0 and all([len(pattern) > 0 for pattern in patterns]):
        return False
    for pattern in patterns:
        if type(pattern[0]) == str:
            if message[0] == pattern[0] and is_valid(rules, message[1:], [pattern[1:]]):
                return True
        else:
            new_patterns = [p + pattern[1:] for p in rules[pattern[0]]]
            if is_valid(rules, message, new_patterns):
                return True
    return False
