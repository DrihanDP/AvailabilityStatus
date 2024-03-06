#TODO List
# Add employee - must have first name, last name, ID, email
# Remove employee - remove via first name, last name or both, ID, or email. If using first name, and there are multiple, show a list that could be there
# show a tag or coloured square that indicates availablility, eg, isolated for work, available for work, close to being finished, close to starting
# show start and end dates for isolation
# add isolation date that emails everyone the start and end date of the isolation
# edit start and finish date that emails everyone
# display employee info section
# display the availability all the time and dates all the time like a calendar

import Employee 

employee1 = Employee.Employee("Drihan", "du Preez", 1, "d@email.com")
employee2 = Employee.Employee("George", "Smith", 2, "g@email.com")

Employee.Employee.Save(employee1)