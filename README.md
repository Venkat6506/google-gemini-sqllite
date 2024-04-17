# google-gemini-sqllite
This application will generate SQL queries using gemini-pro llm
## Step to run Google Gemini Sqllite in local/windows
- Clone google-gemini-sqllite in your local machine
- Download and install Anaconda from https://www.anaconda.com/download
- Type anaconda on windows search and open anaconda command prompt
- Navigate to google-gemini-sqllite progect (in step 1) from conda prompt and/by follow below commands
    * cd <basepath>/google-gemini-sqllite
    * conda create -n ggp-sqllite python=3.11 -y
    * conda activate ggp-sqllite
    * pip install -r requirement.txt
- Create a file with name '.env' in google-gemini folder
- Add below line in .env file
    * GOOGLE_API_KEY="<Supply your secret token here>"
- Run MultiLanguage Invoice Extractor with below command
    * streamlit run app.py --server.port 8080
    * Access the application on http://localhost:8080 from any of your favorite browser
    * ask any question e.g. give me all the student details with category as 'First Class' if student marks are greater or equal to 95, 'Second Class' if marks is in between 85 and 94 and 'Third Class' if greater than or equal to75 and less than 84?
    * Click on 'Ask the question' to get the information.