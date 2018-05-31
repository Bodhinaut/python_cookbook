# 1
def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)




# 2
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = record
print (name)
print (email)
print (phone_numbers)

# 3
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)
'''
*trailing_qtr, current_qtr = sales_record
trailing_avg = sum(trailing_qtr) / len(trailing_qtr)
return avg_comparison(trailing_avg, current_qtr)
'''