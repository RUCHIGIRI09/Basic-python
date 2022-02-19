def text_number(number):
    day = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
    }
    return day.get(number, "Invalid number")
def item_get(number):
    word = {
        1: "a Partridge in a Pear Tree",
        2: "two Turtle Doves",
        3: "three French Hens",
        4: "four Calling Birds",
        5: "five Gold Rings",
        6: "six Geese-a-Laying",
        7: "seven Swans-a-Swimming",
        8: "eight Maids-a-Milking",
        9: "nine Ladies Dancing",
        10: "ten Lords-a-Leaping",
        11: "eleven Pipers Piping",
        12: "twelve Drummers Drumming",
    }
    return word.get(number, "Invalid number")
def recite(start, end):
    return_list = []
    ver = start
    add_string = ""
    while(ver<=end):
        counter = ver
        add_string = "On the " + text_number(ver)+" day of Christmas my true love gave to me: "
        if counter == 1:
            add_string += item_get(counter) + "."
            return_list.append(add_string)
        else:
            while (counter>0):
                if counter == 1:
                    add_string += "and " + item_get(counter) + "."
                else:
                    add_string += item_get(counter) + ", "
                counter -= 1
            return_list.append(add_string)
        ver += 1
    return return_list