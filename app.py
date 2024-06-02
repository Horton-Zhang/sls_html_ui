from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 允许所有跨域请求

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/print')
def print_message():
    print("Hello from Flask!")
    return "Check your console!"

@app.route('/start_print')
def start_print():
    print("start_print")
    return "Check your console!"

@app.route('/stop_print')
def stop_print():
    print("stop_print")
    return "Check your console!"

@app.route('/cancel_print')
def cancel_print():
    print("cancel_print")
    return "Check your console!"

@app.route('/guadao_switch')
def guadao_switch():
    print("guadao_switch")
    return "Check your console!"

@app.route('/reset_switch')
def reset_switch():
    print("reset_switch")
    return "Check your console!"

@app.route('/light_switch', methods=['POST'])
def light_switch():
    data = request.json # 获取JSON数据
    value = data['value'] if 'value' in data else None
    print("light_switch:", value) # 在服务器的控制台打印这个值
    return jsonify({'status': 'Value received'})

@app.route('/pump_switch', methods=['POST'])
def pump_switch():
    data = request.json # 获取JSON数据
    value = data['value'] if 'value' in data else None
    print("pump_switch:", value) # 在服务器的控制台打印这个值
    return jsonify({'status': 'Value received'})

@app.route('/z_axis_up')
def z_axis_up():
    print("z_axis_up")
    return "Check your console!"

@app.route('/z_axis_down')
def z_axis_down():
    print("z_axis_down")
    return "Check your console!"

@app.route('/z_axis_reset')
def z_axis_reset():
    func_name = "z_axis_reset"
    print(func_name)
    return func_name

@app.route('/set_z_axis_spd', methods=['POST'])
def set_z_axis_spd():
    data = request.json # 获取JSON数据
    value = data['value'] if 'value' in data else None
    print("z_axis_spd:", value) # 在服务器的控制台打印这个值
    return jsonify({'status': 'Value received'})

@app.route('/main_power', methods=['POST'])
def set_main_power_value():
    data = request.json # 获取JSON数据
    value = data['value'] if 'value' in data else None
    print("main_power:", value) # 在服务器的控制台打印这个值
    return jsonify({'status': 'Value received'})

@app.route('/Z_aixs_power', methods=['POST'])
def set_Z_aixs_power_value():
    data = request.json # 获取JSON数据
    value = data['value'] if 'value' in data else None
    print("Z_aixs_power:", value) # 在服务器的控制台打印这个值
    return jsonify({'status': 'Value received'})

@app.route('/guadao_power', methods=['POST'])
def set_guadao_power_value():
    data = request.json # 获取JSON数据
    value = data['value'] if 'value' in data else None
    print("guadao_power:", value) # 在服务器的控制台打印这个值
    return jsonify({'status': 'Value received'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
# onToggle(this, flaskAppUrl+'/main_power')