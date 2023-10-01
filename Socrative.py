import json
import Network
import Parser


def main():
    room_code = str(input("Ingrese el nombre del aula: ")).lower()
    response_api = Network.get_api_data(room_code=room_code)

    if response_api.ok:
        api_json_content = json.loads(response_api.content)
        if api_json_content != {}:
            activity_id = str(api_json_content['activity_id'])
            response_quiz = Network.get_quiz_data(activity_id=activity_id, room_code=room_code)
            quiz_json_content = json.loads(response_quiz.content)
            print("\n")
            print("Nombre: " + str(quiz_json_content['name']))
            print("Id: " + activity_id)
            print("Numero de preguntas: " + str(len(quiz_json_content['questions'])))
            questions = Parser.get_questions_from_quiz_content(quiz_json_content=quiz_json_content)
            for question in questions:
                question.print_simple_format()
        else:
            print("\nAula inactiva")
    else:
        print("\nNo existe el aula")


if __name__ == '__main__': main()
