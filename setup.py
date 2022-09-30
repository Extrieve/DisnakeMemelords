import os

categories = ['waifu', 'neko', 'bully', 'cuddle', 'cry', 'hug', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush',
 'smile', 'wave', 'highfive', 'handhold', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']

ame_endpoints = ['approved', 'beautiful', 'challenger', 'circle', 'crush', 'dungeon', 'dictator','fire', 'jail', 'missionpassed',
                 'rip', 'utatoo', 'wated']

available_contests = {'codeforces': ('https://play-lh.googleusercontent.com/EkSlLWf2-04k5Y5F_MDLqoXPdo0TyZX3zKdCfsEUDqVB7INUypTOd6AVmkE_X7ej3JuR', '%Y-%m-%dT%H:%M:%S.%LZ'),
                    'top_coder': ('https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/tdenoarg7lu2emnoyu7c', '%Y-%m-%dT%H:%M:%S.%LZ'),
                     'at_coder': ('https://img.atcoder.jp/assets/atcoder.png', '%Y-%m-%dT%H:%M:%S.%LZ'), 
                     'cs_academy': ('https://students.ieee.org/wp-content/uploads/2018/08/csacademy_sponsor.png', '%Y-%m-%dT%H:%M:%S.%LZ'), 
                     'code_chef': ('https://pbs.twimg.com/profile_images/1477930785537605633/ROTVNVz7_400x400.jpg', '%Y-%m-%dT%H:%M:%S.%LZ'), 
                     'hacker_rank': ('https://upload.wikimedia.org/wikipedia/commons/4/40/HackerRank_Icon-1000px.png', '%Y-%m-%dT%H:%M:%S.%LZ'), 
                     'hacker_earth': ('https://upload.wikimedia.org/wikipedia/commons/e/e8/HackerEarth_logo.png', '%Y-%m-%dT%H:%M:%S.%LZ'), 
                     'kick_start': ('https://bookassist.org/wp-content/uploads/2021/07/google-logo.jpg', '%Y-%m-%dT%H:%M:%S.%LZ'), 
                     'leet_code': ('https://leetcode.com/static/images/LeetCode_logo_rvs.png', '%Y-%m-%dT%H:%M:%S.%LZ')}

horoscope = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

tarot_deck = {'The Fool': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/03/the-fool-tarot-card.webp', 'The Magician': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/03/the-magician-tarot-card.webp', 'The High Priestess': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2019/11/the-high-priestess-tarot-card.webp', 'The Empress': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/02/the-empress-tarot-card.webp', 'The Emperor': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2019/08/the-emperor-tarot-card.webp', 'The': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2019/10/the-hierophant-tarot.webp', 'The Lovers': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/07/the-lovers-tarot-card.webp', 'The Chariot': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/07/the-chariot-tarot-card.webp', 'Strength': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/07/strength-tarot-card.webp', 'The Hermit Tarot Card Meaning': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/09/the-hermit-tarot-card-meaning-rider-waite.webp', 'Wheel Of Fortune': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/wheel-of-fortune-tarot-card.webp', 'Justice Tarot': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/justice-tarot-card-meaning.webp', 'The Hanged Man': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2019/09/the-hanged-man-tarot-card-1.webp', 'Death Tarot': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/death-tarot-card-image.webp', 'Temperance Card': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/temperance-card-in-tarot.webp', 'The Devil': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/the-devil-card-upright.webp', 'The Tower Tarot': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/the-tower-tarot-card-meaning.webp', 'The Star Card': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/the-star-card-in-tarot.webp', 'The Moon Tarot': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/the-moon-tarot-card-original.webp', 'The Sun Card': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/the-sun-card-tarot-reading.webp', 'Judgement Tarot': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/judgement-tarot-card-design.webp', 'The World': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/the-world-tarot-card.webp', 'Minor Arcana Suits': 'https://www.alittlesparkofjoy.com/wp-content/uploads/2020/10/minor-arcana-suits-of-wands.webp'}

speech_bubble = ['https://media.tenor.com/images/4e8676ec3940a77980722881e27995bb/tenor.gif',
'https://media.tenor.com/images/c3930fc34f5dc77aafe2acf9297a7f20/tenor.gif', 'https://media.tenor.com/images/5ee71c5e92aa0c578749f458b8afc602/tenor.gif',
'https://media.tenor.com/images/4037651066bbf0c4eb97f379d1f2eccb/tenor.gif', 'https://media.tenor.com/images/4c1acc6ef972b80b2bca5142eb28734b/tenor.gif',
'https://media.tenor.com/images/f7755b9c2f10902e5ea1b60d8a7684ab/tenor.gif', 'https://media.tenor.com/images/c55389e3ac5ca62f7d97fe76e1696177/tenor.gif',
'https://media.tenor.com/images/54beeaa12015bc9c0b36f6c4cefb35e1/tenor.gif', 'https://media.tenor.com/images/23415f6605d95219213ff97b07c55fec/tenor.gif',
'https://media.tenor.com/images/30679b93ea4970b58383e7af4113f976/tenor.gif','https://media.tenor.com/images/1be8cb71862713c2a9aa9164b5f5e88e/tenor.gif',
'https://media.tenor.com/images/fbeb9659afe5728445edc4b7abae829f/tenor.gif', 'https://media.tenor.com/images/05f4d490a2e5dfdd594f8a28ebca6125/tenor.gif',
'https://media.tenor.com/images/d6c0c5142166df78fc60cb0ff7550b25/tenor.gif', 'https://media.tenor.com/images/ee04d828c1a4793a1d2c7dea87548766/tenor.gif',
'https://media.tenor.com/images/20c6559979ac939a54cf16e144ad7903/tenor.gif', 'https://media.tenor.com/images/408947663c4e95dd7fa8bb997d92b8eb/tenor.gif',
'https://media.tenor.com/images/d53f0609c56f814681c0bbca924486d4/tenor.gif', 'https://media.tenor.com/images/88afb6d38e71d39ef442202e6142e7b6/tenor.gif',
'https://media.tenor.com/images/3425ea5f9aaf8be7240c15713fcc719f/tenor.gif']

# get working directory
cwd = os.getcwd()

# load all cog files
cogs = []
for file in os.listdir(cwd + "/cogs"):
    if file.endswith(".py") and '__' not in file:
        cogs.append(f'cogs.{file[:-3]}')