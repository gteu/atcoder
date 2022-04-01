K = int(input())
S = map(int, list(input()[:4]))
T = map(int, list(input()[:4]))


def get_score(X):
    card = [0] * 9
    for x in X:
        card[x - 1] += 1

    score = 0
    for i, c in enumerate(card):
        score += (i + 1) * 10 ** c
    return score, card


score_s, card_s = get_score(S)
score_t, card_t = get_score(T)
card_sum = [card_s[i] + card_t[i] for i in range(9)]

count = 0
for i in range(9):
    for j in range(9):
        if card_sum[i] < K and card_sum[j] < K:
            final_s = score_s + \
                (i + 1) * 10 ** (card_s[i] + 1) - (i + 1) * 10 ** card_s[i]
            final_t = score_t + \
                (j + 1) * 10 ** (card_t[j] + 1) - (j + 1) * 10 ** card_t[j]
            if final_s > final_t:
                if i == j:
                    count += (K - card_sum[i]) * (K - card_sum[i] - 1)
                else:
                    count += (K - card_sum[i]) * (K - card_sum[j])

print(count / (9 * K - 8) / (9 * K - 9))
