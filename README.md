# potato_leaf_disease

# Potato Leaf Disease Detection Website Guide

Follow these steps to utilize the website for detecting potato leaf diseases:

1. Open this link in your browser: [Potato Leaf Disease Detection](https://potatoleafdisease-guygwmkoh9v7wf7e9w7m5l.streamlit.app/)

2. Click on the "Browse Files" button within the upload images section and select the image of the potato leaf you want to test for disease. Make sure the image is in the **.jpg** format.

   <img src="https://github.com/rajneesh-tetarwal/potato_leaf_disease/assets/145259814/779080a8-0a33-4de9-8af0-c08e0c10c76d" alt="Uploaded Image" width="400">

   Note: The uploaded image will be displayed to ensure you have selected the correct one.
   
   <img src="https://github.com/rajneesh-tetarwal/potato_leaf_disease/assets/145259814/9a0a4150-f80a-4c13-a410-202b1d7d5015" alt="Sample Image" width="400">
   (This image of a healthy potato leaf was randomly downloaded from Google)

3. The test will automatically run once you upload the image, and the final result will be shown below the image.

   <img src="https://github.com/rajneesh-tetarwal/potato_leaf_disease/assets/145259814/33e2c015-5aac-4bb4-a56a-ae3f6f332687" alt="Detection Result" width="400">

4. You can check the checkbox for more information on the final results, such as confidence in the prediction.

   <img src="![image](https://github.com/rajneesh-tetarwal/potato_leaf_disease/assets/145259814/3e09a11f-918f-4f87-9b8a-e27062743103)" alt="Confidence" width="400">


# About the Model

In this project, I've employed a detection model trained on a diverse array of potato leaf disease images sourced from the **plant_village** dataset, which was thoughtfully provided with the project's problem statement.

For an in-depth exploration of the model's inner workings, including its architecture, data preprocessing methodologies, feature extraction techniques, and the model's accuracy, I encourage you to delve into the accompanying Jupyter notebook:

📘 [Explore Model Details](https://github.com/rajneesh-tetarwal/potato_leaf_disease/blob/main/potato_leaf_disease_detection.ipynb)

After training the model using the above techniques I got a training accuracy of 0.9920 and a validation accuracy of 0.9969.

To bring this model to the broader online community, I've developed and deployed a user-friendly website utilizing the Streamlit Python framework. You can access this website via the above mentioned instructions:

🔗 [Visit the Website](https://potatoleafdisease-guygwmkoh9v7wf7e9w7m5l.streamlit.app/)


