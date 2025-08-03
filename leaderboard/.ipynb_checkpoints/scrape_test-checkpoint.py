import requests, datetime, csv, time, asyncio, aiohttp
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "kattis-friends-tracker/1.0 (+https://github.com/you)"}
FRIENDS  = ["aron-cullberg", "s4andersson", "rasmus-melin", "viktor6"]

def parse_profile(html: str) -> float:
    soup = BeautifulSoup(html, "html.parser")
    label = soup.find("span", class_="info_label", string="Score")
    if not label:
        raise ValueError("Score label not found – page layout changed?")
    score_txt = label.find_next("span", class_="important_text").text
    return float(score_txt)

async def fetch_one(session, handle):
    url = f"https://open.kattis.com/users/{handle}"
    async with session.get(url, headers=HEADERS, timeout=30) as r:
        r.raise_for_status()
        score = parse_profile(await r.text())
        return handle, score

async def snapshot():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, h) for h in FRIENDS]
        results = await asyncio.gather(*tasks)

    ts = datetime.datetime.utcnow().isoformat(timespec="seconds")
    with open("points.csv", "a", newline="") as f:
        w = csv.writer(f)
        for handle, score in results:
            w.writerow([ts, handle, score])

if __name__ == "__main__":
    asyncio.run(snapshot())
