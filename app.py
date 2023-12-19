from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bmi_calculator.html')

@app.route('/calculate_bmi')
def calculate_bmi():
    try:
        weight = float(request.args.get('weight'))
        height = float(request.args.get('height')) / 100  # Convert height to meters

        bmi = weight / (height ** 2)

        return jsonify({'bmi': bmi})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
