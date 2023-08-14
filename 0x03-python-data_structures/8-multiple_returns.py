#!/usr/bin/python3

def multiple_returns(sentence):
    sent_len = len(sentence)
    empty_tuple = ()
    non_empty_tuple = ()
    if sent_len == 0:
        empty_tuple = (0, None)
        return empty_tuple
    elif sent_len > 0:
        first_char = sentence[0]
        non_empty_tuple = (sent_len, first_char)
        return non_empty_tuple


# for testing function
if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
