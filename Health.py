def assess_health_risk(symptoms):
    
    
    high_risk_symptoms = ["dizziness","dizzy","chest pain","shortness of breath","cough","wheezing","heart palpitation","heart hurting"]
    mild_risk_symptoms = ["headaches","head hurts","phlegm","watery eyes","eyes are watering","nose irritation","my nose is irrtating me","throat irritation","throat hurts","sinus irritation"]
    
    for symptom in high_risk_symptoms:
        if symptom in symptoms:
            return "High risk - Seek immediate medical attention"
    
    for symptom in mild_risk_symptoms:
        if symptom in symptoms:
            return "Mild risk - Monitor closely and consult a healthcare professional"

def main():
    print("Wildfire Smoke Health Information App")
    print("Provide health information for your child during wildfire smoke events.")
    
    while True:
        symptoms = input("Describe any symptoms (separate with commas): ")
        health_risk = assess_health_risk(symptoms)
        
        print("Health Risk Assessment:", health_risk, ", for more information, please reach out to the Public Health Agency of Canada at Toll-Free 1-844-280-5020")
        
        another_child = input("Do you want to assess another child (yes/no)? ")
        if another_child != 'yes':
            break

    print("Thank you for using the Wildfire Smoke Health Information App.")

main()
