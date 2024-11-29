# **🚗 Road Accident Severity Prediction**

## **🌟 Problem Statement**  
Road accidents are a major public health issue, causing fatalities, injuries, and property damage worldwide. Predicting the severity of accidents based on key factors such as weather, lighting, and road conditions can help mitigate risks and improve road safety.  

**🔍 Solution:**  
This project uses **machine learning** techniques to predict the severity of road accidents based on relevant features from historical data, providing actionable insights for traffic management and safety improvements.

---

## **💡 Project Idea**  

### **Features:**  
- **🚦 Predict Severity:** Classifies road accidents based on severity (e.g., minor, moderate, severe).  
- **📊 Factor Analysis:** Considers key factors like road type, weather, and driver experience to make predictions.  
- **⚖️ Balance Data:** Employs SMOTE (Synthetic Minority Oversampling Technique) to handle class imbalance.  
- **🎯 Evaluate Model:** Measures model performance with accuracy, confusion matrix, and classification report.

---

## **⚙️ Approach**  

### **📂 Data Preparation**  
1. **Load Dataset:** Reads the cleaned accident dataset (`cleaned.csv`).  
2. **Feature Selection:** Extracts relevant features such as age, weather, light conditions, etc.  
3. **Target Variable:** Severity of accidents as the prediction target.  

### **📑 Data Splitting**  
- Splits the data into **training (70%)** and **testing (30%)** sets for model evaluation.  

### **🔄 Preprocessing**  
- **One-Hot Encoding:** Encodes categorical features for compatibility with machine learning models.  
- **SMOTE:** Balances the dataset by oversampling minority classes to address class imbalance.  

### **🧪 Model Training**  
- **Pipeline:** Combines preprocessing and a **Random Forest Classifier** for seamless execution.  
- Trains the model on resampled data for improved generalization on imbalanced datasets.  

### **📉 Evaluation Metrics**  
- **Accuracy Score:** Overall performance of the model.  
- **Confusion Matrix:** Breakdown of predicted vs. actual classifications.  
- **Classification Report:** Precision, recall, and F1-score for each class.

---

## **📊 Results**  
The model provides the following evaluation metrics:  
- **Accuracy:** Proportion of correct predictions.  
- **Confusion Matrix:** Insights into classification errors.  
- **Classification Report:** Detailed performance metrics for each severity level.  

---

## **💻 Tech Stack**  

### **Data Handling**  
- **Pandas:** For loading and manipulating the dataset.  

### **Preprocessing**  
- **Sklearn:**  
  - **StandardScaler:** For feature scaling (if needed).  
  - **OneHotEncoder:** Converts categorical data into numerical format.  
  - **ColumnTransformer:** Applies transformations selectively to columns.  

### **Balancing Technique**  
- **Imbalanced-learn:**  
  - **SMOTE:** Synthetic oversampling for balanced class distribution.  

### **Modeling**  
- **Random Forest Classifier:**  
  - Ensemble-based algorithm for robust classification.  
  - Handles non-linearity and complex interactions effectively.  

### **Evaluation**  
- **Sklearn Metrics:**  
  - `accuracy_score`, `confusion_matrix`, `classification_report`.  

---

🌍 Project Impact
1. Enhanced Road Safety

By predicting accident severity, this project enables traffic authorities and policymakers to identify high-risk scenarios and implement safety measures proactively.
2. Data-Driven Decisions

Provides valuable insights into the relationship between accident factors like weather, lighting, and road type, helping authorities prioritize infrastructure improvements.
3. Real-Time Applications

The model can be integrated into navigation systems or traffic monitoring dashboards to alert drivers about potential accident risks, reducing the likelihood of severe incidents.
4. Cost Savings

Early prediction of accident severity can reduce response times for emergency services, saving lives and minimizing economic losses due to traffic congestion and medical expenses.
5. Public Awareness

Offers educational opportunities to inform the public about accident causes, promoting safer driving behaviors and adherence to traffic regulations.
6. Global Applicability

With suitable localization and additional features, this project can be deployed worldwide, addressing road safety concerns in diverse environments and saving lives globally.

## **🔮 Future Scope**  

- **📈 Feature Expansion:** Include additional features like time of day, vehicle type, or driver health.  
- **🤖 Advanced Models:** Experiment with more advanced models like Gradient Boosting or Neural Networks.  
- **📍 Geographical Insights:** Add geospatial data for location-specific predictions.  
- **📱 Mobile Integration:** Create a real-time mobile app for accident risk alerts.  
- **🌐 Public Dashboard:** Develop a web-based interface to visualize accident trends and predictions interactively.  

---
