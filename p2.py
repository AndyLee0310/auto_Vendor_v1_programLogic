def calculator_letter(text):
    result = {}
    text_upper = text.upper()
    for i in text_upper:
        if i is not ' ':
            result[i] = text_upper.count(i)
    sorted_result = dict(sorted(result.items()))
    for i in sorted_result:
        print(i, sorted_result[i])

text = "Hello welcome to Cathay 60th year anniversary"
calculator_letter(text)