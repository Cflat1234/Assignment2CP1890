from dataclasses import dataclass
from datetime import date,time,datetime

@dataclass
class Task:
    task:str=""
    taskdesc:str=""
    due:date=0
    
    def status(self):
        return self.status
    
@dataclass
class Homework(Task):    
    subject:str=""
    
@dataclass
class Meet(Task):
    location=str=""
    

title=input('Name of Homework: ')
Homework.task=title    
working=input('Define the task: ')
Homework.taskdesc=working
sub=input('What subject is the Homework for: ')
Homework.subject=sub
dues=datetime.strptime(input('When is it due: '),'%Y-%m-%d')
Homework.due=dues
stats=input('Status of Homework: ')
Homework.status=stats

titles=input('Task Name: ')
Meet.task=titles    
workings=input('Define the task: ')
Meet.taskdesc=workings
loc=input('Where is task: ')
Meet.location=loc
duesd=datetime.strptime(input('When is it due: '),'%Y-%m-%d')
Meet.due=duesd
stat=input('Status of Meet: ')
Meet.status=stat


def Homework_print():
    print()
    print('Homework:')
    print(f'Task Name:              {Homework.task}')
    print(f'Task Description:       {Homework.taskdesc}')
    print(f'Due Date:               {Homework.due}')
    print(f'Status:                 {Homework.status}')
    print()

def meet_print():   
    print()
    print('Meeting:')
    print(f'Task Name:              {Meet.task}')
    print(f'Task Description:       {Meet.taskdesc}')
    print(f'Due Date:               {Meet.due}')
    print(f'Status:                 {Meet.status}')
    
Homework_print()    
meet_print()   