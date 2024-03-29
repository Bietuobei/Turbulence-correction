import matplotlib.pyplot as plt
import numpy as np

def draw_curve(filename):
    data=np.loadtxt(filename,dtype=np.float32)
    y1=data[:,1]
    x1=range(0,50)
    plt.plot(x1,y1,label='Fist line',linewidth=1,color='r',marker='o',
             markerfacecolor='blue',markersize=3)
    plt.show()

def main():
    filename = 'E:\github projects\contrastive-unpaired-translation-master\checkpoints\superposition_CUT\loss_log.txt'
    draw_curve(filename)
    print('Finish')

if __name__=='__main__':
    main()
