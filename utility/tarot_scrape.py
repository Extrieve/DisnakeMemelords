import requests
from bs4 import BeautifulSoup

def scrape_tarot():
    url = 'https://www.alittlesparkofjoy.com/tarot-cards-list/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    cards = soup.find_all('div', class_='wp-block-image')

    deck = dict()
    for card in cards:
        card_name = card.find('img')['alt']
        card_url = card.find('img')['data-lazy-src']
        
        card_name = [x.capitalize() for x in card_name.split()]
        card_name = ' '.join(card_name[:-2])

        if 'modern' not in card_name.lower():
            deck[card_name] = card_url

    return deck

def main():
    deck = scrape_tarot()
    print(deck)


if __name__ == "__main__":
    main()