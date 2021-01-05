from bs4 import BeautifulSoup 


with open('file1.html', 'r') as myfile:
    content = myfile.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify)
    # tags = soup.find('h5') #its just find the first tag
    # tags = soup.find_all('h5')
    # print(tags)
    # for tag in tags:
    #     print(tag.text)
    course_cards = soup.find_all('div', class_="card")
    
    for card in course_cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[-1]
        print(f'{course_name} coust about: {course_price}')
        
