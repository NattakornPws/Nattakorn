# == , <>, != , <, >, <=, >=, not, and, or
def ticket(age):
    if age <= 5:
        return 0
    else:
        return 100

def ticket2(age):
    if age <= 5 or age >= 60:
        return 0
    else:
        return 100
def ticket3(age,is_local):
    if (age <= 5 or age >= 60) and is_local == True:
        return 0
    else:
        return 100

def ticket2a(age):
    return 0 if age <= 5 or age >= 60 else 100 #ternary

if __name__ == '__main__':
    ticket(6)
    print(ticket2a(7))
# print(ticket2a(5))
# age = 6
# cost = 0 if age <= 5 or age >= 60 else 100
# print(cost)


# def greeting(lang):
#     if lang == "th":
#         print("sawadee")
#     elif lang == "jp":
#         print("konichiwa")
#     else:
#         print("hello")
#
# def meet_re(eng, interview):
#     if eng > 70 and interview > 80:
#         return True
#     else:
#         return False
#
# greeting("jp")
# print(meet_re(80, 60))