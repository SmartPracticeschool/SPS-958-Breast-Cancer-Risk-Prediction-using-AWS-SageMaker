from flask import Flask,render_template,request,url_for
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello():
    if request.method=='POST':
        radme=request.form['a']
        permn=request.form['b']
        armn=request.form['c']
        compm=request.form['d']
        radw=request.form['e']
        perw=request.form['f']
        arw=request.form['g']
        copw=request.form['h']
        email=request.form['i']
        try:
            radme=float(radme)
            permn=float(permn)
            armn=float(armn)
            compm=float(compm)
            radw=float(radw)
            perw=float(perw)
            arw=float(arw)
            copw=float(copw)
            email=str(email)
        except:
            return render_template('data.html',err_msg='Enter Valid Data')
        url = "https://13ljl044j1.execute-api.us-east-1.amazonaws.com/test/"
        payload = " {\"data\":\" " + str(radme) + ',' + str(permn) + ',' + str(armn) + ',' + str(compm) + ',' + str(radw) + ',' + str(perw) + ',' + str(arw) + ',' + str(copw) + "\"" + ','+ "\"email\"" +":\""+email+"\""+"}"
        print(payload)

        headers = {
            'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
            'X-Amz-Date': '20200930T095337Z',
            'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIA4KDESJFDUSSQKJSG/20200930/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=b81935cc533d5efb8db465da9c12f4a3ed76ca80089dfc3edebdb39df4fe5f7c',
            'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response=response.text.encode('utf8')
        response=str(response)
        print(response)
        result=response[3:-2]
        print(result)
        if result=="Benign":
            return render_template('data.html',result=result,sug='Please Consult Doctor Earlier')
        else:
            return render_template('data.html',result=result,sug='You\'r health is Fine')
    else:
        return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
