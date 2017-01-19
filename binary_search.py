numbers=[1,2,3,4,5,6,7,8,9,10]
low_value = 0
high_value = len(numbers)
item_search=9
def binary_search(numbers,low_value,high_value,item_search):
    mid = round((high_value+low_value)/2.0)
    if item_search == mid:
        print ("Item present in the list at index number" + " ", numbers.index(item_search))
    elif item_search < mid:
        print ("Item is smaller than mid")
        high_value = mid-1
        binary_search(numbers,low_value,high_value,item_search)
    else :
        print ("Item is greater than mid")
        low_value = mid + 1
        binary_search(numbers,low_value,high_value,item_search)
binary_search(numbers,low_value,high_value,item_search)
