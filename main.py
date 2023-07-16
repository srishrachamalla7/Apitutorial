from flask import Flask,request,jsonify

app= Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data={
        
        "user_id" : user_id,
        "name": "something"

    }
    known = request.args.get("known")
    if known:
        user_data["known"] = known

    return jsonify(user_data),200

@app.route("create-user", methods=["POST"])
def create_user():
    data= request.get_json()

    return jsonify(data),201



if __name__ == "__main__":
    app.run(debug=True)
