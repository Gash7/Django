from django.shortcuts import render
import requests

def getstudent(request):
    response = requests.get('http://127.0.0.1:8000/api')
    all_topics_json = response.json()
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5',all_topics_json)
    listOfTopics = []
    for item in all_topics_json :
        print('Inside of Json object')
        tp = Topics(item['Id'],item['Name'],item['Age'],item['gender'],item['Country'],item['skills'],item['created_at'],item['updated_at'],item['text'])
        listOfTopics.append(tp)
    return render(request, 'home.html', {"mylist" : listOfTopics})



def saveData(request):
    r = requests.post('http://127.0.0.1:8000/api', request.POST)

class Topics:

    def __init__(self,Id,Name,Age,gender,Country,skills,created_at,updated_at,text):
        self.Id = Id
        self.Name = Name
        self.Age = Age
        self.gender=gender
        self.Country=Country
        self.skills=skills
        self.created_at = created_at
        self.updated_at = updated_at
        self.text=text


    def __str__(self):
        return " ID : {} \n Name : {} \n  Age : {} \n gender:{} \n  Country: {} \n Skills: {} \n CreatedAt : {} \n UpdatedAt :{} \n text :{} \n ".format(self.Id,self.Name,self.Age,self.gender,self.Country,self.skills,self.created_at,self.updated_at,self.text)