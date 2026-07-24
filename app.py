from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Docker",
        "description": "Understand Docker images and containers.",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn Trivy",
        "description": "Scan Docker images.",
        "completed": True
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks")
def task_list():
    return render_template("tasks.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]

        task = {
            "id": len(tasks) + 1,
            "title": title,
            "description": description,
            "completed": False
        }

        tasks.append(task)

        return redirect(url_for("task_list"))

    return render_template("add_task.html")


@app.route("/complete/<int:id>")
def complete_task(id):

    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            break

    return redirect(url_for("task_list"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)