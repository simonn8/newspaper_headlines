import json

headlines = []
with open('daily_mail_headlines.jsonl') as f:
    for line in f.readlines():
        print(line[:100])
        headline = json.loads(line)
        headlines.append(headline)

for idx, headline in enumerate(headlines):
    print(idx+1, headline["timestamp"])