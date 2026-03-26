
tech_name = 'Power BI'

print('1 current tech tech_name = ', tech_name)

def current_tech():
    global tech_name
    print('2 current tech tech_name = ', tech_name)
    
    tech_name = 'Python'
    print('3 current tech tech_name = ', tech_name)

current_tech()
print('4 current tech tech_name =' , tech_name)