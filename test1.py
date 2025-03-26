computer_languages = {'C', 'COBOL', 'FOTRAN'}
languages = {'java', 'ada', 'c#', 'python'}
computer_languages.add('go') #{'COBOL', 'FOTRAN', 'C', 'go'}
print(computer_languages)
computer_languages.update(languages)# {'COBOL', 'ada', 'go', 'C', 'c#', 'FOTRAN', 'java', 'python'
print(computer_languages)
computer_languages.remove('java')
print(computer_languages)
computer_languages.clear()
print(computer_languages)
