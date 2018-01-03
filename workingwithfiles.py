import os
import glob

cd = (os.getcwd())
print(cd)
path = "/Users/ziedbejaoui/PycharmProjects/diveintopython/workingwithfiles.py"
print(os.path.split(path))
splited_path = os.path.split(path)
print(os.path.join('/Users/ziedbejaoui/PycharmProjects/diveintopython/', 'workingwithfiles.py'))
print(glob.glob('*with*.py'))
print(os.stat('workingwithfiles.py'))