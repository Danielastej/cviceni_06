SPECIAL_SYMBOL = '!@#$%^&*()-_=+[]{};:,.?'

def analyze_password(
        password,
        min_length = 8,
        require_digit=True,
        require_upper=True,
        require_symbol=False,
        banned_words=None,
):
    is_strong = True
    missing_rules = []
    percent = []
    if not len(password) >= min_length:
        is_strong = False
        missing_rules.append('min_length')
    require_symbol = any(ch in SPECIAL_SYMBOL for ch in password)
    if require_symbol == False:
        is_strong = False
        missing_rules.append('symbol')

    require_digit = any(ch.isdigit() for ch in password)
    if require_digit == False:
        is_strong = False
        missing_rules.append('digit')

    require_upper = any(ch.isupper() for ch in password)
    if require_upper == False:
        is_strong = False
        missing_rules.append('upper')

    if banned_words != None:
        if banned_words in password:
            is_strong = False
            missing_rules.append("banned_word")
    score_percent = ...
    return is_strong, score_percent, missing_rules


def load_signal_from_txt(path):
    with open(path, 'r') as file:
        data = []
        for line in file:
            line = line.strip()
            data.append(float(line))
    return data


import matplotlib.pyplot as plt


def plot_signal(values):
    plt.plot(values)
    plt.show()


def signal_min(values):
    return min(values)

def signal_max(values):
    return max(values)

def signal_avg(values):
    return sum(values)/len(values)


def main():
    values = load_signal_from_txt('ekg_signal.txt')
    print(f'Minimum: {signal_min(values)}, Maximum: {signal_max(values)}, Average: {signal_avg(values)}')
    plot_signal(values)

if __name__ == "__main__":
    main()
