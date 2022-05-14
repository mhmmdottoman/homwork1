def main():
    username=input('enter user name: ')
    filename='questions,answers.csv'
    questions=extractfield(filename,1)
    answers=extractfield(filename,2)
    ta=0
    for i in range(len(questions)):
        print(questions[i])
        a=input()
        if a == answers[i]:
            ta+=1
    writeresault(username,ta)

def extractfield(filename,n):
    infile = open(filename, 'r')
    return [x.rstrip().split(',')[n-1] for x in infile]

def writeresault(name,ta):
    outfile=open('result.csv','w')
    result=name+","+str(ta)
    print(result)
    outfile.write(result)
    outfile.close()

main()
