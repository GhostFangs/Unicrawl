from pddiktipy import api
from pprint import pprint as p

a = api()

keywords = input("Masukkan kata kunci pencarian, pisahkan dengan koma jika lebih dari satu: ")

keywords_list = [keyword.strip() for keyword in keywords.split(",")]

for keyword in keywords_list:
    print(f"\nMencari data untuk: {keyword}")
    result = a.search_all(keyword)
    if result:
        p(result)
    else:
        print(f"{keyword} not found.")
    print("\n" + "-"*50 + "\n")
