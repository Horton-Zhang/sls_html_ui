
from sls_commands import sls_send_command
from flask import Flask, render_template, request, jsonify, send_from_directory
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app) # 允许所有跨域请求

@app.route('/<path:filename>')
def index(filename):
    return render_template(filename)

@app.route('/assets/<path:filename>')
def serve_static_file(filename):
    return send_from_directory('assets', filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico')

@app.route('/print')
def print_message():
    print("Hello from Flask!")
    return "Check your console!"

@app.route('/start_print')
def start_print():
    sls_send_command("start_print")
    return "Check your console!"

@app.route('/stop_print')
def stop_print():
    sls_send_command("stop_print")
    return "Check your console!"

@app.route('/cancel_print')
def cancel_print():
    sls_send_command("cancel_print")
    return "Check your console!"

@app.route('/guadao_switch')
def guadao_switch():
    sls_send_command("scrape")
    return "Check your console!"

@app.route('/reset_switch')
def reset_switch():
    sls_send_command("reset")
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
    sls_send_command("z_axis_up")
    return "Check your console!"

@app.route('/z_axis_down')
def z_axis_down():
    sls_send_command("z_axis_down")
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

def run():
    app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
    run()
