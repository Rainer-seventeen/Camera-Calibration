import pickle
import glob

# 读取 pickle 文件
# outputs = glob.glob('out/*.pkl')
# for output in outputs:
#     f = open(output,'rb')
#     data = pickle.load(f)
#     print(data)

    
f = open('out\cameraMatrix.pkl','rb')
data = pickle.load(f)
print(data)