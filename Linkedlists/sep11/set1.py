set1 = {'this', 'is', 'a','set'}

set2 = {'that','is', 'a', 'football'}

print(set1.intersection(set2))

# hashing is that we can convert some object (eg string ) into integer

my_string = "ABC",


print(hash(my_string)%8)

print(hash(2))

big_list =  list(range(1000000))
big_set =  set((range(100000)))

for i in range(1000000):
    if -1 in big_set:
        print("found")