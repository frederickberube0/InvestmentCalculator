
def main():
    use_own_values_prompt = str.upper(input("Do you want to use your own values? [Y/N]: "))
    while use_own_values_prompt != "Y" and use_own_values_prompt != "N":
        use_own_values_prompt = str.upper(input("Incorrect input please enter Y or N. Do you want to use your own values? [Y/N]: "))

    if use_own_values_prompt == "Y":
        values = Use_Own_Values()
    else:
        values = Use_Default_Values()

def Use_Own_Values():
    """Set the values for the calculator to the user's values"""
    print("Enter the initial investment amount ($): ", end=None)
    initial_value = get_integer_value()
    
    print("Enter the expected average inflation rate (%): ")
    inflation_rate = get_float_value()

    print("Enter the length of the investment (yrs): ")
    investment_length = get_integer_value()

    print("Enter the expected interest rate (%): ")
    interest_rate = get_float_value()

    print("Enter the expected annual contribution ($): ")
    annual_contribution = get_integer_value()

    print("Enter the expected contribution growth rate (%): ")
    annual_contribution_growth_rate = get_float_value()

    return {"initial_value": initial_value, "inflation_rate": inflation_rate, "investment_length": investment_length, "interest_rate": interest_rate, "annual_contribution": annual_contribution, "annual_contribution_growth_rate": annual_contribution_growth_rate}

def Use_Default_Values():
    """Set the values for the calculator to the default values"""
    pass

def get_integer_value() -> int:
  """Returns an inputted integer"""
  user_value = input("")
  try:
    return int(user_value)
  except ValueError:
    print(f"{user_value} is not a valid value. Please try again.")
    return get_integer_value()
  
def get_float_value() -> float:
  """Returns an inputted integer"""
  user_value = input("")
  try:
    return float(user_value)
  except ValueError:
    print(f"{user_value} is not a valid value. Please try again.")
    return get_integer_value()