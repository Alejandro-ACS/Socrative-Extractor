class Question:
    def __init__(self, question_type, question_text, question_image):
        self.question_type = question_type
        self.question_text = question_text
        self.question_image = question_image
        self.question_image_url = None
        self.answers = []
        self.image = None

    def chatgpt_format(self):
        question = self.question_text
        if self.question_type == "MC" or self.question_type == "TF":
            for answer in self.answers:
                question += "\n- " + answer.answer_text
        return question

    def print_simple_format(self):
        print("\n" + self.question_text)
        if self.question_type == "MC" or self.question_type == "TF":
            for answer in self.answers:
                print("- " + answer.answer_text)

    def print_complex_format(self):
        print("\n" + self.question_text)
        if self.question_image is not None:
            print("(Img url: " + self.question_text + ")\n")
        if self.question_type == "MC" or self.question_type == "TF":
            for answer in self.answers:
                print("- " + answer.answer_text + " (" + answer.answer_id + ")")
        elif self.question_type == "FR":
            print("- Free answer")


class Answer:
    def __init__(self, answer_text, answer_id):
        self.answer_text = answer_text
        self.answer_id = answer_id
