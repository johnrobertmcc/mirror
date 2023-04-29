import tkinter as tk
import requests
import json

window = tk.Tk()

window.attributes('-fullscreen', True)

window['bg'] = 'black'

label = tk.Label(window, text="This is a test", font=('Monospace 18 bold'), background='black', foreground='white')

text = tk.Text(window, wrap="word", fg='white', bg='black')
text.config(font="Monospace, 16")

api_url = "https://otp-mta-prod.camsys-apps.com/otp/routers/default/nearby?stops=MTASBWY:L19&apikey=2ctbNX4XX7oS5ywqVQT86DntRQQw59eB&groupByParent=true&routes=&timeRange=3600"

# def get_ltrain():
response = requests.get(api_url).text
response_info = json.loads(response)
stop = response_info[0]["stop"]["name"]
print(stop)

text.insert('1.0', stop)
print(text)

label.pack(pady=20)
text.pack(pady=20)

window.mainloop()
