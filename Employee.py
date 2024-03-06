class Employee:
    def __init__(self, firstName, lastName, ID, email):
        self.employeeList = []
        self.firstName = firstName
        self.lastName = lastName
        self.ID = ID
        self.email = email

    def AddEmployee(self, employee):
        self.employeeList.append(employee)

    def RemoveEmployee(self):
        pass
        # pop from list 
    
    def Save(self):
        for val in self.employeeList:
            print(val)
        # with open("AvailabilityStatusInfo.txt", "w") as f:
        #     for items in self.employeeList:
        #         f.write(items)