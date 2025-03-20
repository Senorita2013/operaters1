#arithmetic,comparision,assignment

t1=98
t2=94
t3=41
t4=95
t5=11

sum=t1+t2+t3+t4+t5
print(sum)

average=sum/5
print("The average height of a tree is",average)


#denominations in 100,50,10
amount=int(input("Please enter your amount"))

note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10

print("The notes of 100",note_100)
print("The notes of 50",note_50)
print("The notes of 10",note_10)

#average marks
print("Enter marks in 3 subjects")
s1=int(input())
s2=int(input())
s3=int(input())

sum1=s1+s2+s3
print(sum1)

percentage=(sum1/300)*100
print(percentage)