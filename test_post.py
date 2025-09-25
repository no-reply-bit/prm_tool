import requests

# Personを1件追加
person = {
    "name": "Taro Yamada",
    "title": "Engineer",
    "company": "XYZ",
    "location": "Osaka",
    "linkedin_url": "https://www.linkedin.com/in/taro",
    "tags": "ai,ml",
    "hotness": 3,
    "fit": 2
}
res_p = requests.post("http://127.0.0.1:8000/persons", json=person)
print("persons response:", res_p.json())

# Touchを1件追加
touch = {
    "person_id": 1,  # ここはさっき登録した id に合わせる
    "channel": "Comment",
    "time": "2025-09-25 19:00",
    "note": "投稿にコメント",
    "outcome": "反応あり",
    "next_time": "2025-09-30 09:00"
}
res_t = requests.post("http://127.0.0.1:8000/touches", json=touch)
print("touches response:", res_t.json())
