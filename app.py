from flask import Flask,render_template, request,session
import uuid
import os


app = Flask(__name__)

app.secret_key = "SecretKey"


@app.route("/")
def home():
    return render_template("home.html")
@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form/<string:design>", methods = ["GET","POST"])
def form(design):
    session["design_sess"] = design
    return render_template("form.html")

@app.route("/upload", methods = ["GET","POST"])
def upload():
    desging_upload = session.get("design_sess")
    if desging_upload == "design1":
        design_name = "Design1.html"
    elif desging_upload == "design2":
        design_name = "Design2.html"
    elif desging_upload == "design3":
        design_name = "Design3.html"
    elif desging_upload == "design4":
        design_name = "Design4.html"
    elif desging_upload == "design5":
        design_name = "Design5.html"
    elif desging_upload == "design6":
        design_name = "Design6.html"

    if request.method == "POST":
        name = request.form.get("firstname")
        lastname = request.form.get("lastname")
        school = request.form.get("school")
        college = request.form.get("college")
        phone = request.form.get("phone")
        email = request.form.get("email")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        service1=request.form.get("service1")
        service2=request.form.get("service2")
        service3=request.form.get("service3")
        service4=request.form.get("service4")
        about = request.form.get("about")
        insta = request.form.get("instagram")
        git = request.form.get("github")

        key = uuid.uuid1()
        #Image Uploading Method
        img = request.files["dp"]
        img.save(f"static/images/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")

   
        user_data = {
        "dname": name,
        "dlname": lastname,
        "dsch": school,
        "img": img_new_name,
        "dcol": college,
        "dph": phone,
        "demail": email,
        "ds1": skill1,
        "ds2": skill2,
        "ds3": skill3,
        "ds4": skill4,
        "dabout": about,
        "git": git,
        "insta": insta,
        "s1": service1,
        "s2": service2,
        "s3": service3,
        "s4": service4
    }

    session["user_data"] = user_data

    return render_template(design_name, **user_data, download_available=True)




    return send_file(pdf_path, as_attachment=True, download_name=pdf_filename)

if __name__ == "__main__":
    os.makedirs("static/pdfs", exist_ok=True)
    app.run(debug=True)