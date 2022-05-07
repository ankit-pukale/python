#continue -->make the code to skip to next line of loop
# shopping_list=["veg1","veg2","veg3","nveg","veg4","veg5"]
# for item in shopping_list:
#     if item!="nveg":
#         continue
#     print(f"Buy  item {item}")
#using Break 
shopping_list=["veg1","veg2","veg3","nveg","veg4","veg5"]
for item in shopping_list:
    if item=="nveg":
        break
    else:print(f"Buy  item {item}")