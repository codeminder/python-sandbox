import numpy as np 
from vispy import app, visuals, scene

# Создаем данные

N = 100
pos = np.zeros((N, 3))
colors = np.ones((N, 4))

pos[:, 0] = np.linspace(-0.9, 0.9, N) 
colors[:, 0] = np.linspace(0, 1, N)

# Создаем канвас 
canvas = scene.SceneCanvas(keys='interactive', show=True)

# Добавляем точечный график

scatter = visuals.markers()  
scatter.set_data(pos, face_color=colors) 
canvas.central_widget.add_view().add(scatter)
scatter.set_data(pos, face_color=colors) 
canvas.central_widget.add_view().add(scatter)

# Запускаем приложение 
app.run()