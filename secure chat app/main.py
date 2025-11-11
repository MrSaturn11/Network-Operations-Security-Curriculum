from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

#basic setup for any flask web server/app

app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)

rooms = {}

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length): #dont care what _ is as long as loop runs
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
    
    return code

#creating a homepage and room page
#this is how u set up different routes in flask
#use the decorator syntax (@ symbol) then app.route then /something

@app.route("/", methods=["POST","GET"])
def home():
    session.clear() #clears session when user goes  to home page
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name: #if no name is given
            return render_template("home.html", error = "Please enter a name",code =code, name=name) 
            #code = code name = name because whenever u send a post request youre essentially refreshing a window, so when that happens need to pass that data back in
        
        if join != False and not code:
            return render_template("home.html", error = "Please enter a room code.", code =code, name=name)

        room = code 
        if create != False:
            room = generate_unique_code(4)    
            rooms[room] = {"members":0, "messages": []}
        elif code not in rooms:
           return render_template("home.html", error = "Room does not exist or incorrect room code.", code=code, name = name)
        
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))
    
    return render_template("home.html") 

@app.route("/room") #redirects to this route and then renders the room.html
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home"))#cant directly go to /room route without going through homepage first

    return render_template("room.html", code=room, messages=rooms[room]["messages"]) 

@socketio.on("message")
def message(data):
    """
    gets the room the user is in, generating the content they want to send ( and the name, date and time)
    then go to rooms and add whatever message was sent so we have a history of messages
    (rooms[room]["messages"].append(content))
    when user disconnects and reconnects, messages disappear (data is stored in ram)
    also adds another layer of security
    """
    room = session.get("room")
    if room not in rooms: #if someones sending a message in a room that doesnt exist exit out
        return
    
    content = {
        "name":session.get("name"),
        "message":data["data"]

    }
    send(content,to=room)
    rooms[room]["messages"].append(content) 
    print(f"{session.get('name')} said {data['data']}")

@socketio.on("connect") #listens to connection event then puts them in a room
def connect(auth):
    """gets room code and gets name, makes sure they do have a room and a
      name, makes sure room actually exists, if not 
      they leave, then joins room, then sends a message saying {name} joined room {room}"""
    #looks in session for user room and name
    room = session.get("room") 
    name = session.get("name")
    if not room or not name: #optional to code but ensures someone cant connect to socket without going through homepage
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    send({"name":name,"message":"has entered the room"}, to=room)
    rooms[room]["members"]+=1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room") 
    name = session.get("name")
    leave_room(room)
    if room in rooms:
        #deletes room when everyone leaves the room
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <=0:
            del rooms[room] 

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")
        

if __name__ == "__main__":
    socketio.run(app, debug=True)



