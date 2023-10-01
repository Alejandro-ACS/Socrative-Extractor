import requests
import Constants


def get_api_data(room_code):
    url_api = Constants.socrative_api + room_code
    data = {
        'room': room_code
    }
    return requests.get(url_api, data=data)


def get_quiz_data(activity_id, room_code):
    url_quizzes = Constants.socrative_quizzes_url + activity_id + Constants.socrative_quizzes_path + room_code
    cookies_dict = {
        'sa': 'SA_0AFd_7NneDk0WafSUS0u0fIkHIJFmz3X'
    }
    return requests.get(url_quizzes, cookies=cookies_dict)
