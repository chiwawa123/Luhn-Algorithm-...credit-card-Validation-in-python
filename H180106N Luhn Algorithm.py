def validate_credit_card_number(card_number):


    #Step 1

    #defining variables

    temp_list=list(str(card_number))
    my_list=[]
    list1 = temp_list[-2::-2]
    list2=temp_list[::-2]
    list2 = [int (n) for n in list2]

    #print(list2)
    my_list=[int(n) for n in list1]

    #print(my_list)
    list1 = [int(n)*2 for n in list1]
    t_list=list1

    for el in list1:
        sum_res=0

        if el>9:
            idx = list1.index(el)
            t_list.pop(idx)

            while el:
                rem = el%10
                sum_res+=rem
                el = el//10
            t_list.insert(idx, sum_res)
    #print(t_list)

    #step 1b

    list1_sum = sum(t_list)
    list2_sum = sum(list2)
    #print(b_list)
    final_sum = list1_sum+ list2_sum
    #print(final_sum)

    if final_sum%10 == 0:
        return True
    return False

# Prompting the user to enter the card number

card_number = input("Enter card number")

result = validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")


#a) 4137 8947 1175 5904 is a valid credit card number
#b) 6499 8024 5027 3568 is an invalid credit card number
#c) 8504 1721 9127 3888 is a valid credit card number
#d) 0043 6687 8348 5480 is an invalid credit card number



