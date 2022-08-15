# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


ages = {"0-4 years":0,"5-14 years":0,"15-19 years":0,"20-24 years":0,"25-34 years":0,"35-44 years":0, "45-54 years":0, "55-64 years":0,
        "65-74 years":0, "75-84 years":0, "85 years and over":0}
m_ages = {"0-4 years":0,"5-14 years":0,"15-19 years":0,"20-24 years":0,"25-34 years":0,"35-44 years":0, "45-54 years":0, "55-64 years":0,
        "65-74 years":0, "75-84 years":0, "85 years and over":0}
f_ages = {"0-4 years":0,"5-14 years":0,"15-19 years":0,"20-24 years":0,"25-34 years":0,"35-44 years":0, "45-54 years":0, "55-64 years":0,
        "65-74 years":0, "75-84 years":0, "85 years and over":0}










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

#gets a list of the number of people for each age group
with open('Albury_Age.csv') as f:
    males = []
    females = []
    for line in f:
        line = line.replace(',','')
        line = line.split('"')
        if line[0] in ages:
            if ages[line[0]] == 0:
                ages[line[0]] = line[5]
                m_ages[line[0]] = line[1]
                f_ages[line[0]] = line[3]

print(ages)
print(m_ages)
print(f_ages)