def calculate_balance(df):
    income = df[df['type'] == 'credit']['amount'].sum()
    expense = df[df['type'] == 'debit']['amount'].sum()
    net = income - expense
    return income, expense, net
