
import requests
import json
import base64
from sympy import *
from sympy.parsing.latex import parse_latex

MATHPIX_APP_ID = 'APP ID'
MATHPIX_APP_KEY = 'API KEY'

def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def mathpix_ocr(encoded_image, is_text=False):
    headers = {
        'app_id': MATHPIX_APP_ID,
        'app_key': MATHPIX_APP_KEY,
        'Content-type': 'application/json'
    }
    payload = {
        'src': 'data:image/png;base64,' + encoded_image,
    }
    
    if is_text:
        # Adjust the endpoint for text OCR
        response = requests.post('https://api.mathpix.com/v3/text',
                                 headers=headers,
                                 data=json.dumps(payload))
    else:
        # Use math OCR for anything else
        payload['formats'] = ['latex_normal']
        response = requests.post('https://api.mathpix.com/v3/latex',
                                 headers=headers,
                                 data=json.dumps(payload))
    
    response.raise_for_status()
    return response.json()


def latex_to_decimal(latex_str):
    try:

        expr = parse_latex(latex_str)
        decimal_value = N(expr, 5) 
        return decimal_value
    except SympifyError:
        print(f"Could not convert LaTeX to decimal: {latex_str}")
        return None

def compare_decimal_values(student_latex, professor_latex, tolerance=1e-5):
    student_decimal = latex_to_decimal(student_latex)
    professor_decimal = latex_to_decimal(professor_latex)
    if student_decimal is not None and professor_decimal is not None:
        return abs(student_decimal - professor_decimal) <= tolerance
    else:
        return False
    
def name_recognition(student_image_path):
   x, y, w, h = 0,0,100,100
   return student_image_path[x:x+w, y:y+h]

def evaluate_answers(student_image_path, professor_image_path):

    student_encoded_image = convert_image_to_base64(student_image_path)
    student_result = mathpix_ocr(student_encoded_image)
    student_latex = student_result.get('latex_normal', '').strip()


    professor_encoded_image = convert_image_to_base64(professor_image_path)
    professor_result = mathpix_ocr(professor_encoded_image)
    professor_latex = professor_result.get('latex_normal', '').strip()
    if '\\frac' in student_latex or '\\frac' in professor_latex:
        is_close_enough = compare_decimal_values(student_latex, professor_latex)
        return is_close_enough, student_latex, professor_latex
    else:
        is_close_enough = compare_decimal_values(student_latex, professor_latex)
        return is_close_enough, student_latex, professor_latex
    
def name_reader(student_name_path):

    encoded_image = convert_image_to_base64(student_name_path)

    result = mathpix_ocr(encoded_image, is_text=True)

    if 'text' in result:
        student_name = result['text'].strip()
        return student_name
    elif 'error' in result:
        print("Error:", result['error'])
        return ""
    else:
        print("No recognizable text found.")
        return ""

#test example - add in name_recongention and adjust return statemnts for implementation purposes
student_name_path = '/Users/johnnie/Desktop/Screenshot 2023-11-11 at 2.26.41 PM.png'
student_image_path = '/Users/johnnie/Desktop/Screenshot 2023-11-11 at 2.13.49 PM.png'
professor_image_path = '/Users/johnnie/Desktop/Screenshot 2023-11-11 at 2.17.12 PM.png'

is_correct, student_latex_output, professor_latex_output = evaluate_answers(student_image_path, professor_image_path)
print(f"Are the answers the same? {is_correct}")
print(f"Student LaTeX Output: {student_latex_output}")
print(f"Professor LaTeX Output: {professor_latex_output}")


student_name = name_reader(student_name_path)
print(f"Student Name: {student_name}")
