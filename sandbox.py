__author__ = 'Sylvestre'
import datetime
import mailchimp

date = datetime.datetime(2012,2,3,18,30)
print (date)

list = mailchimp.utils.get_connection().get_list_by_id('7366bb50d3')
