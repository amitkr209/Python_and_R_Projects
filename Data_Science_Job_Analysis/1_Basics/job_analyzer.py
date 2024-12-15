
def calculate_salary(base_salary, bonus_rate=0.10):
    """
    Calculate the Total Salary based on the Base Salary and the Bonus Rate.

    Args:
        base_salary(float): The base salary.
        bonus_rate(float): The bonus rate. Default is 0.10.

    Returns:
        float: The Total Salary
    """
    return base_salary * (1 + bonus_rate)

def calculate_bonus(total_salary, base_salary):
    """
    Calculate the bonus Rate base on the Total Salary and the Base Salary.

    Args:
        total_salary(float): The Total Salary.
        base_salary(float): The Base Salary.

    Returns:
        float: The Bonus Rate
    """
    return (total_salary - base_salary) / base_salary
