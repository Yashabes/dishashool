from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        DAY = request.form['day']
        if(DAY=='SUNDAY' or DAY=='Sunday' or DAY=='sunday'):
            tempee=1
        elif(DAY=='MONDAY' or DAY=='MOnday' or DAY=='monday'):
            tempee=2
        elif(DAY=='TUESDAY' or DAY=='Tuesday' or DAY=='tuesday'):
            tempee=3
        elif(DAY=='WEDNESDAY' or DAY=='Wednesday' or DAY=='wednesday'):
            tempee=4
        elif(DAY=='THURSDAY' or DAY=='Thursday' or DAY=='thursday'):
            tempee=5
        elif(DAY=='FRIDAY' or DAY=='Friday' or DAY=='friday'):
            tempee=6
        elif(DAY=='SATURDAY' or DAY=='Saturday' or DAY=='saturday'):
            tempee=7    
        else:
            tempee=8
        if(tempee==1):
            result="AVOID WEST DIRECTION WHILE DOING WORSHIP OR TRAVELLING ON THIS DAY"
        elif(tempee==2):  
            result="AVOID EAST DIRECTION WHILE DOING WORSHIP OR TRAVELLING ON THIS DAY"
        elif(tempee==3):
            result="AVOID NORTH DIRECTION WHILE DOING WORSHIP OR TRAVELLING ON THIS DAY"
        elif(tempee==4):
            result="AVOID NORTH DIRECTION WHILE DOING WORSHIP OR TRAVELLING ON THIS DAY" 
        elif(tempee==5):
            result="AVOID SOUTH DIRECTION WHILE DOING WORSHIP OR TRAVELLING ON THIS DAY"
        elif(tempee==6):
            result="AVOID WEST DIRECTION WHILE DOING WORSHIP OR TRAVELLING ON THIS DAY"
        elif(tempee==7):
            result="AVOID EAST DIRECTION WHILE DOING WORSHIP OR TRAVELLING ON THIS DAY"
        else:
            result="ENTER A VALID DAY"
        return render_template('website.html',result=result)
    return render_template('website.html',result=None)
if __name__ == '__main__' :
    app.run(debug=True)
    
            

