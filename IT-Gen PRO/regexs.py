#Домашнє завдання:
#1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї
#літери R, за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та 
#нижній регістр.
#2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
#3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
#Вимоги:
#-Цифри (0-9).
#-лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
#-у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
#-Символ "-" не може повторюватися.
#4. Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10
#символів, що містить лише літери та цифри.

#================================================================================
#=============================TASK 1=============================================
#================================================================================

import re

pat = r'Rb+r'
text = input('text: ')
print(re.findall(pat, text) or False)

#================================================================================
#=============================TASK 2=============================================
#================================================================================

def is_valid_creditcard(cardnum):
    if '-' in cardnum:
        num_pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    elif ' ' in cardnum:
        num_pattern = r'^\d{4} \d{4} \d{4} \d{4}$'
    return re.search(num_pattern, cardnum) and True or False

ccard = input('credit card: ')
print(is_valid_creditcard(ccard))

#================================================================================
#=============================TASK 3=============================================
#================================================================================

def is_valid_email(e_mail):
    if e_mail.count('-') > 1:
        return False
    e_mail_pattern = r'^[0-9A-Za-z][0-9A-Za-z_-]*@[A-Za-z]+\.[A-Za-z]{2,}$'
    return re.search(e_mail_pattern, e_mail) and True or False

post = input('email: ')
print(is_valid_email(post))

#=================================Alternative==extended========================

def is_valid_email_s(e_mail):
    e_mail = e_mail.lower()
    if re.split(r'@', e_mail)[0].count('-') > 1:
        return False
    e_mail_pattern = r'^[0-9a-z][0-9a-z_-]*@[a-z]+(-[a-z]+)*(\.[a-z]{2,4})*\.[a-z]{2,}$'
    return re.search(e_mail_pattern, e_mail) and True or False

post = input('email: ')
print(is_valid_email(post))

#================================================================================
#=============================TASK 4=============================================
#================================================================================

def is_valid_login(login):
    login_pattern = r'^([0-9A-Za-z]){2,10}$'
    return re.search(login_pattern, login) and True or False

login = input('login: ')
print(is_valid_login(login))
