number_of_bad_grades=int(input())
question=input()
bad_grades=0
sum_grades=0
num_grades=0
num_questions=0
last_question=''

while question!='Enough':
    grade = int(input())
    sum_grades+=grade
    num_grades+=1
    num_questions+=1
    if grade<=4:
        bad_grades+=1
    if bad_grades==number_of_bad_grades:
        print(f'You need a break, {number_of_bad_grades} poor grades.')
        break
    if question!='Enough':
        last_question=question

    question=input()

if bad_grades<number_of_bad_grades:
    print(f'Average score: {(sum_grades/num_grades):.2f}')
    print(f'Number of problems: {num_questions}')
    print(f'Last problem: {last_question}')