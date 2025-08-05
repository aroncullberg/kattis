# n = int(input())
#
# for _ in range(n):
#     sentence = list(input())
#
#     result = []
#     run = True
#     index = 0
#
#     while run:
#         new = sentence.pop(0)
#
#         if new == '<':
#             if len(result) > 0:
#                 # print(len(result), index)
#                 result.pop(index-1)
#             index = max(0, index - 1)
#             if len(sentence) == 0:
#                 run = False
#             # print(new, ''.join(result))
#             continue
#
#         if new == '[':
#             index = 0
#             if len(sentence) == 0:
#                 run = False
#             # print(new, ''.join(result))
#             continue
#
#         if new == ']':
#             index = len(result)
#             if len(sentence) == 0:
#                 run = False
#             # print(new, ''.join(result))
#             continue
#
#         result.insert(index, new)
#         index += 1
#
#         # print(new, ''.join(result))
#
#         if len(sentence) == 0:
#             run = False
#
#     print(''.join(result))
def process_text(text):
    result = []
    cursor = 0

    for char in text:
        if char == '<':
            if cursor > 0:
                cursor -= 1
                result.pop(cursor)
        elif char == '[':
            cursor = 0
        elif char == ']':
            cursor = len(result)
        else:
            result.insert(cursor, char)
            cursor += 1

    return ''.join(result)


n = int(input())
for _ in range(n):
    text = input()
    print(process_text(text))
