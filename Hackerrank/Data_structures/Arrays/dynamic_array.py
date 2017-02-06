__author__ = 'anna'

# n = 2
# num_query = 5
# last_answer = 0
# sequence_list = [[] for i in range(n)]
# for query in range(num_query):
#     inp = list(map(int, input().strip().split()))
#     if len(inp) == 3:
#         query, x, y = inp
#         print(query, x, y)
#         if query == 1:
#             sequence_index = (x ^ last_answer) % n
#             sequence_list[sequence_index].append(y)
#             print(sequence_list)
#         elif query == 2:
#             sequence_index = (x ^ last_answer) % n
#             new_last_answer_index = (y % len(sequence_list[sequence_index]))
#             last_answer = sequence_list[sequence_index][new_last_answer_index]
#             print(last_answer)

print('Second time:')

n, num_query = map(int, input().strip().split())
last_answer = 0
sequence_list = [[] for i in range(n)]
for query in range(num_query):
    inp = list(map(int, input().strip().split()))
    if len(inp) == 3:
        query, x, y = inp
        print(query, x, y)
        if query == 1:
            sequence_index = (x ^ last_answer) % n
            sequence_list[sequence_index].append(y)
            print(sequence_list)
        elif query == 2:
            sequence_index = (x ^ last_answer) % n
            new_last_answer_index = (y % len(sequence_list[sequence_index]))
            last_answer = sequence_list[sequence_index][new_last_answer_index]
            print(last_answer)