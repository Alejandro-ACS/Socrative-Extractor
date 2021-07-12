import requests
import json

roomName = str(input("Ingrese el nombre del aula: ")).lower()

url = "https://api.socrative.com/rooms/api/current-activity/" + roomName

data = {
    'room': roomName
}

array1 = requests.get(url, data=data)

if array1.ok:
    cache = json.loads(array1.content)

    if cache != {}:

        activity_id = cache['activity_id']

        url1 = "https://teacher.socrative.com/quizzes/"+ str(activity_id) + "/student?room=" + roomName

        cookies_dict = {
            'sa': 'SA_0AFd_7NneDk0WafSUS0u0fIkHIJFmz3X'
        }

        resp = requests.get(url1, cookies=cookies_dict)

        response = json.loads(resp.content)

        print("\nNombre: " + str(response['name']))

        print("Id: " + str(activity_id))

        print("Numero de preguntas: " + str(len(response['questions'])))

        x = 0

        while x != len(response['questions']):
            
            y = x + 1
            
            if response['questions'][x]['question_image'] == None:
                
                print("\nPregunta " + str(y) + ": " + str(response['questions'][x]['question_text']) + "\n")
            
            else:
                
                print("\nPregunta " + str(y) + ": " + str(response['questions'][x]['question_text']) + "\n(Img url: " + str(response['questions'][x]['question_image']['url']) +")\n")
    
            if str(response['questions'][x]['type']) == "MC" or str(response['questions'][x]['type']) == "TF":
                
                z = 0
                
                while z != len(response['questions'][x]['answers']):
                    
                    a = z + 1
                    
                    print(str(a) + ") " + str(response['questions'][x]['answers'][z]['text']) + " (" + str(response['questions'][x]['answers'][z]['id']) + ")")
                    
                    z = z + 1
            
            elif str(response['questions'][x]['type']) == "FR":
                
                print(" - Respuesta libre")
            
            x = x + 1

    else:

        print("\nAula inactiva")

else:
    
    print("\nNo existe el aula")
