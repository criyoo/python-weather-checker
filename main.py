from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__) # Initialize Flask application

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/health")
def health_check():
    return render_template("health.html")


@app.route("/weather")
def weather():
    city = request.args.get("city")

    # Check if the city is valid
    if not bool(city.strip()) or not city or city == "":
        city = "London"

    weather_data = get_weather(city)

    ## City not found
    if weather_data["cod"] != 200:
        return render_template("city_not_found.html")

    return render_template(
        "weather.html", 
        city=city,
        status=weather_data["weather"][0]["description"].capitalize(),
        temperature=f"{weather_data["main"]["temp"]:.1f}",
        feels_like=f"{weather_data["main"]["feels_like"]:.1f}",
        wind_speed=f"{weather_data["wind"]["speed"]:.1f}",
        wind_direction=weather_data["wind"]["deg"],
        wind_gust=f"{weather_data["wind"]["gust"]:.1f}",
        humidity=weather_data["main"]["humidity"],
        pressure=weather_data["main"]["pressure"],
        description=weather_data["weather"][0]["description"]
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)