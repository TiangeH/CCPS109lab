# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:43:44 2020

@author: Tiange
"""

### 1/13
def ryerson_letter_grade(pct):
    #pct = int(input("What is your grade?"))
    if pct >= 90:
            return "A+"
    elif pct >= 85:
            return "A"
    elif pct >= 80:
            return "A-"
    elif pct >= 77:
            return "B+"
    elif pct >= 73:
            return "B"
    elif pct >= 70:
            return "B-"
    elif pct >= 67:
            return "C+"
    elif pct >= 63:
            return "C"
    elif pct >= 60:
            return "C-"
    elif pct >= 57:
            return "D+"
    elif pct >= 53:
            return "D"
    elif pct >= 50:
            return "D-"
    else:
        return "F"

ryerson_letter_grade(62)

### 2/13

def is_ascending(items):
    for i in range(0,len(items)-1):
               
        if items[i]>=items[i+1]:
            print(items[i],items[i+1])
            return False
            break 
        print(items[i],items[i+1])
    else:
        return True


### 3/13
worth = {'a':1,
    'b':3,
    'c':3,
    'd':2,
    'e':1,
    'f':4,
    'g':2,
    'h':4,
    'i':1,
    'j':8,
    'k':5,
    'l':1,
    'm':3,
    'n':1,
    'o':1,
    'p':3,
    'q':10,
    'r':1,
    's':1,
    't':1,
    'u':1,
    'v':4,
    'w':4,
    'x':8,
    'y':4,
    'z':10,
    }
def scrabble_value_1(word, multipliers=None):
      #multipliers=list(multipliers)
      word=word.lower()
      an_t=list(word)
      #an_t=word.split(",")
      #an_t=split(word)
      list1=[worth.get(n,n) for n in an_t]
      if multipliers is not None:
          if len(list1)==len(multipliers):
              total_r=[]
              for i in range(0,len(list1)):
                  total_r.append(list1[i]*multipliers[i])                  
              return sum(total_r)
      if multipliers is None:
          return sum(list1)
word='hexahydroxycyclohexane'
scrabble_value_1(word,multipliers=None)


### 4/13

def count_and_say(digits):
    aux=str(digits)
    aux=aux.replace(",","")
    aux=aux.replace("'","")
    aux=aux.replace("(","")
    aux=aux.replace(")","")
    aux_list = list(aux)
    result_1=[]
    count=1
    final_str=''
    for i in range(len(aux_list)):
        #print("count before loop",count)
        if i==len(aux_list)-1:            
            result_1.append(str(count))
            result_1.append(aux_list[i])            
        elif aux_list[i]==aux_list[i+1]:
            count+=1            
        else:            
            result_1.append(str(count))
            result_1.append(aux_list[i])
            count=1            
    #return result_1
    for element in result_1:
        final_str+=element
    return final_str   
    
#for i in result_1:
    #print (i[0]+str(i[1]),end="")


def count_and_day(digits):
    digits_t=list(digits)
    count=1
    result_1=[]
    for i in range(len(digits_t)):
        if i==len(digits_t)-1:
            result_1.append([count,digits_t[i]])
        elif digits_t[i]==digits_t[i+1]:
            count+=1
        else:
            result_1.append([count,digits_t[i]])
            count=1
            print("every iteration",count)
            return result_1   
    for i in result_1:
        print(i[0]+str(i[1]),end="")
    
digits='333388822211177'
count_and_day(digits)   
#5/13-----------7/110
    
number=98053
numberstr=str(number)
#type(numberstr)
#len(numberstr)%2!=0
#numberstr=list(numberstr)
if len(numberstr)%2 ==0 or numberstr.count('0')>1: #or numberstr.count['9']!=1:
    print("False")
else:
    middle_word=numberstr[len(numberstr)//2]
    print(middle_word)
    if middle_word == '0':
        print("TRUE")        
    if middle_word !='0':
        print("FAlSE")
        
    
 #6/13---82/110   
def sort_list(nbr_list):
    print(sorted(nbr_list, key = nbr_list.count, reverse=True))
    
sort_list([ 3, 3, 6, 6, 6, 5, 5, 8 ])

######7/13-----75/110
def iterated_remove_pairs(items):
    i = 0 
    prev = None
    while i < len(items):
        number = items[i]
        print("original number:",number)
        print("starting i:",i)
        if number == prev:
            items.pop(i)
            items.pop(i -1)
            i -= 1
            print(items)
            print(i)
        else:
            i += 1
            print(i)
        if i:
            print("if after else:",i)
            prev = items[i -1]
            print("prev:",prev)
        else:prev = None
    return items
print(iterated_remove_pairs([42, 5, 8, 2, 99, 99, 2, 7, 7, 8, 5]))


###8/13 --------41/110
def create_zigzag(rows,cols,start=1):
    n=rows*cols
    new_list=list(range(start,n+1))
    print(new_list)

    result_list = []
    while new_list:
        result_list.append(new_list[:cols])            
        new_list = new_list[cols:]
    
    for i in range(0,len(result_list)):
        if i % 2!=0:
            result_list[i]=sorted(result_list[i],reverse=True)
    return result_list
create_zigzag(10,1,39)

def create_zigzag(rows,cols,start=1):
    n=rows*cols
    new_list=list(range(start,start+n))
    print(new_list)

    result_list = []
    while new_list:
        result_list.append(new_list[:cols])            
        new_list = new_list[cols:]
    
    for i in range(0,len(result_list)):
        if i % 2!=0:
            result_list[i]=sorted(result_list[i],reverse=True)
    return result_list
        
create_zigzag(3,5,)



#9/13---------------5/110
def only_odd_digits(n):
    arr_y=list(str(n))
    #tr=None
    for i in range(0,len(arr_y)):
        #tr=True
        if arr_y[i] in ['2','4','6','8','0']:
            return False
            break
    else:
        return True



##10/13-------------76/110

def expand_intervals(intervals):
    new_list=list(intervals.split(','))
    result_1=[]
#new_list=list(new_list.split(','))
    final_list=[]
    for i in range(0,len(new_list)):
        print(i)
        print(new_list[i])
        
        if new_list[i].find("-") == -1:
            result_1.append(int(new_list[i]))
        elif new_list[i].find("-") > 0:
            #result_1=[]
            index_n=new_list[i].index('-')
            min_nbr=int(new_list[i][:index_n])
            max_nbr=int(new_list[i][index_n+1:])
            changed_nbr=list(range(min_nbr,max_nbr+1))
            result_1.append(changed_nbr)    
    for ele in result_1:
            if type(ele)==list:
                for sub_ele in ele:
                    final_list.append(sub_ele)
            else:
                print(ele)
                final_list.append(ele)
    return final_list
    
    #return result_1
del intervals

intervals='1,3-9,12-14,9999'
expand_intervals(intervals)


#this steo is to concate sublist and int together into one list
test_1=[[4, 5, 6], [10, 11, 12], 16]
type(test_1[2])
final_list=[]
for i in test_1:
        if type(i)==list:
            for j in i:
                print("j:",j)
                final_list.append(j)
        else:
            print(i)
            final_list.append(i)
print(final_list)
type(test_1[2])
#new_list_merged=[]
#for i in result_1:
    #new_list_merged += i
#print(new_list_merged)
print(result_1)

##11/13-------------32/110

del items
def first_preceded_by_smaller(items,k):
    count=[]
    k=k
    fit_situation=None
    for i in range(0,len(items)):
        print("the value is:",items[i])
        for j in range(0,len(items)):
            if items[j] <items[i]:
                #if items.index(items[j])<items.index(items[i]):
                if j<i:
                    print(items[j])
                #if items.index(j)<items.index(i)
                    count.append(items[j])
                #sum_value=len(count)        
        print("total:",len(count))
        
        #if sum_value==k:
        if len(count)==k:
                 #print("fit situation:",items[i])
            fit_situation=items[i]
            print("item is:",items[i])
        #count=[]
        #return fit_situation

items=['bob', 'carol', 'tina', 'alex', 'jack', 'emmy',
'tammy', 'sam', 'ted']
k=4
first_preceded_by_smaller(items,k) 



------#don't remove the code above

def first_preceded_by_smaller(items, k = 2):
    sublist = [[]] 
    for i in range(len(items) + 1):
        for j in range(i + 1, len(items) + 1):
            sub = items[i:j] 
            sublist.append(sub)
            x = sublist[1:len(items) + 1]
            y = [len([j for j in i if j < i[-1]]) for i in x]
        for i in y:
            if i >= k:
                return items[y.index(i)]
            if False:
                return None  

items=[42, 99, 16, 55, 7, 32, 17, 18, 73]
k=3
first_preceded_by_smaller(items,k)

def first_preceded_by_smaller(items, k = 2):
    sublist = [[]] 
    for i in range(len(items) + 1):
        for j in range(i + 1, len(items) + 1):
            sub = items[i:j] 
            print("sub",sub)
            sublist.append(sub)
            print("sublist",sublist)
            x = sublist[1:len(items) + 1]
            print("x",x)
            y = [len([j for j in i if j < i[-1]]) for i in x]
            print("y",y)
        for i in y:
            if i >= k:
                return items[y.index(i)]
            if False:
                return None  








--------------------------------------------------------------
def map_book(tokens):
    hash_map = []

    if tokens is not None:
        for element in tokens:
            # Remove Punctuation
            #word = element.replace(",","")
            #word = word.replace(".","")

            # Word Exist?
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        return hash_map
    else:
        return None   
tokens=['tom', 42, 'bob', 'bob', 99,
'bob', 'tom', 'tom', 99]


















    
    #fit_situation=None
    for i in range(0,len(items)):
        print("the value is:",items[i])
        for j in range(0,len(items)):
            if items[j] <items[i]:
                if items.index(items[j])<items.index(items[i]):
                #print(items[j])
                #if items.index(j)<items.index(i)
                    count.append(items[j])
        #sum_value=len(count)        
        print("total:",len(count))
        if len(count)==k:
            return items[i]
            break
             #print("fit situation:",items[i])
             #fit_situation=items[i]
        count=[]
        #print("fit:",fit_situation)
         


items=['bob', 'carol', 'tina', 'alex', 'jack', 'emmy','tammy', 'sam', 'ted'] 
k=4
first_preceded_by_smaller(items,k)
#items.index(items[j])<items.index(items[i])
first_preceded_by_smaller(items,k)

#7/110
def is_cyclops(n):
    numberstr=str(n)
    numberstr=numberstr.replace(",","")
    numberstr=numberstr.replace("(","")
    numberstr=numberstr.replace(")","")
    duplic_ze=numberstr.count('0')
    length_st=len(numberstr)
    if length_st%2 ==0:
        return False
    middle_word=numberstr[len(numberstr)//2]
    if middle_word == '0' and duplic_ze==1:
        return True
    if middle_word !='0' or duplic_ze>1:
        return False

### 26/110
def is_permutation(items,n):
    lengthoflist = len(items) 
    repeated = [] 
    for i in range(lengthoflist): 
        k = i + 1
        for j in range(k, lengthoflist): 
            if items[i] == items[j] and items[i] not in repeated: 
                repeated.append(items[i]) 
    #return repeated 
    if len(repeated)>0:
        return False
    my_list=sorted(items)
    n_len=n
    for i in range(0,n_len-1):
        
        if my_list[-1]!=n_len :
            return False       
        if my_list[i]>=my_list[i+1]:
            return False
            break 
    return True
items=[1]
n=1
is_permutation(items,n)


#---------------------------------after kth occurance :):)
def remove_after_kth(items,k=1):
    k1=k
    unique_list=[] 
    for x in range(0,len(items)):  
        if items[x] not in unique_list:
            unique_list.append(items[x])
        else:
            print(items[x])
        print (unique_list)
    unique_list
    result_1=[] 
    #if len(unique_list)=1:
    #return unique_list[0]*k1
    for t in range(0,len(unique_list)):
        #for i in range(0,len(items)-1):   
        #print("t is:",t,"item is:",items[i])
        indis = [i for i, x in enumerate(items) if x == unique_list[t]]
        #indis=items.index(unique_list[t][,start[,end]])
        if len(indis)>=k1:
            result_1.append(indis[0:k1]) 
        else:
            result_1.append([indis[0]]) # other wise it will be [[0,6],1,[2,3]], have to flat the list
        print(result_1)
    
    #to merge sublist into one
    new_list11=[]
    for ter in result_1:
        for mep in ter:
            new_list11.append(mep)
            print(new_list11)    
      
    
    sorted_numlist=sorted(new_list11)
    
    final_list=[]
    for i in sorted_numlist:
        final_list.append(items[i])
        #print(final_list)
    return final_list

---------------------------------------------------
-------------------------------------------    
text='BOOK ONE: 1805'
\n', 
test_word.replace("\n","")           
def reverse_vowels(text):
    #text=text.replace(",","")
    text=text.replace("'","")
    text=text.replace("(","")
    text=text.replace(")","") 
    text=text.replace("\n","")
    vowels=('aeiouAEIOU')
    vowels_l=list(vowels)
    list_l=list(text)
    capital_w=('ABCDEFGHIGKLMNOPQRSTUVWXYZ')# this is to detect how many upper case in a list
    capital_l=list(capital_w)
    
    v_list=[]
    for i in list_l:
        if i in vowels_l:
            v_list.append(i) #abstract all vowels from the original word and assign a new list
            
    v_list.reverse()
    initial=0
    
    old_index_l=[]                           #create a index list to know all upper case
    for list_l_string in list_l:
        if list_l_string in capital_l:
            #index_p=list_l.index(list_l_string)
            #index_l.append(index_p)
            inds = [gg for gg, searching_w in enumerate(list_l) if searching_w == list_l_string] #this is becuase in the case "BOOK", index will only return the first index
            for all_ins in inds:
                old_index_l.append(all_ins)      #this is becuase append can only append one,so have to create a for
    index_l=[]
    for orig_index in old_index_l:
         if orig_index not in index_l:
             index_l.append(orig_index)        # this is the index used to remove duplicated caused by last step
             
    for y in range(0,len(list_l)):    
        if list_l[y] in vowels_l:
            list_l[y]=v_list[initial]
            initial+=1                        #this is for exchanging the string
    
    #for unlo_s in list_l:
    #   unlo_s.lower()
            
            list_l=[list_strings.lower() for list_strings in list_l] #change all string to lower because upper index will recover those word need upper case
    
    for uncap in range(0,len(list_l)):   
        if uncap in index_l:
            list_l[uncap]=list_l[uncap].upper()
                                                            #to recover the uppder case
    
    final_st=""
    for zz in range(0,len(list_l)):
        final_st+=list_l[zz]   

    return final_st
----------------------------------------------------------------

# to split a list into equivalent chun
#aa=0
#bb=27
#for i in range(aa,bb,3):
#    print(i)
#    x=i
#    result_1.append(l[x:x+3])
#result_1

del items
def turkey_ninthers(items):
    median_l=[]
    k=3    
    len_s=0
    len_e=len(items)
    result_1=[]    
    while len_e >=3: 
        
        for i in range(len_s,len_e,k):
            print(i)
            add_i=i
            result_1.append(items[add_i:add_i+3])
            print(result_1)
            
        for y in range(0,len(result_1)):
            median_s=sorted(result_1[y])
            median_l.append(median_s[1])
            items=median_l
            len_e=len(items)
            median_l=[]
            print(items)
            print(len_e)
    return items
   
items = [55,99,131,42,88,11,17,16,104,2,8,7,0,1,69,8,93,
          9,12,11,16,1,77,90,15,4,123]
turkey_ninthers(items)

for i in range(0,27,3):
    print(i)
    result_1.append(items[i:i+3])
len(result_1)
result_1=[]
result_1.append(items[0:3])
result_1