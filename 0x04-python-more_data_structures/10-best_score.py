#!/usr/bin/python3

def best_score(a_dictionary):
    max_value = None
    best_key = None

    if a_dictionary is None:
        return None

    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if max_value is None or value > max_value:
                max_value = value
                best_key = key

    return best_key
