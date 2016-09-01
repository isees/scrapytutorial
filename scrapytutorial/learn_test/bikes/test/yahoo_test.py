import scrapytutorial.learn_test.bikes.yahoo_search as ys

soup = ys.search_data('ride video')
results = soup.find("div", id='web').find_all("li")

for li in results:
    try:
        a = li.find("div", class_="compTitle").a
        title = a.text.strip()
        url = a.get("href")
        abstract = li.find("div", class_="aAbs").text
        print abstract
        print url
        print '\n'
    except Exception:
        continue
