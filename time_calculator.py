

def add_time(start_time, duration, *day):
   
   days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
   
   [add_hour, add_minutes] = start_time.split(':')
   split_between_AM_PM_start_time = start_time.split(' ')
   start_time = split_between_AM_PM_start_time[0]
   AM_or_PM = split_between_AM_PM_start_time[1]


   [start_hour, start_minutes] = start_time.split(':')
   [add_hour, add_minutes] = duration.split(':')

   next_days = 0

   end_hour = int(start_hour) + int(add_hour)
   end_minutes = int(start_minutes) + int(add_minutes)
   
   if end_minutes >= 60:
      end_minutes = end_minutes - 60
      end_hour = end_hour + 1
   
   if end_hour >= 12:
      quotient, remainder = divmod(end_hour,12)
      if remainder:
         end_hour = remainder
      else:
         end_hour
      
      if end_hour > 12:
         end_hour = end_hour - ((quotient-1)*12)
      
      if quotient > 0:
         if AM_or_PM == 'PM':
            next_days = ((quotient-1) // 2) + 1
         else:
            next_days = quotient // 2
      
      if quotient > 0 and quotient % 2 != 0:
         if AM_or_PM == 'PM':
            AM_or_PM = 'AM'
         else:
            AM_or_PM = 'PM'

   
   # end_hour= "{:02d}".format(end_hour)
   end_minutes = "{:02d}".format(end_minutes)
   
   new_time = f'{end_hour}:{end_minutes} {AM_or_PM}'

   if day:
      current_day = day[0].title()
      if next_days > 0:
         index = days.index(current_day)
         index += next_days % 7 
         if index > 6:
            index = index - 7
         current_day = days[index]
      new_time += f', {current_day}'
   
   if next_days == 1:
      new_time += ' (next day)' 
   elif next_days > 1:
      new_time += f' ({next_days} days later)'
   
   return print(new_time)   
   
add_time('3:00 PM', '3:10')
add_time('11:30 AM', '2:32', 'Monday')
add_time('11:43 AM', '00:20')
add_time('10:10 PM', "3:30")
add_time('11:43 PM', '24:20', 'tueSday')
add_time('6:30 PM', '205:12')



