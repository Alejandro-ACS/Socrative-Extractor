import Utils
from Models import *


def get_questions_from_quiz_content(quiz_json_content):
    array = []
    for question in quiz_json_content['questions']:
        question_text = Utils.clean_html(str(question['question_text']))
        question_type = str(question['type'])
        question_image = question['question_image']

        question_structure = Question(question_type=question_type,
                                      question_text=question_text,
                                      question_image=question_image)

        if question_image is not None:
            question_image_url = str(question['question_image']['url'])
            question_structure.question_image_url = question_image_url
        if question_type == "MC" or question_type == "TF":
            for answer in question['answers']:
                answer_text = Utils.clean_html(str(answer['text']))
                answer_id = Utils.clean_html(str(answer['id']))
                answer_structure = Answer(answer_text=answer_text,
                                          answer_id=answer_id)
                question_structure.answers.append(answer_structure)

        array.append(question_structure)
    return array
