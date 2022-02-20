class Luhn:    
    def __init__(self, card_num):        
        self.card_num = ""
        if len(card_num.replace(" ", "")) <= 1 or not card_num.replace(" ", "").isdecimal():
            self.card_num = "ER"
        else:
            self.card_num = card_num.replace(" ", "")[::-1]
    def valid(self):       
        if self.card_num == "ER":
            return False
        else:
            digit_total = 0
            for i, d in enumerate(self.card_num):
                if i % 2 == 0:
                    digit_total += int(d)
                else:
                    d_times_2 = 2 * int(d)
                    if d_times_2 < 10:
                        digit_total += d_times_2
                    else:
                        digit_total += d_times_2 - 9
            return bool(digit_total % 10 == 0)
