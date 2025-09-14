from flask import Flask, render_template, request, jsonify
import os
import PyPDF2
import re

app = Flask(__name__)

# Set upload folder path
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        # Save the file temporarily
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
       
        # Process the PDF and extract text
        extracted_text = extract_text_from_pdf(file_path)
       
        # Analyze the text and generate explanation
        explanation = analyze_blood_report(extracted_text)
       
        return jsonify({'explanation': explanation})

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to analyze the blood report and give explanation
def analyze_blood_report(text):
    # Example: simple analysis by checking common blood components
    explanation = "Blood Report Analysis: \n"
   
    # Dummy example to check for Hemoglobin levels
    hemoglobin_match = re.search(r'Hemoglobin\s*:\s*(\d+\.?\d*)', text)
    if hemoglobin_match:
        hemoglobin_value = float(hemoglobin_match.group(1))
        if hemoglobin_value < 13.5:
            explanation += (
                f"Hemoglobin is low: {hemoglobin_value} g/dL.\n"
                "This may indicate anemia, often caused by iron deficiency or blood loss.\n"
                "Consult a doctor for proper diagnosis and treatment.\n"
            )
        elif hemoglobin_value > 17.5:
            explanation += (
                f"Hemoglobin is high: {hemoglobin_value} g/dL.\n"
                "This may indicate polycythemia, which could cause headaches and fatigue.\n"
                "Consult a doctor to determine the underlying cause.\n"
            )
        else:
            explanation += ""  # No explanation for normal levels

    rbc_match = re.search(r'RBC\s*:\s*(\d+\.?\d*)', text)
    if rbc_match:
        rbc_value = float(rbc_match.group(1))
        if rbc_value < 4.7:
            explanation += (
                f"RBC count is low: {rbc_value} cells/mcL.\n"
                "This may indicate anemia or a bone marrow issue causing low red blood cell production.\n"
                "Consult a doctor to identify the cause and discuss treatment.\n"
            )
        elif rbc_value > 6.1:
            explanation += (
                f"RBC count is high: {rbc_value} cells/mcL.\n"
                "This may indicate polycythemia, dehydration, or a condition increasing red blood cell production.\n"
                "Consult a doctor to evaluate the cause and necessary actions.\n"
            )
        else:
            explanation += "Hi"  # No explanation for normal levels


    wbc_match = re.search(r'WBC\s*:\s*(\d+\.?\d*)', text)
    if wbc_match:
        wbc_value = float(wbc_match.group(1))
        if wbc_value < 4000.0:
            explanation += (
                f"WBC count is low: {wbc_value} cells/mcL.\n"
                "This may indicate leukopenia, often caused by infections or bone marrow disorders.\n"
                "Consult a doctor to investigate the cause and explore treatment options.\n"
            )
        elif wbc_value > 11000.0:
            explanation += (
                f"WBC count is high: {wbc_value} cells/mcL.\n"
                "This may indicate an infection, inflammation, or immune system disorder.\n"
                "Consult a doctor to determine the underlying cause.\n"
            )
        else:
            explanation += ""  # No explanation for normal levels

    platelet_match = re.search(r'Platelets\s*:\s*(\d+\.?\d*)', text)
    if platelet_match:
        platelet_value = float(platelet_match.group(1))
        if platelet_value < 150000:
            explanation += (
                f"Platelet count is low: {platelet_value} mcL.\n"
                "This may indicate thrombocytopenia, which can lead to excessive bleeding or bruising.\n"
                "Consult a doctor to identify the cause and consider treatment options.\n"
            )
        elif platelet_value > 450000:
            explanation += (
                f"Platelet count is high: {platelet_value} mcL.\n"
                "This may indicate thrombocytosis, possibly due to an underlying condition like inflammation or bone marrow disorders.\n"
                "Consult a doctor for further evaluation and advice.\n"
            )
        else:
            explanation += ""  # No explanation for normal levels


    glucose_match = re.search(r'Glucose\s*:\s*(\d+\.?\d*)', text)
    if glucose_match:
        glucose_value = float(glucose_match.group(1))
        if glucose_value < 70:
            explanation += (
                f"Glucose level is low: {glucose_value} mg/dL.\n"
                "This may indicate hypoglycemia, which can cause symptoms like dizziness, sweating, or fainting.\n"
                "Consult a doctor for advice on managing low blood sugar.\n"
            )
        elif glucose_value > 140:
            explanation += (
                f"Glucose level is high: {glucose_value} mg/dL.\n"
                "This may indicate hyperglycemia, which could be a sign of diabetes or other metabolic issues.\n"
                "Consult a doctor for proper diagnosis and treatment options.\n"
            )
        else:
            explanation += ""  # No explanation for normal levels

    hematocrit_match = re.search(r'Hematocrit\s*:\s*(\d+\.\d+)\s*%', text)
    if hematocrit_match:
        hematocrit_value = float(hematocrit_match.group(1))
        # Reference ranges may vary, adjust as needed
        if hematocrit_value < 40:
            explanation += (
                f"Hematocrit level is low: {hematocrit_value}%.\n"
                "This may indicate anemia, blood loss, or other conditions.\n"
                "Consult a doctor for further evaluation.\n"
            )
        elif hematocrit_value > 52:
            explanation += (
                f"Hematocrit level is high: {hematocrit_value}%.\n"
                "This may indicate dehydration, certain blood disorders, or other conditions.\n"
                "Consult a doctor for further evaluation.\n"
            )
        else:
            explanation += ""  # No explanation for normal levels

    mcv_match = re.search(r'MCV\s*:\s*(\d+\.\d+)\s*fL', text)
    if mcv_match:
        mcv_value = float(mcv_match.group(1))
        # Reference ranges may vary, adjust as needed
        if mcv_value < 80:
            explanation += (
                f"MCV level is low: {mcv_value} fL.\n"
                "This may indicate microcytic anemia, often caused by iron deficiency.\n"
                "Consult a doctor for further evaluation and treatment.\n"
            )
        elif mcv_value > 100:
            explanation += (
                f"MCV level is high: {mcv_value} fL.\n"
                "This may indicate macrocytic anemia, often caused by vitamin B12 or folate deficiency.\n"
                "Consult a doctor for further evaluation and treatment.\n"
            )
        else:
            explanation += ""  # No explanation for normal levels

    mch_match = re.search(r'MCH\s*:\s*(\d+\.\d+)\s*pg', text)
    if mch_match:
        mch_value = float(mch_match.group(1))
        # Reference ranges may vary, adjust as needed
        if mch_value < 27:
            explanation += (
                f"MCH level is low: {mch_value} pg.\n"
                "This may indicate microcytic anemia, often caused by iron deficiency.\n"
                "Consult a doctor for further evaluation and treatment.\n"
            )
        elif mch_value > 34:
            explanation += (
                f"MCH level is high: {mch_value} pg.\n"
                "This may indicate macrocytic anemia, often caused by vitamin B12 or folate deficiency.\n"
                "Consult a doctor for further evaluation and treatment.\n"
            )
        else:
            explanation += ""  # No explanation for normal levels

    return explanation

if __name__ == '__main__':
    app.run(debug=True)