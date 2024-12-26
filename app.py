from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import math

app = Flask(__name__)

class CollisionAvoidanceSystem:
    def __init__(self):
        self.vehicle_location = (28.644800, 77.216721)  # Default location
        self.obstacles = []
        self.threshold_distance = 0.05  # Threshold in kilometers
        self.abs_engaged = False

    def simulate_obstacle(self):
        """Simulate an obstacle at random GPS coordinates."""
        offset = random.uniform(-0.01, 0.01)
        obstacle_location = (self.vehicle_location[0] + offset, self.vehicle_location[1] + offset)
        self.obstacles.append(obstacle_location)
        if len(self.obstacles) > 10:
            self.obstacles = self.obstacles[-10:]

    def detect_collision(self):
        """Detect potential collisions."""
        for obstacle in self.obstacles:
            distance = self.calculate_distance(self.vehicle_location, obstacle)
            if distance <= self.threshold_distance:
                self.engage_abs()
                return True, obstacle, distance
        self.disengage_abs()
        return False, None, None

    @staticmethod
    def calculate_distance(coord1, coord2):
        """Calculate distance using the Haversine formula."""
        R = 6371
        lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
        lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def update_vehicle_location(self, lat, lon):
        """Update the vehicle's location."""
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            raise ValueError("Invalid latitude or longitude.")
        self.vehicle_location = (lat, lon)

    def engage_abs(self):
        self.abs_engaged = True

    def disengage_abs(self):
        self.abs_engaged = False

# Initialize the collision avoidance system
system = CollisionAvoidanceSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        if 'simulate_obstacle' in request.form:
            system.simulate_obstacle()
        elif 'check_collision' in request.form:
            collision_status, obstacle, distance = system.detect_collision()
            return render_template('demo.html', obstacles=system.obstacles,
                                   collision_status=collision_status,
                                   alert=f"Collision Alert! Obstacle at {obstacle} ({distance:.2f} km)"
                                   if collision_status else "No collisions detected.")
        elif 'update_location' in request.form:
            try:
                lat = float(request.form['latitude'])
                lon = float(request.form['longitude'])
                system.update_vehicle_location(lat, lon)
            except ValueError as e:
                return render_template('demo.html', error=str(e), obstacles=system.obstacles)
    return render_template('demo.html', obstacles=system.obstacles)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
