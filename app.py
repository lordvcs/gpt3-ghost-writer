import os
from flask import Flask, request, session
from story import write_story, append_to_story, session_prompt

app = Flask(__name__)
app.config["SECRET_KEY"] = "top-secret!"


@app.route("/bot", methods=["POST"])
def ghost_writer():
    incoming_msg = request.values.get("Body")
    file1 = open("spookystory.txt", "a")
    if incoming_msg == "the end":
        file1.close()
        session.pop("session_story", None)
        return str("The end...")
    session_story = session.get("session_story")
    # next part of the story generated by gpt3
    story = write_story(session_story)
    if os.stat("spookystory.txt").st_size == 0:
        file1.write(session_prompt)
    # save the appended whole story to session
    session["session_story"] = append_to_story(story, session_story)
    file1.write(story)

    # msg = MessagingResponse()
    # msg.message(story)

    return str(story)


if __name__ == "__main__":
    app.run(debug=True)