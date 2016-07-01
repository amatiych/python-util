'''
    Author: Aleksey Matiychenko
    Created 06/14/2016
    
    This module has some simple date math routins that don't rely on any
    python libraries. In particular the two main functions calculate difference in days 
    between two days and a weekday of any given day
    
'''

days =[31,28,31,30,31,30,31,31,30,31,30,31]


#lambda functions
isleap = lambda y : y  % 4 == 0
days_in_year = lambda y:  366 if isleap(y) else 365

WeekDays = ['Sunday','Monday','Tuesday','Wednesday',
'Thursday','Friday','Saturday']

def date_parts(dt):
    '''
        parse the dates into three idividual parts'
        dates are assumed to be in US format - MM/dd/yyyy
    '''
    toks = dt.split('/')
    m,d,y = [int(s) for s in toks]
    return d,m,y 
     
def dt_cnt(y,m):
   '''
       return number of days in any given year/ month
   '''
   if m == 2 and isleap(y):
       return 29
   return days[m-1]

def intdate(ds):
   '''
       Integer date yyyyMMdd
   '''
   d1,m1,y1 =date_parts(ds)
   return y1 * 10000 + m1 * 100 + d1

def days_in_same_year(ds1,ds2):
   '''
       number of days between two dates in the same year
   '''
   (d1,m1,y1) = date_parts(ds1)
   (d2,m2,y2) = date_parts(ds2) 
   if m1 == m2:
       return d2-d1

   m3 = [mi for mi in range(m1,m2+1)]
   days = [dt_cnt(y1,m) for m in m3]
   endadj = dt_cnt(y2,m2)-d2

   return sum(days)-endadj-d1

def days_span_one_year(ds1,ds2):
  '''
       number of days between two dates in adjucent years (eg. 03/31/2016-02/27/2017)
  '''
  (d1,m1,y1) = date_parts(ds1)
  (d2,m2,y2) = date_parts(ds2)
  days = days_in_same_year(ds1,'12/31/' + str(y1))
  days = days + days_in_same_year('01/01/' + str(y2),ds2)
  return days + 1

def dt_diff(ds1,ds2):
   '''
      Main function to calculate difference in days between two dates
   '''
   if intdate(ds1) > intdate (ds2):
       ds1, ds2 = ds2, ds1 


   (d1,m1,y1) = date_parts(ds1)
   (d2,m2,y2) = date_parts(ds2)
   
   if y1 == y2:
       return days_in_same_year(ds1,ds2)

   years = y2-y1  
   if years == 1:
      return days_span_one_year(ds1,ds2)

   start_year_days = days_in_same_year(ds1,'12/31/' + str(y1))+1
   end_year_days = days_in_same_year('01/01/' + str(y2),ds2)
   middle_years = range(y1+1,y2)
   middle_year_days = sum([days_in_year(y) for y in middle_years])
   return start_year_days + end_year_days + middle_year_days
    

      
def weekday(dt):
    d0 = '01/01/1990' # Sunday. Makes calculation easy
    wd = 0
    diff = dt_diff(dt,d0)+1
    rem = diff % 7
    return WeekDays[rem]
    

if __name__ == '__main__':   
    print(dt_diff('01/01/2015','06/14/2016'))
    print(weekday('06/14/2016')) #should say Tuesday