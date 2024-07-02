# TFnet2Steam Text Converter

This is a small Python tool to convert formatted text from [https://www.transportfever.net](https://www.transportfever.net) to [formatted text for Steam content](https://steamcommunity.com/comment/Recommendation/formattinghelp).

All common element types are supported, including urls, lists, tables and more.

## Usage

Extract the HTML content from a transportfever.net page that you want to convert from the page source or the browser developer tool (F12).
Copy it to "input.txt".
Then run the script with Python 3.9 (install BeautifulSoup package).
Your output will be written to "steam_output.txt".
