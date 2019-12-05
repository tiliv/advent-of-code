from collections import Counter

password_range = (272091, 815433)
candidates = []

for password in range(*password_range):
    password = str(password)
    if ''.join(sorted(password)) != password:
        continue
    repeats = [common[1] for common in Counter(password).most_common(len(password))]
    if 2 not in repeats:
        continue
    candidates.append(password)

print(len(candidates))
