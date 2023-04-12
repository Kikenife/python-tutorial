class Employee:
    """Employee's details and annual salary"""
    def __init__(self, first_name, last_name, annual_salary):
        """Inintialize the attribute"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Give the employee a raise"""
        self.annual_salary += amount
