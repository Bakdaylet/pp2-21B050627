import os
print('Exist:', os.access('C:\\Users\Admin\\Desktop\\Новая папка', os.F_OK))
print('Readable:', os.access('C:\\Users\Admin\\Desktop\\Новая папка', os.R_OK))
print('Writable:', os.access('C:\\Users\Admin\\Desktop\\Новая папка', os.W_OK))
print('Executable:', os.access('C:\\Users\Admin\\Desktop\\Новая папка', os.X_OK))