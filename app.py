
from flask import Flask, render_template, request, session
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


@app.route("/form/<string:design>", methods=["GET", "POST"])
def form(design):
    session["design_sess"] = design
    return render_template("form.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    desging_upload = session.get("design_sess")
    if desging_upload not in ["design1", "design2", "design3", "design4", "design5", "design6"]:
        return "Invalid design selection.", 400

    design_name = f"{desging_upload.capitalize()}.html"

    if request.method == "POST":
        try:
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
            service1 = request.form.get("service1")
            service2 = request.form.get("service2")
            service3 = request.form.get("service3")
            service4 = request.form.get("service4")
            about = request.form.get("about")
            insta = request.form.get("instagram")
            git = request.form.get("github")

            key = uuid.uuid1()
            # Image Uploading Method
            img = request.files["dp"]
            img.save(f"static/images/{img.filename}")
            img_new_name = f"{key}{img.filename}"
            os.rename(f"static/images/{img.filename}", f"static/images/{img_new_name}")

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

        except Exception as e:
            return f"An error occurred: {e}", 500

    return "Invalid request method.", 405





if __name__ == "__main__":
    os.makedirs("static/pdfs", exist_ok=True)
    app.run(debug=True)
