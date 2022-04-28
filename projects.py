# This file contains all related information of all portfolio projects
from flask import url_for

web_scraper = {
    "name": "Electrical Appliance Price Scraper",
    "image": 'img/Price-scraper-img.jpg',
    "description": "Automatically scrapes and compares the prices of household electrical appliances on several websites and exports it as an excel file using Python.",
    "github_link": "https://github.com/JameaPlays/appliance_price_scraper",
}

morse_code = {
    "name": "Morse Code Converter",
    "image": 'img/morse-code-img.jpg',
    "description": "A text based morse code converter, allowing you to encode and decode Morse Code messages to send to your friends for fun.",
    "github_link": "https://github.com/JameaPlays/Morse_Code_Translator",
}

tic_tac_toe = {
    "name": "Tic-Tac-Toe",
    "image": 'img/tic-tac-toe-img.jpg',
    "description": "A text based Tic-Tac-Toe game, a childhood game that everyone played.",
    "github_link": "https://github.com/JameaPlays/tic_tac_toe.git",
}

all_projects = [web_scraper, morse_code, tic_tac_toe]
