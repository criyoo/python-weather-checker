from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__) # Initialize Flask application

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/weather")
def weather():
    # city = request.form["city"]
    city = request.args.get("city").strip()

    # Check if the city is valid
    if not bool(city.strip()) or not city or city == "":
        city = "London"
    weather_data = get_weather(city)

    # City not found
    if weather_data["cod"] == "404" or not ["cod"] == "200":
        return render_template("city_not_found.html")

    return render_template(
        "weather.html", 
        title=city,
        status=weather_data["weather"][0]["description"].capitalize(),
        temperature=f"{weather_data["main"]["temp"]:.1f}",
        feels_like=f"{weather_data["main"]["feels_like"]:.1f}",
        description=weather_data["weather"][0]["description"]
    )



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)