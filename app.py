from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

def categorize_prediction(value):
    if value < 1:
        return "A"
    elif value < 2:
        return "B"
    elif value < 3:
        return "C"
    else:
        return "D"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Debugging: Print form data
        print(request.form)

        # Get form data safely
        age = int(request.form.get('age', 0))
        studyHourPerWeek = int(request.form.get('study_hours', 0))
        onlineCoursesCompleted = int(request.form.get('online_courses', 0))
        assignmentCompletionRate = int(request.form.get('completion_rate', 0))
        examScore = int(request.form.get('exam_score', 0))
        attendanceRate = int(request.form.get('attendance', 0))
        timeSpentOnSocialMedia = int(request.form.get('social_media', 0))
        hoursOfSleep = int(request.form.get('sleep', 0))

        participation = int(request.form.get('participation', "No") == "Yes")
        techUse = int(request.form.get('tech_use', "No") == "Yes")

        # Gender Mapping
        gender = request.form.get('gender', 'Other')
        gMale = int(gender == "Male")
        gFemale = int(gender == "Female")
        gOther = int(gender == "Other")

        # Learning Style Mapping
        preferredLearningStyle = request.form.get('learning_style', 'Read/Write')
        plsAuditory = int(preferredLearningStyle == "Auditory")
        plsVisual = int(preferredLearningStyle == "Visual")
        plsKinesthetic = int(preferredLearningStyle == "Kinesthetic")
        plsReadWrite = int(preferredLearningStyle == "Read/Write")

        # Stress Level Mapping
        selfReportedStressLevel = request.form.get('stress_level', 'Low')
        stressMapping = {"Low": 0, "Medium": 1, "High": 2}
        stressLevel = stressMapping.get(selfReportedStressLevel, 0)

        # Prepare input data
        input_data = np.array([[age, studyHourPerWeek, onlineCoursesCompleted, participation, 
                                assignmentCompletionRate, examScore, attendanceRate, techUse, timeSpentOnSocialMedia, 
                                hoursOfSleep, plsAuditory, plsKinesthetic, plsReadWrite, plsVisual, 
                                gFemale, gMale, gOther, stressLevel]])

        # Make prediction
        numerical_prediction = model.predict(input_data)[0]  # Get the numerical prediction

        # Clip prediction to ensure it doesn't include 4
        numerical_prediction = np.clip(numerical_prediction, 0, 3.9999)  # Cap to just below 4

        # Convert to category
        categorical_prediction = categorize_prediction(numerical_prediction)


        return render_template('results.html', prediction=categorical_prediction)

    except Exception as e:
        return f"Error: {str(e)}", 400  # Return error for debugging

if __name__ == '__main__':
    app.run(debug=True)
