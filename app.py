from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            age=int(request.form.get('age')),
            workclass=str(request.form.get('workclass')),
            education_num=int(request.form.get('education_num')),
            marital_status=str(request.form.get('marital_status')),
            occupation=int(request.form.get('occupation')),
            race=str(request.form.get('race')),
            sex=str(request.form.get('sex')),
            capital_gain=int(request.form.get('capital_gain')),
            capital_loss=int(request.form.get('capital_loss')),
            hours_per_week=int(request.form.get('hours_per_week')),
            native_country=int(request.form.get('native_country'))
            
            
            
            
           
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        def final_result(pred):
            if pred==1:
                result='Income is more than 50k'
            else:
                result = 'Income is less than 50k'
            return result
        
        final_results = final_result(pred)
            

        return render_template('results.html',final_results = final_result(pred))






if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
