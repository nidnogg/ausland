from bs4 import BeautifulSoup
import requests 

url = 'https://dri.ufrj.br/index.php/pt/intercambio/chamadas'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# current open exchange programs
program_headers = soup.find("div", itemprop="articleBody").find_all('h3')

current_programs_file = open('out.txt', 'r')
previous_program = current_programs_file.readline()
current_program = program_headers[0].text

if(previous_program.strip() == current_program.strip()):
    print("same")
else:
    current_programs_file.close()
    current_programs_file = open('out.txt', 'w')
    for program in program_headers:
        current_programs_file.write(program.text + '\n')
    